from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import TopicFather, TableForm03, SpanishSentence, EnglishSentence, TablaMaestra, StudentPerformance
from .serializers import TopicFatherSerializer, TableForm03Serializer
from django.http import JsonResponse
from spellchecker import SpellChecker
from rest_framework.decorators import api_view
from openai import OpenAI
import random
import os
import environ
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from difflib import ndiff
from django.utils.html import format_html
from django.contrib.auth.models import AnonymousUser

User = get_user_model()  # Esto asegurará que obtienes el modelo de usuario correcto


# Configura tu cliente OpenAI
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def openai_request(messages, max_tokens=50):
    """
    Realiza una solicitud a OpenAI y devuelve el contenido generado.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"


class CrearOracionView(APIView):
    permission_classes = [IsAuthenticated]  # Requiere autenticación

    def post(self, request):
        try:
            # Verificar el usuario autenticado
            user = request.user
            if not user.is_authenticated:
                return Response(
                    {"error": "Usuario no autenticado. Por favor, inicia sesión."},
                    status=status.HTTP_401_UNAUTHORIZED
                )

            # Lógica de selección aleatoria y creación de oración
            # Seleccionar un tema aleatorio
            random_topic = TopicFather.objects.order_by('?').first()
            if not random_topic:
                return Response(
                    {"error": "No hay datos disponibles en la tabla 'TopicFather'."},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Seleccionar una fila aleatoria de TablaMaestra
            random_row = TablaMaestra.objects.order_by('?').first()
            if not random_row:
                return Response(
                    {"error": "No hay datos disponibles en la tabla 'TablaMaestra'."},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Construir relación y mensaje
            relacion = f"{
                random_row.verb_tense} - {random_row.grammatical_category} - {random_row.related_subtopic}"
            messages = [
                {"role": "system", "content": "You are a helpful language tutor that creates sentences in Spanish."},
                {"role": "user", "content": f"Create a sentence in Spanish based on:\n"
                 f"Tiempo Verbal: {random_row.verb_tense}\n"
                 f"Categoría: {random_row.grammatical_category}\n"
                 f"Submateria: {random_row.related_subtopic}\n"
                 f"Topic: {random_topic.topic_father.capitalize()}.\n\n"
                 f"Write only one sentence."}
            ]

            # Realizar solicitud a OpenAI
            oracion = openai_request(messages)

            # Guardar datos en StudentPerformance
            StudentPerformance.objects.create(
                id_fk_tabla_maestra=random_row,
                id_fk_user=user,  # Relación con usuario autenticado
                id_fk_topic_father=random_topic,
                oracion_generada=oracion
            )

            # Retornar respuesta
            return Response(
                {
                    "tema_seleccionado": random_topic.topic_father.capitalize(),
                    "relacion_seleccionada": relacion,
                    "oracion_generada": oracion,
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RevisarTraduccionView(APIView):
    def post(self, request):
        oracion_generada = request.data.get('oracion_generada')
        respuesta_alumno = request.data.get('respuesta_alumno')

        if not oracion_generada or not respuesta_alumno:
            return Response(
                {"error": "Debes proporcionar 'oracion_generada' y 'respuesta_alumno'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Obtener la traducción correcta de OpenAI
            messages_translation = [
                {"role": "system", "content": "You are a helpful language tutor that provides only direct translations."},
                {"role": "user", "content": f"Translate the following sentence into English:\n\n{
                    oracion_generada}"}
            ]
            correct_answer = openai_request(
                messages_translation, max_tokens=50)

            # Normalizar la respuesta correcta eliminando el punto final si lo tiene
            if correct_answer.endswith('.'):
                correct_answer = correct_answer[:-1]

            # Resaltar diferencias entre la respuesta del estudiante y la correcta
            highlighted_diff = highlight_differences(
                respuesta_alumno, correct_answer)

            def evaluate_translation(category, max_score):
                messages = [
                    {"role": "system", "content": f"You are an English tutor that evaluates translations and assigns a strict score from 0 to {
                        max_score}."},
                    {"role": "user", "content": f"Evaluate the following translation based on {category}. Provide a strict integer score.\n\n"
                     f"Original sentence in Spanish: {oracion_generada}\n"
                     f"Student's translation: {respuesta_alumno}\n\n"
                     f"Provide an integer score, do not include explanations."}
                ]
                response = openai_request(messages, max_tokens=10)
                if not response or not response.strip().isdigit():
                    return 0  # Puntaje predeterminado en caso de error
                return int(response.strip())

            # Obtener puntajes
            score_lexical_accuracy = evaluate_translation(
                "Lexical Accuracy", 3)
            score_grammatical_structure = evaluate_translation(
                "Grammatical Structure", 3)
            score_natural_fluency = evaluate_translation("Natural Fluency", 2)
            score_punctuation_spelling = evaluate_translation(
                "Punctuation and Spelling", 1)
            score_contextual_usage = evaluate_translation(
                "Contextual Usage", 1)

            # Calcular el puntaje total
            total_score = (
                score_lexical_accuracy +
                score_grammatical_structure +
                score_natural_fluency +
                score_punctuation_spelling +
                score_contextual_usage
            )

            # Obtener feedback constructivo
            messages_feedback = [
                {"role": "system",
                    "content": "You are an encouraging and constructive English tutor."},
                {"role": "user", "content": f"Provide brief constructive feedback with a recommendation and words of encouragement based on the following:\n\n"
                 f"Original sentence in Spanish: {oracion_generada}\n"
                 f"Student's translation: {respuesta_alumno}\n\n"
                 f"Correct translation: {correct_answer}"}
            ]
            feedback = openai_request(messages_feedback, max_tokens=100)

            # Obtener ejemplos y notas desde OpenAI
            messages_example_note = [
                {"role": "system", "content": "You are an English tutor providing clear and concise feedback."},
                {"role": "user", "content": f"Based on the following:\n\n"
                 f"Original sentence in Spanish: {oracion_generada}\n"
                 f"Student's translation: {respuesta_alumno}\n\n"
                 f"Correct translation: {correct_answer}\n\n"
                 f"Provide examples of key areas to improve and a brief note summarizing what to focus on for better translations. "
                 f"Respond in the following format:\n\n"
                 f"key areas to improve:\n"
                 f"- <category>: '<incorrect> → <correct>'\n"
                 f"Note: <brief note summarizing areas to focus on>"}
            ]
            example_note_response = openai_request(
                messages_example_note, max_tokens=100)

            # Procesar respuesta para extraer examples y note
            try:
                examples_text = ""
                note_text = ""

                if "key areas to improve:" in example_note_response and "Note:" in example_note_response:
                    parts = example_note_response.split("Note:")
                    # Extraer la parte de ejemplos
                    key_areas = parts[0].strip()
                    # Extraer la parte de la nota
                    note_text = f"Note: {parts[1].strip()}"
                else:
                    raise ValueError(
                        "El formato de la respuesta de OpenAI no es válido.")

            except Exception as e:
                return Response(
                    {"error": f"El feedback obtenido no es válido: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            # Retornar las diferencias resaltadas, el puntaje, el feedback, ejemplos y nota
            return Response({
                'highlighted_diff': highlighted_diff,
                'score': total_score,
                'feedback': feedback,
                'key_areas': key_areas,
                'note': note_text
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": f"Hubo un error procesando la solicitud: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Función para resaltar diferencias
def highlight_differences(user_answer, correct_answer):
    # Utiliza difflib.ndiff para calcular las diferencias entre ambas respuestas
    diff = list(ndiff(user_answer.split(), correct_answer.split()))
    diff_html = []

    for part in diff:
        # Eliminar el prefijo (-, +, o espacio) y tomar solo la palabra relevante
        word = part[2:]  # Extraer la palabra quitando el prefijo

        if part.startswith('-'):
            # Palabra incorrecta en la respuesta del usuario (rojo y tachado)
            diff_html.append(
                f'<span style="color: red; text-decoration: line-through;">{
                    word}</span>'
            )
        elif part.startswith('+'):
            # Palabra faltante sugerida por el tutor (verde y negrita)
            diff_html.append(
                f'<span style="color: green; font-weight: bold;">{word}</span>'
            )
        elif part.startswith(' '):
            # Palabras que coinciden entre ambas respuestas
            diff_html.append(word)

    # Unir las palabras con un espacio entre ellas
    return format_html(' '.join(diff_html))


class CreateTableForm03View(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TableForm03Serializer(data=request.data)
        if serializer.is_valid():
            # Asigna el usuario actual al id_FK
            serializer.save(id_FK=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Nueva vista para guardar las oraciones


@api_view(['POST'])
def save_sentences(request):
    try:
        data = request.data

        # Utiliza un usuario predeterminado si no se pasa el usuario autenticado
        user = request.user if request.user.is_authenticated else User.objects.get(
            id=1)

        table_form_03_data = {
            'id_FK': user,  # Usuario predeterminado o autenticado
            'Title_Name': data.get('Title_Name'),
            'Language': data.get('Language'),
            'Topic_Father': data.get('Topic_Father'),
            'Topic_Son': data.get('Topic_Son'),
            'Description': data.get('Description'),
            'Level_CEFR': data.get('Level_CEFR'),
            'number_setence': len(data.get('spanish_sentences', []))
        }

        # Guardar en TableForm03
        table_form_03 = TableForm03.objects.create(**table_form_03_data)

        # Guardar oraciones en español
        for sentence in data.get('spanish_sentences', []):
            SpanishSentence.objects.create(
                id_FK=table_form_03,
                Sentence=sentence.get('Sentence')
            )

        # Guardar oraciones en inglés
        for sentence in data.get('english_sentences', []):
            EnglishSentence.objects.create(
                id_FK=table_form_03,
                Sentence=sentence.get('Sentence')
            )

        return Response({"message": "Sentences saved successfully."}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def check_spelling(request):
    language = request.GET.get('language', 'en').lower()
    words = request.GET.getlist('words[]')
    num_tokens = int(request.GET.get('num_tokens', 100))
    topic_father = request.GET.get('topic_father', '')
    description = request.GET.get('description', '')
    cefr_level = request.GET.get('cefr_level', '')

    # Nuevo parámetro para omitir el chequeo ortográfico
    skip_spell_check = request.GET.get(
        'skip_spell_check', 'false').lower() == 'true'

    language_codes = {
        'english': 'en',
        'spanish': 'es',
        'french': 'fr',
        'japanese': 'ja',
        'german': 'de',
        'chinese': 'zh'
    }
    language_code = language_codes.get(language, 'en')

    try:
        # Solo hacer el spell checking si no se ha pedido omitirlo
        if not skip_spell_check:
            spell = SpellChecker(language=language_code)
            misspelled = spell.unknown(words)

            if misspelled:
                response = {
                    'status': 'error',
                    'message': f"Misspelled words: {', '.join(misspelled)}"
                }
                return JsonResponse(response)

        # Construir el prompt para OpenAI
        prompt = (
            f"Language: {language}. Topics: {', '.join(words)}. "
            f"Topic Father: {topic_father}. Description: {description}. "
            f"CEFR Level: {cefr_level}."
        )

        num_sentences = max(1, num_tokens // 100)

        messages = [
            {"role": "system",
                "content": f"You are a tutor creating sentences in {language}."},
            {"role": "user", "content": f"Create {num_sentences} sentences based on the following topics: {
                prompt}. Provide the sentences only in {language}."}
        ]

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=num_tokens
        )

        suggestions = completion.choices[0].message.content
        sentences = [line.strip()
                     for line in suggestions.split("\n") if line.strip()]

        # Return the sentences in JSON
        return JsonResponse({
            'status': 'success',
            'message': 'Sentences generated successfully.',
            'sentences': sentences
        })
    except ValueError as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': f'Internal server error: {str(e)}'}, status=500)


class TopicFatherListView(generics.ListAPIView):
    serializer_class = TopicFatherSerializer

    def get_queryset(self):
        # Obtén el idioma del parámetro en la solicitud
        language = self.request.query_params.get('language', 'en')
        # Para depurar y verificar el valor recibido
        print(f"Language received: {language}")

        # Elige la columna de acuerdo al idioma
        if language == 'en':
            return TopicFather.objects.values('topic_father_en').order_by('topic_father_en')
        elif language == 'fr':
            return TopicFather.objects.values('topic_father_fr').order_by('topic_father_fr')
        elif language == 'de':
            return TopicFather.objects.values('topic_father_de').order_by('topic_father_de')
        elif language == 'pt':
            return TopicFather.objects.values('topic_father_pt').order_by('topic_father_pt')
        else:
            return TopicFather.objects.values('topic_father').order_by('topic_father')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return JsonResponse(list(queryset), safe=False)

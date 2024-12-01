from rest_framework import generics
from django.db.models import Q
from apps.skill_builder.models import TableForm03, SpanishSentence, EnglishSentence
from apps.skill_practice.models import Nivel, Tema, OpcionNivel
from .serializers import NivelSerializer, TemaSerializer, TableForm03Serializer, SpanishSentenceSerializer, EnglishSentenceSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from openai import OpenAI
import environ
import os
import logging
import traceback
from difflib import ndiff
from django.utils.html import format_html

# Configura tu cliente OpenAI
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


class CrearOracionView(APIView):
    def post(self, request):
        nivel = request.data.get('nivel')
        contenido = request.data.get('contenido')
        tema = request.data.get('tema')
        descripcion = request.data.get('descripcion')

        try:
            messages = [
                {"role": "system", "content": "You are a helpful language tutor that creates sentences in Spanish."},
                {"role": "user", "content": f"Create a sentence in Spanish using the following details:\n"
                 f"Level: {nivel}\n"
                 f"Content: {contenido}\n"
                 f"Topic: {tema}\n"
                 f"Description: {descripcion}\n\n"
                 f"Write only one sentence."}
            ]
            completion_translation = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                max_tokens=50
            )
            # Cambiado `response` por `completion_translation`
            oracion = completion_translation.choices[0].message.content.strip()
            return Response({"oracion": oracion}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class NivelesListView(APIView):
    def get(self, request):
        niveles = Nivel.objects.all()
        serializer = NivelSerializer(niveles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContenidosListView(APIView):
    def post(self, request):
        try:
            # Obtén el nivel del cuerpo de la solicitud
            nivel_nombre = request.data.get('nivel')
            if nivel_nombre:
                contenidos = OpcionNivel.objects.filter(
                    nivel__nombre=nivel_nombre)
                data = [{"label": contenido.texto, "value": contenido.texto}
                        for contenido in contenidos]
                return Response(data, status=status.HTTP_200_OK)
            return Response({"error": "Nivel no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Imprime el error en la consola y responde con el error
            print("Error en ContenidosListView:", e)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TemasListView(APIView):
    def get(self, request):
        try:
            temas = Tema.objects.all()
            data = [{"label": tema.nombre, "value": tema.nombre}
                    for tema in temas]
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print("Error en TemasListView:", e)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Vista API para revisar la traducción
class RevisarTraduccionView(APIView):
    def post(self, request):
        oracion_generada = request.data.get('oracion_generada')
        respuesta_alumno = request.data.get('respuesta_alumno')

        try:
            # Crear el mensaje para obtener la traducción correcta
            messages_translation = [
                {"role": "system", "content": "You are a helpful language tutor that provides only direct translations."},
                {"role": "user", "content": f"Translate the following sentence into English:\n\n{
                    oracion_generada}"}
            ]

            # Llamada a OpenAI para obtener la traducción correcta
            completion_translation = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages_translation,
                max_tokens=50  # Limitar los tokens para la traducción
            )

            # Extraer la traducción correcta generada por OpenAI
            correct_answer = completion_translation.choices[0].message.content.strip(
            )
            # Quitar el punto final si está presente
            if correct_answer.endswith('.'):
                correct_answer = correct_answer[:-1]

            # Resaltar las diferencias entre la respuesta del usuario y la traducción correcta
            highlighted_diff = highlight_differences(
                respuesta_alumno, correct_answer)

            # Crear el mensaje para obtener el score
            messages_score = [
                {"role": "system", "content": "You are an English tutor that evaluates translations and assigns a score from 1 to 10."},
                {"role": "user", "content": f"Evaluate the following translation:\n\n"
                 f"Original sentence in Spanish: {oracion_generada}\n"
                 f"Student's translation: {respuesta_alumno}\n\n"
                 f"Provide only a numeric score from 1 to 10, without any explanation or additional text."}
            ]

            # Llamada a OpenAI para obtener el score
            completion_score = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages_score,
                max_tokens=10  # Limitar los tokens para obtener solo el score
            )

            # Extraer el score de la respuesta
            score = completion_score.choices[0].message.content.strip()

            # Crear el mensaje para obtener feedback constructivo
            messages_feedback = [
                {"role": "system",
                    "content": "You are an encouraging and constructive English tutor."},
                {"role": "user", "content": f"Provide brief constructive feedback with a recommendation and words of encouragement based on the following:\n\n"
                 f"Original sentence in Spanish: {oracion_generada}\n"
                 f"Student's translation: {respuesta_alumno}\n\n"
                 f"Correct translation: {correct_answer}"}
            ]

            # Llamada a OpenAI para obtener el feedback constructivo
            completion_feedback = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages_feedback,
                max_tokens=100  # Limitar los tokens para el feedback breve
            )

            # Extraer el feedback constructivo
            feedback = completion_feedback.choices[0].message.content.strip()

            # Retornar las diferencias resaltadas, el score y el feedback
            return Response({
                'highlighted_diff': highlighted_diff,
                'score': score,
                'feedback': feedback
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Función para resaltar diferencias
def highlight_differences(user_answer, correct_answer):
    # Utiliza difflib.ndiff para calcular las diferencias entre ambas respuestas
    diff = list(ndiff(user_answer.split(), correct_answer.split()))
    diff_html = []

    for part in diff:
        if part.startswith('-'):
            # Palabra incorrecta en la respuesta del usuario (rojo y tachado)
            diff_html.append(
                f'<span style="color: red; text-decoration: line-through;">{part[2:]}</span>')
        elif part.startswith('+'):
            # Palabra correcta sugerida por el tutor (verde y negrita)
            diff_html.append(
                f'<span style="color: green; font-weight: bold;">{part[2:]}</span>')
        else:
            # Palabras que coinciden entre ambas respuestas
            diff_html.append(part[2:])

    # Unir las palabras con un espacio entre ellas
    return format_html(' '.join(diff_html))


@api_view(['POST'])
def check_answer(request):
    try:
        # Obtener los datos enviados en la solicitud
        sentence = request.data.get('sentence')
        user_answer = request.data.get('user_answer')
        language = request.data.get('language', 'en').lower()
        print(language)

        if not sentence or not user_answer or not language:
            return JsonResponse({
                'success': False,
                'message': 'Missing required fields'
            }, status=400)

        # Construir el prompt para OpenAI para obtener solo la traducción correcta
        prompt_translation = (
            f"Translate the following sentence from Spanish to {language}:\n\n"
            f"Sentence: {sentence}\n\n"
            f"Provide only the translation. Do not include any explanations, comments, or extra text. "
            f"Return only the translated sentence."
        )

        # Crear el mensaje para el modelo de OpenAI
        messages_translation = [
            {"role": "system", "content": "You are a helpful language tutor that provides only direct translations."},
            {"role": "user", "content": prompt_translation}
        ]

        # Llamada a OpenAI para obtener solo la traducción
        completion_translation = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages_translation,
            max_tokens=50  # Limitar los tokens para la traducción
        )

        # Extraer la traducción correcta generada por OpenAI
        correct_answer = completion_translation.choices[0].message.content.strip(
        )

        # Construir el prompt para obtener el feedback sobre la traducción del estudiante
        prompt_feedback = (
            f"You are a language tutor. The student has translated the following sentence:\n\n"
            f"Original sentence: {sentence}\n"
            f"Student's translation: {user_answer}\n\n"
            f"Please provide a concise feedback on the accuracy, corrections if needed, and a score from 1 to 10. "
            f"The feedback should be in {
                language} and must not exceed 150 words."
        )

        messages_feedback = [
            {"role": "system", "content": "You are a helpful language tutor providing brief and clear feedback."},
            {"role": "user", "content": prompt_feedback}
        ]

        # Llamada a OpenAI para generar el feedback
        completion_feedback = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages_feedback,
            max_tokens=150  # Limitar los tokens para el feedback
        )

        # Obtener el feedback generado por OpenAI
        feedback = completion_feedback.choices[0].message.content.strip()

        # Resaltar las diferencias entre la respuesta del usuario y la correcta
        highlighted_diff = highlight_differences(user_answer, correct_answer)

        return JsonResponse({
            'success': True,
            'correct_answer': correct_answer,  # La traducción correcta
            'feedback': feedback,
            'highlighted_diff': highlighted_diff  # Devolver la diferencia resaltada
        }, status=200)

    except openai.error.OpenAIError as e:
        logger.error(f"OpenAI API error: {e}")
        return JsonResponse({'success': False, 'message': f"OpenAI API error: {str(e)}"}, status=500)

    except Exception as e:
        # Captura cualquier otro error y registra el traceback
        logger.error(f"Server error: {str(e)}")
        return JsonResponse({'success': False, 'message': 'An unknown error occurred'}, status=500)


class TitleDetailView(generics.RetrieveAPIView):
    queryset = TableForm03.objects.all()
    serializer_class = TableForm03Serializer


class TableForm03ListView(generics.ListAPIView):
    serializer_class = TableForm03Serializer

    def get_queryset(self):
        queryset = TableForm03.objects.all()

        # Obtener los parámetros de la solicitud
        search_query = self.request.query_params.get('search', None)
        language_filter = self.request.query_params.get('language', None)
        level_cefr_filter = self.request.query_params.get('level_cefr', None)

        # Imprimir los valores para ver qué está recibiendo el backend
        print(f"Search query: {search_query}, Language: {
              language_filter}, CEFR Level: {level_cefr_filter}")

        # Filtro de búsqueda por Title_Name, Description, Topic_Father o Topic_Son
        if search_query:
            queryset = queryset.filter(
                Q(Title_Name__icontains=search_query) |
                Q(Description__icontains=search_query) |
                Q(Topic_Father__icontains=search_query) |
                Q(Topic_Son__icontains=search_query)
            )

        # Filtro por Language
        if language_filter:
            queryset = queryset.filter(Language__icontains=language_filter)

        # Filtro por CEFR Level
        if level_cefr_filter:
            queryset = queryset.filter(Level_CEFR__icontains=level_cefr_filter)

        return queryset

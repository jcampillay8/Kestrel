from rest_framework import generics
from .models import TopicFather, TableForm03, SpanishSentence, EnglishSentence
from .serializers import TopicFatherSerializer, TableForm03Serializer
from django.http import JsonResponse
from spellchecker import SpellChecker
from rest_framework.decorators import api_view
from openai import OpenAI
import os
import environ
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
User = get_user_model()  # Esto asegurará que obtienes el modelo de usuario correcto


# Configura tu cliente OpenAI
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

class CreateTableForm03View(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TableForm03Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(id_FK=request.user)  # Asigna el usuario actual al id_FK
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Nueva vista para guardar las oraciones
@api_view(['POST'])
def save_sentences(request):
    try:
        data = request.data
        
        # Utiliza un usuario predeterminado si no se pasa el usuario autenticado
        user = request.user if request.user.is_authenticated else User.objects.get(id=1)

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
    skip_spell_check = request.GET.get('skip_spell_check', 'false').lower() == 'true'

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
            {"role": "system", "content": f"You are a tutor creating sentences in {language}."},
            {"role": "user", "content": f"Create {num_sentences} sentences based on the following topics: {prompt}. Provide the sentences only in {language}."}
        ]

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=num_tokens
        )

        suggestions = completion.choices[0].message.content
        sentences = [line.strip() for line in suggestions.split("\n") if line.strip()]

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
        print(f"Language received: {language}")  # Para depurar y verificar el valor recibido

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


    

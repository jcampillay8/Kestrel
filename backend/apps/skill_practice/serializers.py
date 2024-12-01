from rest_framework import serializers
from apps.skill_builder.models import TableForm03, SpanishSentence, EnglishSentence
from apps.skill_practice.models import Nivel, Tema


class NivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = '__all__'


class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = '__all__'


class SpanishSentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpanishSentence
        fields = ['Sentence', 'rating_sentence', 'number_votes_sentence']


class EnglishSentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishSentence
        fields = ['Sentence', 'rating_sentence', 'number_votes_sentence']


class TableForm03Serializer(serializers.ModelSerializer):
    spanish_sentences = serializers.SerializerMethodField()
    english_sentences = serializers.SerializerMethodField()

    class Meta:
        model = TableForm03
        fields = [
            'id', 'Title_Name', 'Language', 'Topic_Father', 'Topic_Son',
            'Description', 'Level_CEFR', 'spanish_sentences', 'english_sentences'
        ]

    # Mostrar solo las oraciones en español si el lenguaje es español
    def get_spanish_sentences(self, obj):
        if obj.Language.lower() == 'spanish':
            return SpanishSentenceSerializer(obj.spanish_sentences.all(), many=True).data
        return []

    # Mostrar solo las oraciones en inglés si el lenguaje es inglés
    def get_english_sentences(self, obj):
        if obj.Language.lower() == 'english':
            return EnglishSentenceSerializer(obj.english_sentences.all(), many=True).data
        return []

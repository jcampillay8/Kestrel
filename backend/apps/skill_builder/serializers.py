from rest_framework import serializers
from .models import TableForm03, TopicFather, SpanishSentence, EnglishSentence, TablaMaestra


class TablaMaestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablaMaestra
        fields = ['id', 'verb_tense', 'grammatical_category',
                  'related_subtopic', 'order']


class TopicFatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicFather
        fields = ['id', 'topic_father']


class SpanishSentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpanishSentence
        fields = ['id', 'id_FK', 'rating_sentence',
                  'number_votes_sentence', 'Sentence']


class EnglishSentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishSentence
        fields = ['id', 'id_FK', 'rating_sentence',
                  'number_votes_sentence', 'Sentence']


class TableForm03Serializer(serializers.ModelSerializer):
    spanish_sentences = SpanishSentenceSerializer(many=True, write_only=True)
    english_sentences = EnglishSentenceSerializer(many=True, write_only=True)

    class Meta:
        model = TableForm03
        fields = [
            'id', 'id_FK', 'Title_Name', 'Language', 'Topic_Father', 'Topic_Son',
            'Description', 'Level_CEFR', 'number_setence', 'rating', 'number_votes',
            'spanish_sentences', 'english_sentences'
        ]

    def create(self, validated_data):
        spanish_sentences_data = validated_data.pop('spanish_sentences')
        english_sentences_data = validated_data.pop('english_sentences')
        table_form_03 = TableForm03.objects.create(**validated_data)

        for spanish_sentence_data in spanish_sentences_data:
            SpanishSentence.objects.create(
                id_FK=table_form_03, **spanish_sentence_data)

        for english_sentence_data in english_sentences_data:
            EnglishSentence.objects.create(
                id_FK=table_form_03, **english_sentence_data)

        return table_form_03

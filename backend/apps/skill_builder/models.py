from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class StudentPerformance(models.Model):
    id = models.AutoField(primary_key=True)
    id_fk_tabla_maestra = models.ForeignKey(
        'TablaMaestra',
        on_delete=models.CASCADE,
        related_name='student_performances',
        verbose_name="Referencia a TablaMaestra"
    )
    id_fk_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='student_performances',
        verbose_name="Referencia a Usuario",
        null=True,  # Permitir valores nulos
        blank=True  # Permitir que el formulario lo deje vacío
    )
    id_fk_topic_father = models.ForeignKey(
        'TopicFather',
        on_delete=models.CASCADE,
        related_name='student_performances',
        verbose_name="Referencia a TopicFather"
    )
    oracion_generada = models.TextField(
        verbose_name="Oración Generada", blank=True, null=True
    )
    score = models.IntegerField(verbose_name="Puntaje", blank=True, null=True)
    note = models.TextField(verbose_name="Nota", blank=True, null=True)
    key_areas = models.TextField(
        verbose_name="Áreas Clave", blank=True, null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Actualización")


class TablaMaestra(models.Model):
    verb_tense = models.CharField(max_length=50, verbose_name="Tiempo Verbal")
    grammatical_category = models.CharField(
        max_length=50, verbose_name="Categoría Gramatical")
    related_subtopic = models.CharField(
        max_length=50, verbose_name="Submateria Relacionada")
    order = models.IntegerField(verbose_name="Orden")

    def save(self, *args, **kwargs):
        # Normalizar datos antes de guardar
        self.verb_tense = self.verb_tense.strip().capitalize()
        self.grammatical_category = self.grammatical_category.strip().capitalize()
        self.related_subtopic = self.related_subtopic.strip().capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.verb_tense} - {self.grammatical_category} - {self.related_subtopic}"


class TopicFather(models.Model):
    id = models.AutoField(primary_key=True)
    topic_father = models.CharField(max_length=255)
    topic_father_en = models.CharField(
        max_length=255, blank=True, null=True)  # Inglés
    topic_father_fr = models.CharField(
        max_length=255, blank=True, null=True)  # Francés
    topic_father_de = models.CharField(
        max_length=255, blank=True, null=True)  # Alemán
    topic_father_pt = models.CharField(
        max_length=255, blank=True, null=True)  # Portugués

    def save(self, *args, **kwargs):
        self.topic_father = self.topic_father.strip().lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.topic_father


class TableForm03(models.Model):
    id_FK = models.ForeignKey(User, on_delete=models.CASCADE)
    Title_Name = models.CharField(max_length=50)
    Language = models.CharField(max_length=50)
    Topic_Father = models.CharField(max_length=50)
    Topic_Son = models.TextField()
    Description = models.CharField(max_length=255)
    Level_CEFR = models.CharField(max_length=2)
    number_setence = models.IntegerField()
    rating = models.FloatField(null=True, blank=True)
    number_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.Title_Name


class SpanishSentence(models.Model):
    id_FK = models.ForeignKey(
        TableForm03, on_delete=models.CASCADE, related_name='spanish_sentences')
    rating_sentence = models.FloatField(null=True, blank=True)
    number_votes_sentence = models.IntegerField(default=0)
    Sentence = models.CharField(max_length=100)

    def __str__(self):
        return self.Sentence


class EnglishSentence(models.Model):
    id_FK = models.ForeignKey(
        TableForm03, on_delete=models.CASCADE, related_name='english_sentences')
    rating_sentence = models.FloatField(null=True, blank=True)
    number_votes_sentence = models.IntegerField(default=0)
    Sentence = models.CharField(max_length=100)

    def __str__(self):
        return self.Sentence


class LanguageWord(models.Model):
    language = models.CharField(max_length=50)
    alphabet = models.CharField(max_length=5)
    alphabet2 = models.CharField(max_length=5)
    word = models.TextField()  # Para almacenar una lista de palabras como texto
    counter = models.IntegerField(default=0)  # Contador de palabras

    def save(self, *args, **kwargs):
        # Actualiza el contador de palabras cada vez que se guarda el modelo
        self.counter = len(self.word.split(','))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.language} - {self.alphabet} - {self.alphabet2}"

from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class TopicFather(models.Model):
    id = models.AutoField(primary_key=True)
    topic_father = models.CharField(max_length=255)
    topic_father_en = models.CharField(max_length=255, blank=True, null=True)  # Inglés
    topic_father_fr = models.CharField(max_length=255, blank=True, null=True)  # Francés
    topic_father_de = models.CharField(max_length=255, blank=True, null=True)  # Alemán
    topic_father_pt = models.CharField(max_length=255, blank=True, null=True)  # Portugués

    def save(self, *args, **kwargs):
        self.topic_father = self.topic_father.strip().lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.topic_father



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

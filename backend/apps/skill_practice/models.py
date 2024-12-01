from django.db import models


class Nivel(models.Model):
    nombre = models.CharField(max_length=50, unique=True)


class OpcionNivel(models.Model):
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)


class Tema(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

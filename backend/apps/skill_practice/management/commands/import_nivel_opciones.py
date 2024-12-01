import csv
from django.core.management.base import BaseCommand
from apps.skill_practice.models import Nivel, OpcionNivel


class Command(BaseCommand):
    help = 'Import levels and options from nivel_opciones.csv into the database'

    def handle(self, *args, **kwargs):
        # Ruta del archivo CSV
        csv_file_path = 'apps/nivel_opciones.csv'

        # Abrir el archivo CSV
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Saltar el encabezado

            # Iterar sobre las filas del CSV e insertar en la base de datos
            for row in reader:
                nivel_name = row[0].strip()  # Columna de nivel
                opcion_text = row[1].strip()  # Columna de opción

                # Obtener o crear el nivel
                nivel, created_nivel = Nivel.objects.get_or_create(
                    nombre=nivel_name)

                # Crear o actualizar las opciones de nivel
                opcion, created_opcion = OpcionNivel.objects.get_or_create(
                    nivel=nivel,
                    texto=opcion_text
                )

                # Mensajes de éxito
                if created_nivel:
                    self.stdout.write(self.style.SUCCESS(
                        f'Added Nivel: {nivel_name}'))
                if created_opcion:
                    self.stdout.write(self.style.SUCCESS(
                        f'Added Opcion: {opcion_text}'))
                else:
                    self.stdout.write(self.style.WARNING(
                        f'Opcion already exists: {opcion_text}'))

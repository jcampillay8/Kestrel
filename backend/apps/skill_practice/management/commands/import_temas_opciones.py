import csv
from django.core.management.base import BaseCommand
from apps.skill_practice.models import Tema


class Command(BaseCommand):
    help = 'Import topics from temas_opciones.csv into the database'

    def handle(self, *args, **kwargs):
        # Ruta del archivo CSV
        csv_file_path = 'apps/temas_opciones.csv'

        # Abrir el archivo CSV
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Saltar el encabezado

            # Iterar sobre las filas del CSV e insertar en la base de datos
            for row in reader:
                tema_name = row[0].strip()  # Columna del tema

                # Obtener o crear el tema
                tema, created = Tema.objects.get_or_create(nombre=tema_name)

                # Mensaje para indicar si se ha creado o actualizado el registro
                if created:
                    self.stdout.write(self.style.SUCCESS(
                        f'Added Tema: {tema_name}'))
                else:
                    self.stdout.write(self.style.WARNING(
                        f'Tema already exists: {tema_name}'))

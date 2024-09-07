import csv
from django.core.management.base import BaseCommand
from apps.skill_builder.models import TopicFather

class Command(BaseCommand):
    help = 'Import topics from topics_father.csv into the database'

    def handle(self, *args, **kwargs):
        # Ruta del archivo CSV
        csv_file_path = 'apps/topics_father.csv'

        # Abrir el archivo CSV
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Saltar el encabezado, si existe

            # Iterar sobre las filas del CSV e insertar en la base de datos
            for row in reader:
                topic_father_name = row[0].strip().lower()  # Columna para el nombre en español
                topic_father_en = row[2].strip().lower()  # Columna para el nombre en inglés
                topic_father_fr = row[3].strip().lower()  # Columna para el nombre en francés
                topic_father_de = row[4].strip().lower()  # Columna para el nombre en alemán
                topic_father_pt = row[5].strip().lower()  # Columna para el nombre en portugués

                # Crear o actualizar registros en la base de datos
                topic_father, created = TopicFather.objects.get_or_create(
                    topic_father=topic_father_name,
                    defaults={
                        'topic_father_en': topic_father_en,
                        'topic_father_fr': topic_father_fr,
                        'topic_father_de': topic_father_de,
                        'topic_father_pt': topic_father_pt
                    }
                )

                if not created:
                    # Actualiza los valores de las columnas de idioma si ya existe el registro
                    topic_father.topic_father_en = topic_father_en
                    topic_father.topic_father_fr = topic_father_fr
                    topic_father.topic_father_de = topic_father_de
                    topic_father.topic_father_pt = topic_father_pt
                    topic_father.save()

                # Mensaje para indicar si se ha creado o actualizado el registro
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Added: {topic_father_name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Updated: {topic_father_name}'))

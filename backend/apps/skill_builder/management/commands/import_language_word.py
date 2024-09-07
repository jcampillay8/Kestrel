import csv
from django.core.management.base import BaseCommand
from apps.skill_builder.models import LanguageWord  # Asegúrate de usar la ruta correcta al modelo

class Command(BaseCommand):
    help = 'Import language data from CSV into the database'

    def handle(self, *args, **kwargs):
        # Ruta del archivo CSV
        csv_file_path = 'apps/Language_Alphabets_Words_Extended.csv'  # Asegúrate que la ruta es accesible desde manage.py

        # Abrir el archivo CSV
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Crear o actualizar registros en la base de datos
                language_word, created = LanguageWord.objects.update_or_create(
                    language=row['Language'],
                    alphabet=row['Alphabet'],
                    alphabet2=row['Alphabet2'],
                    defaults={'word': row['Word']}
                )

                # Mensaje para indicar si se ha creado o actualizado el registro
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Added: {language_word}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Updated: {language_word}'))

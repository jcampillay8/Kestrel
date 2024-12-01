import csv
from django.core.management.base import BaseCommand
from apps.skill_builder.models import TablaMaestra


class Command(BaseCommand):
    help = 'Import data from tabla_maestra.csv into the database'

    def handle(self, *args, **kwargs):
        # Ruta del archivo CSV
        csv_file_path = 'apps/tabla_maestra.csv'

        # Abrir el archivo CSV
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Saltar el encabezado, si existe

            # Iterar sobre las filas del CSV e insertar en la base de datos
            for row in reader:
                verb_tense = row[1].strip()  # Columna Tiempo Verbal
                # Columna Categorías Gramaticales
                grammatical_category = row[2].strip()
                # Columna Submateria Relacionada
                related_subtopic = row[3].strip()
                order = int(row[4])  # Columna Orden

                # Crear o actualizar registros en la base de datos
                tabla_maestra, created = TablaMaestra.objects.get_or_create(
                    verb_tense=verb_tense,
                    grammatical_category=grammatical_category,
                    related_subtopic=related_subtopic,
                    defaults={'order': order}
                )

                if not created:
                    # Actualiza el orden si ya existe el registro
                    tabla_maestra.order = order
                    tabla_maestra.save()

                # Mensaje para indicar si se ha creado o actualizado el registro
                if created:
                    self.stdout.write(self.style.SUCCESS(
                        f'Added: {verb_tense} - {grammatical_category} - {related_subtopic}'))
                else:
                    self.stdout.write(self.style.WARNING(
                        f'Updated: {verb_tense} - {grammatical_category} - {related_subtopic}'))

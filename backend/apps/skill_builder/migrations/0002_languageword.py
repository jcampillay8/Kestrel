# Generated by Django 5.1 on 2024-09-06 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill_builder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('alphabet', models.CharField(max_length=5)),
                ('alphabet2', models.CharField(max_length=5)),
                ('word', models.TextField()),
                ('counter', models.IntegerField(default=0)),
            ],
        ),
    ]
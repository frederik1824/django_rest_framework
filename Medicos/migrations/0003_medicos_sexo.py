# Generated by Django 4.1.5 on 2023-02-09 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicos', '0002_medicos_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicos',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'MASCULINO'), ('F', 'FEMENINO')], max_length=10, null=True),
        ),
    ]
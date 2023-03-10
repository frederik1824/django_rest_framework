# Generated by Django 4.1.5 on 2023-02-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicos', '0005_remove_medicos_apellidos_remove_medicos_nombres_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicos',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='medicos',
            name='especialidad',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='medicos',
            name='facebook',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='medicos',
            name='instagram',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]

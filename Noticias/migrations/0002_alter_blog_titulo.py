# Generated by Django 4.1.5 on 2023-02-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]

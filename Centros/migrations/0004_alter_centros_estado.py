# Generated by Django 4.1.5 on 2023-02-09 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Centros', '0003_remove_centros_provincia_delete_provincia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centros',
            name='estado',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]

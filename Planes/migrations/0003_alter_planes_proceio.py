# Generated by Django 4.1.5 on 2023-02-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Planes', '0002_alter_planes_proceio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planes',
            name='proceio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
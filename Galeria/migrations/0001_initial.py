# Generated by Django 4.1.5 on 2023-01-05 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(upload_to='galeria/imagen')),
                ('date_joind', models.DateTimeField(auto_now_add=True)),
                ('last_joind', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

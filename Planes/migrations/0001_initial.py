# Generated by Django 4.1.5 on 2023-01-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('proceio', models.DecimalField(decimal_places=0, max_digits=8)),
                ('description', models.TextField()),
            ],
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-17 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vio', '0007_weatherdata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WeatherData',
        ),
    ]
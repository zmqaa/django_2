# Generated by Django 5.1.4 on 2024-12-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vio', '0012_tag_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafile',
            name='row_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

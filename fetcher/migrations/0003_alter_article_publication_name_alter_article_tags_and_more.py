# Generated by Django 4.0.3 on 2022-04-09 11:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetcher', '0002_rename_podcast_name_bloglink_publication_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publication_name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=None),
        ),
        migrations.AlterField(
            model_name='episode',
            name='publication_name',
            field=models.CharField(max_length=256),
        ),
    ]

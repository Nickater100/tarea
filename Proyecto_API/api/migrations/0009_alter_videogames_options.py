# Generated by Django 4.1 on 2022-08-28 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_videogames_created_videogames_modified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videogames',
            options={'ordering': ['name', 'published_year']},
        ),
    ]

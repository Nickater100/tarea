# Generated by Django 4.1 on 2022-08-28 22:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_videogames_options_videogames_genres_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogames',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videogames',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

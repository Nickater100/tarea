# Generated by Django 4.1 on 2022-08-28 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogames',
            name='name',
            field=models.CharField(default='HogwartsLegacy', max_length=100),
        ),
    ]

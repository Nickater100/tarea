# Generated by Django 4.1 on 2022-08-28 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_genres_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genres',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]

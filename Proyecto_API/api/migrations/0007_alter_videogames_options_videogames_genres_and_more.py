# Generated by Django 4.1 on 2022-08-28 22:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_videogames_modified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videogames',
            options={'ordering': ('name', 'published_year')},
        ),
        migrations.AddField(
            model_name='videogames',
            name='genres',
            field=models.ManyToManyField(to='api.genres'),
        ),
        migrations.AddField(
            model_name='videogames',
            name='name',
            field=models.CharField(default='HogwartsLegacy', max_length=100),
        ),
        migrations.AddField(
            model_name='videogames',
            name='platform',
            field=models.ManyToManyField(to='api.platform'),
        ),
        migrations.AddField(
            model_name='videogames',
            name='published_year',
            field=models.PositiveIntegerField(default=1997),
        ),
        migrations.AddField(
            model_name='videogames',
            name='publisher',
            field=models.OneToOneField(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='api.publisher'),
            preserve_default=False,
        ),
    ]

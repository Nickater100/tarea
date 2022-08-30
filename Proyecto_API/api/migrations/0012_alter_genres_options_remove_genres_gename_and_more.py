# Generated by Django 4.1 on 2022-08-28 23:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_genres_options_rename_name_genres_gename'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genres',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='genres',
            name='geName',
        ),
        migrations.AddField(
            model_name='genres',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='platform',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='trade_name',
            field=models.CharField(max_length=30),
        ),
    ]

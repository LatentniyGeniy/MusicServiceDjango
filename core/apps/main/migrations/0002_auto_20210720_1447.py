# Generated by Django 3.2.5 on 2021-07-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ManyToManyField(to='main.Genre'),
        ),
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.ManyToManyField(to='main.Genre'),
        ),
    ]
# Generated by Django 3.2.5 on 2021-08-17 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='song',
            field=models.ManyToManyField(related_name='song_playlist', to='main.Song'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_playlist', to=settings.AUTH_USER_MODEL),
        ),
    ]

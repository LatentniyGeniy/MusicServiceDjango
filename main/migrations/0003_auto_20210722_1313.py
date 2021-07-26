# Generated by Django 3.2.5 on 2021-07-22 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210720_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ManyToManyField(related_name='albums', to='main.Artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='picture_link',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='artist',
            name='picture_link',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='artist',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='main.album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='file_link',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
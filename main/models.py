from django.db import models
from main.choices import RELEASE_TYPE_CHOICES, ALBUM


class Genre(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Artist(models.Model):
    title = models.CharField(max_length=255, unique=True)
    picture_link = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre)


class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ManyToManyField(Artist, related_name='albums')
    release_date = models.DateField()
    release_type = models.CharField(
        max_length=10,
        choices=RELEASE_TYPE_CHOICES,
        default=ALBUM
    )
    genre = models.ManyToManyField(Genre)
    picture_link = models.CharField(max_length=255)


class Song(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    genre = models.ManyToManyField(Genre)
    file_link = models.CharField(max_length=255)


class User(models.Model):
    name = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date_of_birth = models.DateField()


class Playlist(models.Model):
    title = models.CharField(max_length=255)
    song = models.ManyToManyField(Song)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

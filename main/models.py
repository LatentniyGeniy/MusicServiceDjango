from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Artist(models.Model):
    title = models.CharField(max_length=150)
    picture_link = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre)


class Album(models.Model):
    title = models.CharField(max_length=150)
    release_date = models.DateField()

    ALBUM = 'Album'
    SINGLE = 'Single'
    EP = 'EP'
    RELEASE_TYPE_CHOICES = [
        (ALBUM, 'Album'),
        (SINGLE, 'Single'),
        (EP, 'EP'),
    ]
    release_type = models.CharField(
        max_length=10,
        choices=RELEASE_TYPE_CHOICES,
        default=ALBUM
    )
    genre = models.ManyToManyField(Genre)
    picture_link = models.CharField(max_length=200)


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    file_link = models.CharField(max_length=200)


class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date_of_birth = models.DateField()


class Playlist(models.Model):
    title = models.CharField(max_length=100)
    song = models.ManyToManyField(Song)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

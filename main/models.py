from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=50)


class Artist(models.Model):
    title = models.CharField(max_length=150)
    picture_link = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre)


class Album(models.Model):
    title = models.CharField(max_length=150)
    release_date = models.DateField()
    release_type = models.CharField(max_length=50) #или сделать справочник с типами релизов(EP, сингл, альбом)
    picture_link = models.CharField(max_length=200)


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    authors = models.CharField(max_length=150)
    producers = models.CharField(max_length=100)
    source = models.CharField(max_length=100) #типа под каким лейблом сделано (так было в спотифай)
    file_link = models.CharField(max_length=200)


class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=50)


class Playlist(models.Model):
    title = models.CharField(max_length=100)
    song = models.ManyToManyField(Song)
    user = models.CharField(User)
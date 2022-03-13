from django.contrib import admin
from django.contrib.auth import get_user_model

from core.apps.main.models import Album, Artist, Genre, Song, Playlist, Like

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(get_user_model())
admin.site.register(Playlist)
admin.site.register(Like)

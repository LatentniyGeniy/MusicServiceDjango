from django.contrib import admin
from main.models import Album, Artist, Genre, Song, User


admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(User)

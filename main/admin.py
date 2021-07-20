from django.contrib import admin
from main.models import Album, Artist, Genre, Song


registered_models = {Album, Artist, Genre, Song}
admin.site.register(registered_models)

from rest_framework import serializers

from main.models import Album, Genre, Artist, Song


class AlbumDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ("title", "release_date", "release_type")


class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"

from rest_framework import serializers

from core.apps.main.models import Album, Genre, Artist, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("title",)


class AlbumDetailSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ("id", "title", "release_date", "artist", "genre", "release_type", "picture_link", 'songs')


class AlbumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ("id", "title", "release_date", "release_type")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "title")


class ArtistDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ("id", "title", "genre", "picture_link")


class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("id", "title", "genre")


class SongListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("id", "title")


class SongDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("id", "title", "album", "genre", "file_link")

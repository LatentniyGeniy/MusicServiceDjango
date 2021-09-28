from rest_framework import serializers

from core.apps.main.models import Album, Genre, Artist, Song, Playlist


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("title",)


class AlbumDetailSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ("id", "title", "release_date", "artist", "genre", "release_type", "picture_link", 'songs', 'is_fan')


class AlbumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ("id", "title", "release_date", "release_type")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "title")


class ArtistDetailSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ("id", "title", "genre", "picture_link", 'is_fan')


class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("id", "title", "genre")


class SongListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("id", "title")


class SongDetailSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ("id", "title", "album", "genre", "file_link", 'is_fan')


class PlaylistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ("id", "title")


class PlaylistDetailSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Playlist
        fields = ("id", "title", "user", "song", 'is_fan')

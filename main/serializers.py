from rest_framework import serializers

from main.models import Album, Genre, Artist, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("title",)


class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"


class AlbumDetailSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ("title", "release_date", "release_type", "picture_link", 'songs')


class AlbumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ("title", "release_date", "release_type")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("title",)


class ArtistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class ArtistDetailSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ("title", "genre", "picture_link", 'songs')


class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("title", "genre")


class SongCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class SongListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("title", "artist")


class SongDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("title", "artist", "album", "genre", "file_link")

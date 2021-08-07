from rest_framework import serializers

from core.apps.main.models import Album, Genre, Artist, Song, User


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


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

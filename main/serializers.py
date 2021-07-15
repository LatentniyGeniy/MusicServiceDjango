from rest_framework import serializers

from .models import Album


class AlbumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ("title", "release_date", "release_type", "picture_link")




class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"
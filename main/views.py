from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from main.mixins import MultiSerializerViewSetMixin
from main.models import Album, Genre, Artist, Song
from main.serializers import (AlbumDetailSerializer,
                              AlbumListSerializer,
                              GenreSerializer,
                              ArtistDetailSerializer,
                              ArtistListSerializer,
                              SongDetailSerializer,
                              SongListSerializer)


class AlbumViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumDetailSerializer
    serializer_action_classes = {
        'list': AlbumListSerializer,
        'create': AlbumDetailSerializer,
    }


class GenreViewSet(ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ArtistViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistDetailSerializer
    serializer_action_classes = {
        'list': ArtistListSerializer,
        'create': ArtistDetailSerializer,
    }


class SongViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongDetailSerializer
    serializer_action_classes = {
        'list': SongListSerializer,
        'create': SongDetailSerializer,
    }

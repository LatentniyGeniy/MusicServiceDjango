from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet

from core.apps.main.mixins import MultiSerializerViewSetMixin
from core.apps.main.models import Album, Genre, Artist, Song, User
from core.apps.main.serializers import (
    AlbumDetailSerializer,
    AlbumListSerializer,
    GenreSerializer,
    ArtistDetailSerializer,
    ArtistListSerializer,
    SongDetailSerializer,
    SongListSerializer,
    RegistrationSerializer,
)


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


class RegistrationAPIView(GenericViewSet, ListModelMixin, CreateModelMixin):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

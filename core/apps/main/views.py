from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from core.apps.main.mixins import MultiSerializerViewSetMixin, PermissionByActionMixin
from core.apps.like.mixins import LikedMixin
from core.apps.main.models import Album, Genre, Artist, Song, Playlist
from core.apps.main.serializers import (
    AlbumDetailSerializer,
    AlbumListSerializer,
    GenreSerializer,
    ArtistDetailSerializer,
    ArtistListSerializer,
    SongDetailSerializer,
    SongListSerializer,
    PlaylistDetailSerializer,
    PlaylistListSerializer,
)


class AlbumViewSet(PermissionByActionMixin, MultiSerializerViewSetMixin, LikedMixin, ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumDetailSerializer
    serializer_action_classes = {
        'list': AlbumListSerializer,
        'create': AlbumDetailSerializer,
    }
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAuthenticated]}


class GenreViewSet(PermissionByActionMixin, GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAdminUser]}


class ArtistViewSet(PermissionByActionMixin, MultiSerializerViewSetMixin, LikedMixin, ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistDetailSerializer
    serializer_action_classes = {
        'list': ArtistListSerializer,
        'create': ArtistDetailSerializer,
    }
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAuthenticated]}


class SongViewSet(PermissionByActionMixin, MultiSerializerViewSetMixin, LikedMixin, ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongDetailSerializer
    serializer_action_classes = {
        'list': SongListSerializer,
        'create': SongDetailSerializer,
    }
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAuthenticated]}


class PlaylistViewSet(PermissionByActionMixin, MultiSerializerViewSetMixin, LikedMixin, ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistDetailSerializer
    serializer_action_classes = {
        'list': PlaylistListSerializer,
        'create': PlaylistDetailSerializer,
    }
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAuthenticated]}

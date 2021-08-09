from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
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
)


class AlbumViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumDetailSerializer
    serializer_action_classes = {
        'list': AlbumListSerializer,
        'create': AlbumDetailSerializer,
    }
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAuthenticated]}

    #слишком часто повторяется. Это же неправильно? как лучше исправить?
    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class GenreViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAdminUser]}

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class ArtistViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistDetailSerializer
    serializer_action_classes = {
        'list': ArtistListSerializer,
        'create': ArtistDetailSerializer,
    }
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAuthenticated]}

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class SongViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongDetailSerializer
    serializer_action_classes = {
        'list': SongListSerializer,
        'create': SongDetailSerializer,
    }
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAuthenticated]}

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

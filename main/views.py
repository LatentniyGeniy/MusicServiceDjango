from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin


from main.models import Album, Genre, Artist, Song
from main.serializers import AlbumDetailSerializer, AlbumCreateSerializer, GenreSerializer, ArtistDetailSerializer, SongDetailSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            serializer_class = AlbumCreateSerializer
        else:
            serializer_class = AlbumDetailSerializer
        return serializer_class


class GenreViewSet(ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistDetailSerializer


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongDetailSerializer

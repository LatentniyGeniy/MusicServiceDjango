from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin


from main.models import Album, Genre, Artist, Song
from main.serializers import AlbumDetailSerializer, AlbumCreateSerializer, GenreSerializer, ArtistSerializer, SongSerializer


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
    serializer_class = ArtistSerializer


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer








































# from django.shortcuts import render, redirect
#
# from .forms import AlbumForm
# from .models import Album
#
#
# def index(request):
#     albums = Album.objects.all()
#     return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'albums': albums})
#
#
# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = AlbumForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             error = 'Форма неверна'
#
#     form = AlbumForm()
#     context = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'main/create.html', context)
#
#
# def edit(request, id):
#     album = Album.objects.get(id=id)
#     return render(request, 'main/create.html', {'album': album})
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Album
from .serializers import AlbumListSerializer, AlbumCreateSerializer


class AlbumListView(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumListSerializer(albums, many=True)
        return Response(serializer.data)


class AlbumCreateView(APIView):
    def post(self, request):
        album = AlbumCreateSerializer(data=request.data)
        if album.is_valid():
            album.save()
        return Response(status=201)














































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
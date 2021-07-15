from django.urls import path
from . import views
urlpatterns = [
#    path('', views.index, name='home'),
#    path('craeate', views.create, name='create'),
    path('album/', views.AlbumListView.as_view()),
    path('create-album/', views.AlbumCreateView.as_view()),
]

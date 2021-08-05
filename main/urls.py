from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main import views


router = DefaultRouter()
router.register('albums', views.AlbumViewSet)
router.register('genres', views.GenreViewSet)
router.register('artists', views.ArtistViewSet)
router.register('songs', views.SongViewSet)
router.register('users', views.RegistrationAPIView)
router.register('login', views.LoginAPIView)
router.register('user', views.UserRetrieveUpdateAPIView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

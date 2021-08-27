import factory
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from factory import fuzzy

from core.apps.main.models import Genre, Artist, Album, Song, Playlist, Like


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.fuzzy.FuzzyText(length=10)
    email = factory.LazyAttribute(lambda a: '{}@example.com'.format(a.username).lower())
    password = factory.fuzzy.FuzzyText(length=15)

    class Meta:
        model = get_user_model()


class SuperUserFactory(UserFactory):
    is_superuser = True
    is_staff = True


class GenreFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=10)

    class Meta:
        model = Genre


class ArtistFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=10)
    picture_link = factory.LazyAttribute(lambda o: 'https://picture/%s' % o.title)
    genre = factory.RelatedFactory(GenreFactory)

    class Meta:
        model = Artist


class AlbumFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=12)
    artist = factory.RelatedFactory(ArtistFactory)
    release_date = factory.Faker('date_object')
    release_type = factory.fuzzy.FuzzyChoice(('Album', 'Single', 'EP'))
    genre = factory.RelatedFactory(GenreFactory)
    picture_link = factory.LazyAttribute(lambda o: 'https://picture/%s' % o.title)

    class Meta:
        model = Album


class SongFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=12, prefix='Song')
    album = factory.SubFactory(AlbumFactory)
    genre = factory.RelatedFactory(GenreFactory)
    file_link = factory.LazyAttribute(lambda o: 'https://file/%s' % o.title)

    class Meta:
        model = Song


class PlaylistFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=5, prefix='Playlist_')
    user = factory.SubFactory(UserFactory)
    song = factory.RelatedFactory(SongFactory)

    class Meta:
        model = Playlist


class LikeItemFactory(factory.django.DjangoModelFactory):
    object_id = factory.SelfAttribute('content_object.id')
    content_type = factory.LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.content_object))

    class Meta:
        exclude = ['content_object']
        abstract = True


class LikeFactory(LikeItemFactory):
    content_object = factory.SubFactory(UserFactory)

    class Meta:
        model = Like

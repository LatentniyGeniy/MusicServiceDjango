import datetime

from factory import fuzzy
from faker import Faker

import factory
from pytz import UTC

from core.apps.main.models import Genre, Artist, Album, Song, User


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


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.fuzzy.FuzzyText(length=10)
    email = factory.LazyAttribute(lambda a: '{}@example.com'.format(a.username).lower())

    is_active = True
    is_staff = False

    created_at = factory.fuzzy.FuzzyDateTime(datetime.datetime(2021, 12, 12, tzinfo=UTC),
                                             datetime.datetime(2021, 12, 12, tzinfo=UTC),
                                             force_day=3, force_second=42)
    updated_at = factory.fuzzy.FuzzyDateTime(datetime.datetime(2021, 1, 1, tzinfo=UTC),
                                             datetime.datetime(2021, 12, 12, tzinfo=UTC),
                                             force_day=3, force_second=42)

    class Meta:
        model = User

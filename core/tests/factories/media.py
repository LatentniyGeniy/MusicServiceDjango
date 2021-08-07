from factory import fuzzy

import factory


from core.apps.main import Genre, Artist, Album, Song


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
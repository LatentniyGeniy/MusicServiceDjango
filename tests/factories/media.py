from random import randint

import factory

from main.models import Genre


GENRES = [
    'Hip - Hop',
    'Reggae',
    'Pop',
    'Indie',
    'Rock',
    'Classic',
    'R & B',
    'Jazz',
]


class GenreFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: GENRES[n % len(GENRES)])

    class Meta:
        model = Genre

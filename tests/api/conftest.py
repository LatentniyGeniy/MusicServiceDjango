import pytest

from tests.factories.media import GenreFactory


@pytest.fixture
def genres(genres_qty):
    return GenreFactory.create_batch(size=genres_qty)


@pytest.fixture
def genre():
    return GenreFactory.create()

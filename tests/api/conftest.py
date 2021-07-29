import pytest

from tests.factories.media import GenreFactory, ArtistFactory, AlbumFactory, SongFactory


@pytest.fixture
def genres(genres_qty):
    return GenreFactory.create_batch(size=genres_qty)


@pytest.fixture
def genre():
    return GenreFactory.create()


@pytest.fixture
def artists(artists_qty):
    return ArtistFactory.create_batch(size=artists_qty)


@pytest.fixture
def albums(albums_qty):
    return AlbumFactory.create_batch(size=albums_qty)


@pytest.fixture
def songs(songs_qty):
    return SongFactory.create_batch(size=songs_qty)

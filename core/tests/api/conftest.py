import pytest

from rest_framework.test import APIClient

from core.tests.factories.media import (
    GenreFactory,
    ArtistFactory,
    AlbumFactory,
    SongFactory,
    UserFactory,
    SuperUserFactory,
    PlaylistFactory,
)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def genres(genres_qty):
    return GenreFactory.create_batch(size=genres_qty)


@pytest.fixture
def genre():
    return GenreFactory.create()


@pytest.fixture
def artist():
    return ArtistFactory.create()


@pytest.fixture
def artists(artists_qty):
    return ArtistFactory.create_batch(size=artists_qty)


@pytest.fixture
def album():
    return AlbumFactory.create()


@pytest.fixture
def albums(albums_qty):
    return AlbumFactory.create_batch(size=albums_qty)


@pytest.fixture
def song():
    return SongFactory.create()


@pytest.fixture
def songs(songs_qty):
    return SongFactory.create_batch(size=songs_qty)


@pytest.fixture
def user():
    return UserFactory.create()


@pytest.fixture
def users(users_qty):
    return UserFactory.create_batch(size=users_qty)


@pytest.fixture
def superuser():
    return SuperUserFactory.create()


@pytest.fixture
def playlist():
    return PlaylistFactory.create()


@pytest.fixture
def playlists(playlist_qty):
    return PlaylistFactory.create_batch(size=playlist_qty)

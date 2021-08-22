import json

import pytest

from rest_framework import status

from core.tests.utils import login_user


@pytest.mark.django_db
class TestAlbum:

    @pytest.mark.parametrize('albums_qty', [0, 3, 5])
    def test_list(self, client, albums, albums_qty):
        """
        test list of albums on getting right:
            * amount
        """
        res = client.get('/api/v1/albums/')

        assert res.status_code == status.HTTP_200_OK
        assert len(res.json()) == albums_qty

    @pytest.mark.parametrize('artists_qty, genres_qty', [(3, 3)])
    def test_create_album(self, api_client, artists, genres, genres_qty, artists_qty, user):
        title = 'Album'
        artist = [artist.id for artist in artists]
        release_date = "2021-07-30"
        release_type = 'Single'
        genre = [genre.id for genre in genres]
        picture_link = 'https://file/tyjtyjty.png'

        data = json.dumps({
            'title': title,
            'artist': artist,
            "release_date": release_date,
            'release_type': release_type,
            'genre': genre,
            'picture_link': picture_link,
        })

        login_user(api_client, user)
        res = api_client.post(f'/api/v1/albums/', data=data, content_type='application/json')
        response_data = res.json()

        assert res.status_code == status.HTTP_201_CREATED
        assert response_data['title'] == title
        assert len(response_data['artist']) == len(artist)
        assert response_data['release_date'] == release_date
        assert response_data['release_type'] == release_type
        assert len(response_data['genre']) == len(genre)
        assert response_data['picture_link'] == picture_link

    def test_update_album(self, api_client, album, user):
        title = 'Edited Album'
        picture_link = 'https://file/rtyrtyry.png'
        release_type = 'Single'
        release_date = "2021-08-12"

        data = json.dumps({
            'title': title,
            'picture_link': picture_link,
            'release_type': release_type,
            "release_date": release_date,
        })

        login_user(api_client, user)
        res = api_client.patch(f'/api/v1/albums/{album.id}/', data=data, content_type='application/json')
        response_data = res.json()

        assert res.status_code == status.HTTP_200_OK
        assert response_data['title'] == title
        assert response_data['picture_link'] == picture_link
        assert response_data['release_type'] == release_type
        assert response_data['release_date'] == release_date

    def test_detail(self, client, album):
        res = client.get(f'/api/v1/albums/{album.id}/')
        response_data = res.json()

        assert res.status_code == status.HTTP_200_OK
        assert response_data['title'] == album.title
        assert response_data['picture_link'] == album.picture_link
        assert response_data['release_type'] == album.release_type
        assert response_data['release_date'] == album.release_date.strftime('%Y-%m-%d')
        assert len(response_data['artist']) == album.artist.count()
        assert len(response_data['genre']) == album.genre.count()

import json

import pytest

from rest_framework import status

from core.tests.utils import login_user


@pytest.mark.django_db
class TestSong:

    @pytest.mark.parametrize('songs_qty', [0, 1, 2])
    def test_list(self, client, songs, songs_qty):
        """
        test list of songs on getting right:
            * amount
        """
        res = client.get('/api/v1/songs/')

        assert res.status_code == status.HTTP_200_OK
        assert len(res.json()) == songs_qty

    @pytest.mark.parametrize('genres_qty', [3])
    def test_create_song(self, api_client, album, genres, genres_qty, user):
        title = 'Some title'
        genre = [genre.id for genre in genres]
        album_id = album.id
        file_link = 'https://file/asdasda.mp3'

        data = json.dumps({
            'title': title,
            'genre': genre,
            'album': album_id,
            'file_link': file_link,
        })

        login_user(api_client, user)
        res = api_client.post(f'/api/v1/songs/', data=data, content_type='application/json')
        response_data = res.json()

        assert res.status_code == status.HTTP_201_CREATED
        assert response_data['title'] == title
        assert len(response_data['genre']) == len(genre)
        assert response_data['album'] == album_id

    def test_update_song(self, api_client, song, user):
        title = 'Edited title'

        data = json.dumps({
            'title': title,
        })

        login_user(api_client, user)
        res = api_client.patch(f'/api/v1/songs/{song.id}/', data=data, content_type='application/json')
        response_data = res.json()

        assert res.status_code == status.HTTP_200_OK
        assert response_data['title'] == title

    def test_detail(self, client, song):
        res = client.get(f'/api/v1/songs/{song.id}/')
        response_data = res.json()

        assert res.status_code == status.HTTP_200_OK
        assert response_data['title'] == song.title
        assert response_data['album'] == song.album.id
        assert len(response_data['genre']) == song.genre.count()

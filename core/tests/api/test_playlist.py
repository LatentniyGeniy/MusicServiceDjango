import json

import pytest

from rest_framework import status

from core.tests.utils import login_user


@pytest.mark.django_db
class TestPlaylist:

    @pytest.mark.parametrize('playlist_qty', [0, 3, 5])
    def test_list(self, client, playlists, playlist_qty):
        """
        test list of playlist on getting right:
            * amount
        """
        res = client.get('/api/v1/playlists/')

        assert res.status_code == status.HTTP_200_OK
        assert len(res.json()) == playlist_qty

    @pytest.mark.parametrize('songs_qty', [3])
    def test_create_playlist(self, api_client, songs, songs_qty, user):
        title = 'Playlist'
        user_id = user.id
        song = [song.id for song in songs]

        data = json.dumps({
            'title': title,
            'user': user_id,
            "song": song,
        })

        login_user(api_client, user)
        res = api_client.post(f'/api/v1/playlists/', data=data, content_type='application/json')
        response_data = res.json()

        assert res.status_code == status.HTTP_201_CREATED
        assert response_data['title'] == title
        assert response_data['user'] == user_id
        assert len(response_data['song']) == len(song)

    @pytest.mark.parametrize('songs_qty', [3])
    def test_update_playlist(self, api_client, playlist, songs, songs_qty, user):
        title = 'Edited_Playlist'
        song = [song.id for song in songs]

        data = json.dumps({
            'title': title,
            'song': song,
        })

        login_user(api_client, user)
        res = api_client.patch(f'/api/v1/playlists/{playlist.id}/', data=data, content_type='application/json')
        response_data = res.json()

        assert res.status_code == status.HTTP_200_OK
        assert response_data['title'] == title
        assert len(response_data['song']) == len(song)

    def test_detail(self, client, playlist):
        res = client.get(f'/api/v1/playlists/{playlist.id}/')
        response_data = res.json()

        assert res.status_code == status.HTTP_200_OK
        assert response_data['title'] == playlist.title
        assert len(response_data['song']) == playlist.song.count()

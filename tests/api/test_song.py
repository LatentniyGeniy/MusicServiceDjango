import pytest

from rest_framework import status


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
    def test_create_song(self, client, album, genres, genres_qty):
        data = {
            'title': 'Some title',
            'genre': [genre.id for genre in genres],
            'album': album.id,
            'file_link': 'https://file/asdasda.mp3'
        }
        res = client.post(f'/api/v1/songs/', data=data, content_type='application/json')
        response_data = res.json()

        assert res.status_code == status.HTTP_201_CREATED
        assert response_data['title'] == data['title']
        assert len(response_data['genre']) == len(data['genre'])
        assert response_data['album'] == data['album']


# GET /api/v1/songs/ - GET LIST
# POST /api/v1/songs/ - CREATE NEW SONG
# GET /api/v1/songs/<song_id>/ - GET DETAIL SONG <SONG_ID>
# PATCH/PUT /api/v1/songs/<song_id>/ - UPDATE SONG <SONG_ID>

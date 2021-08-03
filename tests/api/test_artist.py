import pytest

from rest_framework import status


@pytest.mark.django_db
class TestArtists:

    @pytest.mark.parametrize('artists_qty', [0, 3, 5, 7])
    def test_list(self, client, artists, artists_qty):
        """
        test list of artists on getting right:
            * amount
        """
        res = client.get('/api/v1/artists/')

        assert res.status_code == status.HTTP_200_OK
        assert len(res.json()) == artists_qty

    @pytest.mark.parametrize('genres_qty', [3])
    def test_create_artist(self, client, genres, genres_qty):
        data = {
            'title': 'Artist',
            'picture_link': 'https://file/adrthy.png',
            'genre': [genre.id for genre in genres],
        }
        res = client.post(f'/api/v1/artists/', data=data, content_type='application/json')
        response_data = res.json()

        assert res.status_code == status.HTTP_201_CREATED
        assert response_data['title'] == data['title']
        assert response_data['picture_link'] == data['picture_link']
        assert len(response_data['genre']) == len(data['genre'])

    def test_update_artist(self, client, artist):
        data = {
            'title': 'Edited Artist',
            'picture_link': 'https://file/rtyrtyry.png',
        }
        res = client.patch(f'/api/v1/artists/{artist.id}/', data=data, content_type='application/json')
        response_data = res.json()

        assert res.status_code == status.HTTP_200_OK
        assert response_data['title'] == data['title']
        assert response_data['picture_link'] == data['picture_link']

    def test_detail(self, client, artist):
        res = client.get(f'/api/v1/artists/{artist.id}/')
        response_data = res.json()

        assert res.status_code == status.HTTP_200_OK
        assert response_data['title'] == artist.title
        assert response_data['picture_link'] == artist.picture_link
        assert len(response_data['genre']) == artist.genre.count()

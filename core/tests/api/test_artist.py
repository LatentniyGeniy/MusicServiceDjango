import pytest
import json

from rest_framework import status

from core.tests.utils import login_user


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
    def test_create_artist(self, api_client, genres, genres_qty, user):
        title = 'Artist'
        picture_link = 'https://file/adrthy.png'
        genre = [genre.id for genre in genres]

        data = json.dumps({
            'title': title,
            'picture_link': picture_link,
            'genre': genre,
        })
        res = api_client.post(f'/api/v1/artists/', data=data, content_type='application/json')

        assert res.status_code == status.HTTP_401_UNAUTHORIZED

        login_user(api_client, user)
        res = api_client.post(f'/api/v1/artists/', data=data, content_type='application/json')
        response_data = res.json()

        assert res.status_code == status.HTTP_201_CREATED
        assert response_data['title'] == title
        assert response_data['picture_link'] == picture_link
        assert len(response_data['genre']) == len(genre)

    def test_update_artist(self, api_client, artist, user):
        title = 'Edited Artist'
        picture_link = 'https://file/rtyrtyry.png'
        data = json.dumps({
            'title': title,
            'picture_link': picture_link,
        })

        login_user(api_client, user)
        res = api_client.patch(f'/api/v1/artists/{artist.id}/', data=data, content_type='application/json')
        response_data = res.json()

        assert res.status_code == status.HTTP_200_OK
        assert response_data['title'] == title
        assert response_data['picture_link'] == picture_link

    def test_detail(self, client, artist):
        res = client.get(f'/api/v1/artists/{artist.id}/')
        response_data = res.json()

        assert res.status_code == status.HTTP_200_OK
        assert response_data['title'] == artist.title
        assert response_data['picture_link'] == artist.picture_link
        assert len(response_data['genre']) == artist.genre.count()

import pytest

from rest_framework import status

from core.tests.utils import login_user


@pytest.mark.django_db
class TestLike:

    def test_like_song(self, api_client, song, user):

        login_user(api_client, user)
        res = api_client.post(f'/api/v1/songs/{song.id}/like/')

        assert res.status_code == status.HTTP_200_OK

        res = api_client.post(f'/api/v1/songs/{song.id}/like/')

        assert res.status_code == status.HTTP_409_CONFLICT

    def test_unlike_song(self, api_client, song, user):

        login_user(api_client, user)

        res = api_client.post(f'/api/v1/songs/{song.id}/like/')

        assert res.status_code == status.HTTP_200_OK

        res = api_client.delete(f'/api/v1/songs/{song.id}/like/')

        assert res.status_code == status.HTTP_200_OK

        res = api_client.delete(f'/api/v1/songs/{song.id}/like/')

        assert res.status_code == status.HTTP_404_NOT_FOUND
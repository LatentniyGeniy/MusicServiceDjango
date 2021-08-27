import pytest

from rest_framework import status

from core.tests.utils import login_user


@pytest.mark.django_db
class TestLike:

    def test_like_song(self, api_client, song, user, like):

        login_user(api_client, user)
        res = api_client.get(f'/api/v1/songs/{song.id}/like')

        assert res.status_code == status.HTTP_200_OK

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

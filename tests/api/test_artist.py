import faker
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

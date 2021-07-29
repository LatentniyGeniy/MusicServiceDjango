import faker
import pytest

from rest_framework import status


@pytest.mark.django_db
class TestAlbum:

    @pytest.mark.parametrize('albums_qty', [0, 3]) #### до 5 работает нормально
    def test_list(self, client, albums, albums_qty):
        """
        test list of genres on getting right:
            * amount
        """
        res = client.get('/api/v1/albums/')

        assert res.status_code == status.HTTP_200_OK
        assert len(res.json()) == albums_qty

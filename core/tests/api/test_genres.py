import faker
import pytest

from rest_framework import status


@pytest.mark.django_db
class TestGenres:

    @pytest.mark.parametrize('genres_qty', [0, 3, 5, 7])
    def test_list(self, client, genres, genres_qty):
        """
        test list of genres on getting right:
            * amount
        """
        res = client.get('/api/v1/genres/')

        assert res.status_code == status.HTTP_200_OK
        assert len(res.json()) == genres_qty

    def test_detail_error(self, client):
        """
        test genre details for non-existing genre
        """
        res = client.get(
            f'/api/v1/genres/{faker.Faker().random_number(digits=30)}/')

        assert res.status_code == status.HTTP_404_NOT_FOUND

    def test_detail(self, client, genre):
        res = client.get(f'/api/v1/genres/{genre.id}/')
        response_data = res.json()

        assert res.status_code == status.HTTP_200_OK
        assert response_data['title'] == genre.title

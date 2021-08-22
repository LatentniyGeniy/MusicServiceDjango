import pytest

from rest_framework import status


@pytest.mark.django_db
class TestUser:

    def test_user_create(self, client):
        data = {
            'email': 'tester@example.com',
            'username': 'tester',
            'password': '123testPaSSword123',
        }
        res = client.post(f'/api/v1/registration/', data=data, content_type='application/json')
        response_data = res.json()

        assert res.status_code == status.HTTP_201_CREATED
        assert response_data['email'] == data['email']

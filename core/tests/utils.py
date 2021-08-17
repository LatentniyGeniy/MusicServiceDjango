from rest_framework_simplejwt.tokens import RefreshToken


def login_user(client, user) -> None:
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

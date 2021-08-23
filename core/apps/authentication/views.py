from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from core.apps.authentication.serializers import RegistrationSerializer
from django.contrib.auth import get_user_model


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RegistrationViewSet(GenericViewSet, CreateModelMixin):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

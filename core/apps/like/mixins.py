from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from core.apps.like import services

from core.apps.like.serializers import FanSerializer

class LikedMixin(object):

    @action(detail=True, methods=['POST', 'DELETE'])
    def like(self, request, pk=None):
        liked_object = self.get_object()

        if request.method == 'POST':
            if services.is_fan(liked_object, request.user) is True:
                return Response(status=status.HTTP_409_CONFLICT)
            else:
                services.add_like(liked_object, request.user)
                return Response()

        elif request.method == 'DELETE':
            if services.is_fan(liked_object, request.user) is False:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                services.remove_like(liked_object, request.user)
                return Response()

    @action(detail=True, methods=['GET'])
    def fans(self, request, pk=None):
        """Получает всех пользователей, которые лайкнули `obj`.
        """
        obj = self.get_object()
        fans = services.get_fans(obj)
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data)

    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` твит (`obj`).
        """
        user = self.context.get('request').user
        return services.is_fan(obj, user)
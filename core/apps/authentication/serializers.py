from rest_framework import serializers

from django.contrib.auth import get_user_model


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from users.models.common import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'role')

    def create_user(self, validated_data):
        clear_password = validated_data.pop('password', None)
        password = make_password(clear_password)

        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance

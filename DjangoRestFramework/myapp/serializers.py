from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('creator',)
        extra_kwargs = {
            'url': {'view_name': 'myapp:post-detail'},
            'creator': {'view_name': 'myapp:user-detail'}
        }


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'url', 'post_set', 'is_staff', 'password']
        read_only_fields = ('post_set', 'is_staff')
        extra_kwargs = {
            'url': {'view_name': 'myapp:user-detail'},
            'post_set': {'view_name': 'myapp:post-detail'}
        }

    def create(self, validated_data):
        """handle the password"""
        return User.objects.create_user(**validated_data)

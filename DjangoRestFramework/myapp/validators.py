from rest_framework import serializers

# from django.contrib.auth.models import User
from .models import Post, MyUser, UserLottie


class PostSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('creator',)
        extra_kwargs = {
            'url': {'view_name': 'myapp:post-detail'},
            'creator': {'view_name': 'myapp:myuser-detail'}
        }


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = MyUser
        fields = ['id', 'username', 'url', 'post_set', 'is_staff', 'password']
        read_only_fields = ('post_set', 'is_staff')
        extra_kwargs = {
            'url': {'view_name': 'myapp:myuser-detail'},
            'post_set': {'view_name': 'myapp:post-detail'}
        }

    def create(self, validated_data):
        """handle the password"""
        return MyUser.objects.create_user(**validated_data)


class LottieSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLottie
        fields = '__all__'

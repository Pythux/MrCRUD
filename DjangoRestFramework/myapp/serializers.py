from rest_framework import serializers
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


# # Serializers define the API representation. # #

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         # fields = '__all__'
#         fields = ['url', 'username', 'email', 'is_staff']
#         # exclude = ('password',)

# # # printable to get the generated serializer: # # #
# from myapp.serializers import UserSerializer
# print(UserSerializer())


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#
#     def validate(self, data):
#         # data is an OrderedDict with default value for each field if not given
#         raise serializers.ValidationError('yoyo, name: {}'.format(data['username']))
#
#     def validate_username(self, value):
#         raise serializers.ValidationError('userName :{}'.format(value))


class UserSerializer(serializers.Serializer):

    # def validate(self, data):
    #     # data is an OrderedDict with default value for each field if not given
    #     raise serializers.ValidationError('yoyo, name: {}'.format(data['username']))
    #
    # def validate_username(self, value):
    #     raise serializers.ValidationError('userName :{}'.format(value))

    url = serializers.HyperlinkedIdentityField(view_name='user-detail')
    username = serializers.CharField(
        help_text='Required. 150 characters or fewer. Letters, '
                  'digits and @/./+/-/_ only.',
        max_length=150, validators=[
            UnicodeUsernameValidator,
            UniqueValidator(queryset=User.objects.all(),
                            # overwite error message
                            message="already exist :)")])
    # email = serializers.EmailField(
    #     allow_blank=True, label='Email address',
    #     max_length=254, required=False)

    def create(self, validated_data):
        """Create & return a new `User` instance, given the validated data."""
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update & return an existing `User` instance, given the validated data."""
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

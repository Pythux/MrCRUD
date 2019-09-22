from rest_framework import serializers


class Credentials(serializers.Serializer):
    """Composite fields List and Dict"""
    login = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

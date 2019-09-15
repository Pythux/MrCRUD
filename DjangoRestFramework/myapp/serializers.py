from rest_framework import serializers

from .models import NicePlace


class NicePlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NicePlace
        fields = '__all__'


class CustomSerializer(serializers.Serializer):
    """Composite fields List and Dict"""
    title = serializers.CharField()
    place = NicePlaceSerializer()

    def create(self, validated_data):
        np = NicePlaceSerializer(data=validated_data['place'])
        # np.is_valid()
        np._validated_data = validated_data['place']
        np._errors = {}
        np.save()
        return 'good!'


"""in shell: (python manage.py shell)

from myapp import serializers as s
c = s.NicePlaceSerializer(data={'place': 'here', 'coord_x': 1, 'coord_y': 2})
c.is_valid()
# c.data
c.validated_data
c.save()

from myapp import serializers as s
c = s.CustomSerializer(data={'title': 'yo', 'place': {'place': 'here', 'coord_x': 1, 'coord_y': 2}})
c.is_valid()
# c.data
c.validated_data
c.save()
nps = s.NicePlace.objects.all()
"""

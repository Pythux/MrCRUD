from rest_framework import serializers

from .models import Country, NicePlace


class NicePlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NicePlace
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    """Composite fields List and Dict"""
    place = NicePlaceSerializer()

    class Meta:
        model = Country
        # fields = '__all__'
        exclude = 'niceplace',

    def create(self, validated_data):
        nested_data = validated_data.pop('place')
        place = self.fields['place'].create(nested_data)
        validated_data['niceplace'] = place
        return super(CountrySerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        nested_serializer = self.fields['place']
        nested_instance = instance.niceplace
        nested_data = validated_data.pop('place')
        nested_serializer.update(nested_instance, nested_data)
        # field "place" in not in validated_data, it have been `pop`ed
        return super(CountrySerializer, self).update(instance, validated_data)


"""in shell: (python manage.py shell)

from myapp import serializers as s
c = s.CountrySerializer(data={'name': 'Chill', 'place': {'name': 'here', 'coord_x': 1, 'coord_y': 2}})
c.is_valid()
# c.data
c.validated_data
c.save()

data = {'name': 'Chill', 'place': {'name': 'renamed', 'coord_x': 1, 'coord_y': 2}}
instance = s.Country.objects.all().first()
c = s.CountrySerializer(instance, data=data)
c.is_valid()
c.validated_data
c.save()  # update

nps = s.Country.objects.all()
nps.delete()
"""

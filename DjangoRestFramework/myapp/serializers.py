from rest_framework import serializers

from .models import Country, NicePlace


class NicePlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NicePlace
        # fields = '__all__'
        exclude = 'country',


class CountrySerializer(serializers.ModelSerializer):
    """Composite fields List and Dict"""
    places = NicePlaceSerializer(many=True)

    class Meta:
        model = Country
        fields = '__all__'
        # exclude = 'niceplace_set',

    # def create(self, validated_data):
    #     nested_data = validated_data.pop('place')
    #     place = self.fields['place'].create(nested_data)
    #     validated_data['niceplace'] = place
    #     return super(CountrySerializer, self).create(validated_data)

    def create(self, validated_data):
        nested_data = validated_data.pop('places')

        country = Country.objects.create(**validated_data)
        for place in nested_data:
            NicePlace(country=country, **place).save()
        return country

    def update(self, instance, validated_data):
        nested_serializer = self.fields['places']
        instance.niceplace_set.all().delete()
        for place in validated_data.pop('places'):
            place['country'] = instance
            nested_serializer.create([place])
        # field "places" in not in validated_data, it have been `pop`ed
        return super(CountrySerializer, self).update(instance, validated_data)


"""in shell: (python manage.py shell)

from myapp import serializers as s
c = s.CountrySerializer(data={'name': 'Chill', 'places': []})
c.is_valid()
# c.data
c.validated_data
c.save()

from myapp import serializers as s
data = {'name': 'Chill', 'places': [{'name': 'here', 'coord_x': 1, 'coord_y': 3}]}
data = {'name': 'Chill', 'places': [{'name': 'renamed', 'coord_x': 1, 'coord_y': 2}]}
instance = s.Country.objects.all().first()
c = s.CountrySerializer(instance, data=data)
c.is_valid()
c.validated_data
c.save()  # update

nps = s.Country.objects.all()
nps.delete()
"""

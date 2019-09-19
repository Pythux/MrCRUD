from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Country, NicePlace


class NicePlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NicePlace
        # fields = '__all__'
        exclude = 'country',


class CountrySerializer(serializers.ModelSerializer):
    """Composite fields List and Dict"""
    places = NicePlaceSerializer(many=True, source='niceplace_set')
    owner = serializers.ReadOnlyField(source='owner.username')

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
        # validated_data use the source naming
        nested_data = validated_data.pop('niceplace_set')
        country = Country.objects.create(**validated_data)
        for place in nested_data:
            NicePlace(country=country, **place).save()
        return country

    def update(self, instance, validated_data):
        nested_serializer = self.fields['places']
        instance.niceplace_set.all().delete()
        for place in validated_data.pop('niceplace_set'):
            place['country'] = instance
            nested_serializer.create([place])
        # field "places" in not in validated_data, it have been `pop`ed
        return super(CountrySerializer, self).update(instance, validated_data)


class UserSerializer(serializers.ModelSerializer):
    # country_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Country.objects.all())
    # country_set = serializers.StringRelatedField(many=True)
    # country_set = CountrySerializer(many=True, read_only=True, source='country_set')
    url = serializers.HyperlinkedIdentityField(view_name='myapp:user-detail')
    country_set = serializers.HyperlinkedRelatedField(
        view_name='myapp:country-list',
        many=True,
        read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'url', 'country_set']


"""in shell: (python manage.py shell)

from myapp import serializers as s
c = s.CountrySerializer(data={'name': 'Chill', 'places': []})

from myapp import serializers as s
data = {'name': 'Chill', 'places': [{'name': 'here', 'coord_x': 1, 'coord_y': 3}]}
data = {'name': 'Chill', 'places': [{'name': 'renamed', 'coord_x': 1, 'coord_y': 2}]}
instance = s.Country.objects.all().first()
c = s.CountrySerializer(instance, data=data)
c.is_valid()
c.validated_data
c.save()  # update

s.Country.objects.all().delete()
"""

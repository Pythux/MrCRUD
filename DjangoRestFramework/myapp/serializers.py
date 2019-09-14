from rest_framework import serializers
# from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
# from rest_framework.validators import UniqueValidator
import re


# # Serializers define the API representation. # #

class Color(object):
    """
    A color represented in the RGB colorspace.
    """
    def __init__(self, red, green, blue):
        assert(red >= 0 and green >= 0 and blue >= 0)
        assert(red < 256 and green < 256 and blue < 256)
        self.red, self.green, self.blue = red, green, blue


class ColorField(serializers.Field):
    """
    Color objects are serialized into 'rgb(#, #, #)' notation.
    """
    def to_representation(self, value):
        return "rgb(%d, %d, %d)" % (value.red, value.green, value.blue)

    default_error_messages = {
        'incorrect_type': 'Incorrect type. Expected a string, but got {input_type}',
        'incorrect_format': 'Incorrect format. Expected `rgb(#,#,#)`.',
        'out_of_range': 'Value out of range. Must be between 0 and 255.'
    }

    def to_internal_value(self, data):
        if not isinstance(data, str):
            # msg = 'Incorrect type. Expected a string, but got %s'
            # raise serializers.ValidationError(msg % type(data).__name__)
            self.fail('incorrect_type', input_type=type(data).__name__)

        if not re.match(r'^rgb\([0-9]+,[0-9]+,[0-9]+\)$', data):
            raise serializers.ValidationError('Incorrect format. Expected `rgb(#,#,#)`.')
            self.fail('incorrect_format')

        data = data.strip('rgb(').rstrip(')')
        red, green, blue = [int(col) for col in data.split(',')]

        if any([col > 255 or col < 0 for col in (red, green, blue)]):
            # raise ValidationError('Value out of range. Must be between 0 and 255.')
            self.fail('out_of_range')

        return Color(red, green, blue)


class ColorSerializer(serializers.Serializer):
    color = ColorField()


class NestedSerializer(serializers.Serializer):
    x = serializers.IntegerField()
    y = serializers.DecimalField(3, 2)


class CustomSerializer(serializers.Serializer):
    """Composite fields List and Dict"""
    title = serializers.CharField()
    list_of_position = serializers.ListField(
        max_length=2, allow_empty=False,
        child=NestedSerializer())
    dict = serializers.DictField(
        child=serializers.CharField(max_length=2))

    second_dict = NestedSerializer()
    color = ColorField()

    inserted_date = serializers.SerializerMethodField()

    def get_inserted_date(self, obj):
        return timezone.now()


"""in shell:
>>> from myapp import serializers as s

def er(d):
     c = s.CustomSerializer(data=d)
     c.is_valid()
     return c.errors

>>> er({'title': 'Titre', 'list_of_position': [{'x': 1, 'y': 1.234}],
        'dict': {'yo': 42, 'three': 123, 'da': '_'}, 'second_dict': {'x': 4, 'y': 2},
        'color': 'rgb(4,400,1)'})
"""

from rest_framework import serializers
from ..models import Color

class ColorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Color
		fields = ('name','descricion', 'hexadecimal', 'red', 'green', 'blue')

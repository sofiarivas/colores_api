from rest_framework import serializers
from ..models import Color

class ColorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Color
		fields = ('name', 'hexadecimal', 'red', 'green', 'blue')
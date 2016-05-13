from django import forms
from .models import Color
from django.utils.translation import ugettext_lazy as _

class ColorForm(forms.ModelForm):
	class Meta:
		model = Color
		fields = ['name','hexadecimal', 'red', 'green', 'blue' ]
		lables = {
		'name':  _('Escribe el nombre de tu color'),
		'hexadecimal':  _('Cual es el hexadecimal'),
		'rojo':  _('Porcentaje de rojo'),
		'green':  _('Porcentaje de verde'),
		'blue': _('Porcentaje de azul'),
		}

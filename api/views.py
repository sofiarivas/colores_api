from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Color
import json


def index(request):
    return HttpResponse('Hoooooooola')


class HomeView(View):
    def get(self, request):
        return HttpResponse('esto es una vista')


class ColorsView(View):
    def get(self, request):
        list_color = []
        colors = Color.objects.all()
        for c in colors:
            dict_color = {
                'name': c.name,
                'hexadecimal': c.hexadecimal,
                'red': c.red,
                'blue': c.blue,
                'green': c.green,
            }
            list_color.append(dict_color)

        my_colorjson = {'colors': list_color}

        return HttpResponse(json.dumps(my_colorjson), content_type='application/json')


class IndexView(View):
    def get(self, request):
        get_params = request.GET
        nombre = get_params.get('nombre', 'fulano')
        return HttpResponse('hola' + nombre)

    @method_decorator(csrf_exempt)
    def post(self, request):
        get_params = request.POST
        nombre = get_params.get('nombre', 'fulano')
        return HttpResponse('hola post ' + nombre)

    def put(self, request):
        return HttpResponse('put')

    def delete(self, request):
        return HttpResponse('delete')


class GreetView(View):
    def get(self, request, nombre):
        return HttpResponse('hola' + nombre)


class JsonView(View):
    def get(self, request):
        return HttpResponse("""
            {'grupo': 'cinta negra', 'integrantes': ['chris', 'fer', 'emilio]
            }""", content_type='application/json')

    def post(self, request):
        my_json = {
            'colors': [
                '#000000',
                '#FFFFFF',
                '#FF0000',
            ]
        }
        color = request.POST.get('color')
        if color:
            my_json['colors'].append(color)
        return HttpResponse(json.dumps(my_json), content_type='application/json')


class ColorView(View):
    colores = {
        'rojo': '#FFF0F0F',
        'azul': '#FFFFFFF'
    }

    def get(self, request, color):
        hex = self.colores.get(color)
        if hex:
            resp = {'status': 'ok', 'hex': hex}
        else:
            resp = {'status': 'error', 'message': 'Color not available'}
        return HttpResponse(json.dumps(resp), content_type='application/json')

<<<<<<< HEAD
from django.conf.urls import url, include
from .views import IndexView, GreetView, JsonView, ColorView, ColorsView,FormularioView, DisplayColors, DisplayAdvance
=======
from django.conf.urls import url
from .views import IndexView, GreetView, JsonView, ColorView, ColorsView,FormularioView
>>>>>>> eed0ca15d137888b1701b1e1bb6502d04822a1ce
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'index/$', csrf_exempt(IndexView.as_view())),
    url(r'greet/([a-z]+)$', csrf_exempt(GreetView.as_view())),
    url(r'json/$', csrf_exempt(JsonView.as_view())),
    url(r'color/([a-z]+)$', csrf_exempt(ColorView.as_view())),
    url(r'colors/$', ColorsView.as_view(),
    	name='colors'
    	),
    url(r'formulario/$', FormularioView.as_view()),
    url(r'display/$', DisplayColors.as_view(), name ="display"),
    url(r'displayadvanced/$', DisplayAdvance.as_view(), name ="displayadvance")



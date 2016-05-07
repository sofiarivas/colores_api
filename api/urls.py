from django.conf.urls import url
from .views import IndexView, GreetView, JsonView, ColorView, ColorsView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'index/$', csrf_exempt(IndexView.as_view())),
    url(r'greet/([a-z]+)$', csrf_exempt(GreetView.as_view())),
    url(r'json/$', csrf_exempt(JsonView.as_view())),
    url(r'color/([a-z]+)$', csrf_exempt(ColorView.as_view())),
    url(r'colors/$', ColorsView.as_view()),


]

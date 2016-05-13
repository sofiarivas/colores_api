from django.conf.urls import url, include
from django.contrib import admin
from api.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'restapi/', include('api.api.urls', namespace='restapi')),
    url(r'^$', HomeView.as_view(), name='homeview')
]

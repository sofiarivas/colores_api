from django.conf.urls import url, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'colors', views.ColorViewSet)

urlpatterns = [
	url(r'^', include(router.urls))
	# url(r'^colores/$',
	# 	views.ColorListView.as_view(),
	# 	name="colores_list"),
	
	# url (r'^colores/(?P<pk>\d+)/$',
	# 	views.ColorDetailView.as_view(),
	# 	name = "color_detail"),

	# url(r'^crearcolor/$',
	# 	views.ColorCreateView.as_view(),
	# 	name = "color_crear"), 

	

]
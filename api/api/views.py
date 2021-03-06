from rest_framework import generics
from ..models import Color
from .serializer import ColorSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from django.shortcuts import render

class ColorViewSet(viewsets.ModelViewSet):
	queryset = Color.objects.all()
	serializer_class = ColorSerializer

class ColorListView(generics.ListAPIView):
	queryset = Color.objects.all()
	serializer_class = ColorSerializer

class ColorDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Color.objects.all()
	serializer_class = ColorSerializer

class ColorCreateView(generics.ListCreateAPIView):
	queryset = Color.objects.all()
	serializer_class = ColorSerializer
	permission_classes = (IsAdminUser,)
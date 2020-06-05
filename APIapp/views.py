from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CountarraySerializer, DescSerializer
from .models import Desc, Countarray
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class CountarrayViewset(viewsets.ModelViewSet):
    serializer_class = CountarraySerializer
    queryset = Countarray.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ['index']


class DescViewset(viewsets.ModelViewSet):
    serializer_class = DescSerializer
    queryset = Desc.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ['desc']

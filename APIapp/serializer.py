from rest_framework import serializers
from .models import Countarray, Desc


class CountarraySerializer(serializers.ModelSerializer):
    class Meta:
        model = Countarray
        fields = ('index', 'countarray')


class DescSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desc
        fields = ('desc', 'index')

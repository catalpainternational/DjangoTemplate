from .models import *
from rest_framework import serializers


class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Appname
            fields = ('url', 'text')

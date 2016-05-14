from .models import MyModel
from rest_framework import serializers


class MyModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = MyModel
            fields = ('url', 'text')

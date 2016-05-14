from django.shortcuts import render

# Create your views here.
from .models import *
from rest_framework import viewsets
from .serializers import *


class AppViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Appname.objects.all()
    serializer_class = AppSerializer

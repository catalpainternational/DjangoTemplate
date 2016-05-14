from django.views.generic.base import TemplateView

from rest_framework import viewsets

from .serializers import MyModelSerializer
from .models import MyModel


class IndexView(TemplateView):
    template_name = 'index.html'


class MyModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

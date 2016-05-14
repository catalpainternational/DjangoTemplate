from .models import MyModel
from rest_framework import viewsets
from .serializers import MyModelSerializer


class MyModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

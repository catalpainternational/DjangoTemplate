import logging
from django.views.generic.base import TemplateView

from rest_framework import viewsets

from .serializers import ExampleModelSerializer
from .models import ExampleModel

logger = logging.getLogger({{ project_name }})


class IndexView(TemplateView):
    template_name = 'example_app/index.html'

    def get(self, request, *args, **kwargs):
        logger.debug('Index View Requested')
        return super(IndexView, self).get(request, *args, **kwargs)


class ExampleModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleModelSerializer

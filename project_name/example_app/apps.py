from __future__ import unicode_literals

from django.apps import AppConfig


class AppNameConfig(AppConfig):
    name = 'example_app'

    def ready(self):
        import signals
        

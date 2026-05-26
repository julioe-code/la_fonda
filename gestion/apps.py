import sys

from django.apps import AppConfig


class GestionConfig(AppConfig):
    name = 'gestion'

    def ready(self):
        if any(arg in sys.argv for arg in ['runserver', 'migrate', 'shell', 'test', 'check']):
            from django.contrib.auth.models import Group
            from django.db.utils import OperationalError, ProgrammingError

            try:
                for role in ['Administrador', 'Mesero', 'Cajero']:
                    Group.objects.get_or_create(name=role)
            except (OperationalError, ProgrammingError):
                pass

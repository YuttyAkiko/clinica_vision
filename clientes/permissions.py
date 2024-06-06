# permissions.py

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Consulta

content_type = ContentType.objects.get_for_model(Consulta)

edit_permission = Permission.objects.create(
    codename='can_edit_consulta',
    name='Can edit consulta',
    content_type=content_type,
)

delete_permission = Permission.objects.create(
    codename='can_delete_consulta',
    name='Can delete consulta',
    content_type=content_type,
)

view_permission = Permission.objects.create(
    codename='can_view_consulta',
    name='Can view consulta',
    content_type=content_type,
)

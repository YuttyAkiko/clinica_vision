from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Cliente
from .utils import buscar_endereco_via_cep
from django.contrib.auth.models import User
from .permissions import edit_permission, delete_permission, view_permission

@receiver(pre_save, sender=Cliente)
def preencher_endereco(sender, instance, **kwargs):
    if instance.cep:
        endereco = buscar_endereco_via_cep(instance.cep)
        if endereco:
            instance.rua = endereco['rua']
            instance.bairro = endereco['bairro']
            instance.cidade = endereco['cidade']
            instance.estado = endereco['estado']

# cliente/signals.py
# @receiver(post_save, sender=User)
def adicionar_permissoes_novo_usuario(sender, instance, created, **kwargs):
    if created:
        instance.user_permissions.add(edit_permission)
        instance.user_permissions.add(delete_permission)
        instance.user_permissions.add(view_permission)


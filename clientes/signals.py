from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Cliente
from .utils import buscar_endereco_via_cep

@receiver(pre_save, sender=Cliente)
def preencher_endereco(sender, instance, **kwargs):
    if instance.cep:
        endereco = buscar_endereco_via_cep(instance.cep)
        if endereco:
            instance.rua = endereco['rua']
            instance.bairro = endereco['bairro']
            instance.cidade = endereco['cidade']
            instance.estado = endereco['estado']

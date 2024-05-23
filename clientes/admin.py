from django.contrib import admin
from .models import Convenio, Cliente, Consulta, Receita, Exame

    
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'cpf', 'telefone', 'sexo',
    ]
    
class ConsultaAdmin(admin.ModelAdmin):
    list_display = [
        'agenda', 'cliente',
    ]
    
    
admin.site.register(Cliente, ClientAdmin)
admin.site.register(Consulta, ConsultaAdmin)

admin.site.register(Convenio)
admin.site.register(Receita)
admin.site.register(Exame)
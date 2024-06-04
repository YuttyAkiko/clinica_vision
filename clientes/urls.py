from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('registro/', views.cliente_cadastro, name='cliente_cadastro'),
    path('atualizar/', views.cliente_atualizar, name='cliente_atualizar'),
    path('consultas/', views.consulta_lista, name='consulta_lista'),
    path('consultas/criar/', views.consulta_cadastro, name='consulta_create'),
    path('consultas/editar/<int:pk>/', views.consulta_atualizar, name='consulta_update'),
    path('consultas/excluir/<int:pk>/', views.consulta_excluir, name='consulta_delete'),
    path('ajax/get_medicos/', views.get_medicos_by_especialidade, name='ajax_get_medicos'),
    path('ajax/get_dias/', views.get_dias_by_medico, name='ajax_get_dias'),
    path('ajax/get_horarios/', views.get_horarios_by_dia, name='ajax_get_horarios'),
]
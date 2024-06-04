from django.urls import path
from . import views

app_name = 'medicos'

urlpatterns = [
    #MEDICO
    path('perfil/', views.perfil, name='medico_perfil'),
    path('meus-dados/', views.atualizar_cadastro, name='atualizar_cadastro'),
    path('minha-agenda/', views.minha_agenda, name='minha_agenda'),
    path('consultas/', views.consultas_lista, name='consultas_lista'),
    path('prontuarios/', views.prontuarios_lista, name='prontuarios_lista'),
    path('prontuarios/add/<int:pk>/', views.prontuario_add, name='prontuario_add'),
    path('prontuarios/<int:pk>/', views.prontuario, name='prontuario'),

    # ADMIN
    path('registro/medico/', views.medico_cadastro, name='medico_cadastro'),
    path('registro/especialidade/', views.especialidade_cadastro, name='especialidade_cadastro'),
    path('agendar/', views.agenda_cadastro, name='agendar_consulta'),
    path('agendar/atualizar/<int:pk>/', views.agenda_atualizar, name='agendar_consulta_atualizar'),
    path('agendar/apagar/<int:pk>/', views.agenda_deletar, name='agendar_consulta_deletar'),
    path('minhas/consultas/', views.agenda_lista, name="agenda_lista"),
    path('admim/lista/medicos/', views.medico_lista, name="medicos_lista"),
    path('admim/lista/especialidades/', views.especialidade_lista, name="especialidade_lista")
]
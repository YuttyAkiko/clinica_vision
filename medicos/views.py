from django.db.models.base import Model as Model
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Medico, Agenda, Especialidade
from .forms import CreateConsultaForm
from clientes.models import Consulta, Cliente, Prontuario
from datetime import datetime

class TestMixinIsAdmin(UserPassesTestMixin):
    def test_func(self):
        is_admin_or_is_staff = self.request.user.is_superuser or \
            self.request.user.is_staff
        return bool(is_admin_or_is_staff)

    def handle_no_permission(self):
        messages.error(
            self.request, "Você não tem permissões!"
        )
        return redirect("accounts:index")

# VIEWS - PERFIL MÉDICO

class PerfilView(LoginRequiredMixin, TestMixinIsAdmin, DetailView):

    model = Medico
    login_url = 'accounts:login'
    template_name = 'medicos/perfil.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Medico, user=self.request.user)
    
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return TestMixinIsAdmin.handle_no_permission(self)
        
class CadastroUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):

    model = Medico
    login_url = reverse_lazy('accounts:login')
    template_name = 'accounts/update_user.html'
    fields = ['crm', 'telefone']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        user = self.request.user
        try:
            return Cliente.objects.get(user=user)
        except Cliente.DoesNotExist:
            return None
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MinhaAgendaListView(ListView):

    model = Agenda
    login_url = 'accounts:login'
    template_name = 'medicos/minha_agenda.html'
    context_object_name = 'horarios'

# class ConsultasListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):

#     model = Consulta
#     login_url = 'accounts:login'
#     template_name= 'medicos/consultas_lista.html'
#     context_object_name = 'consultas'

#     def get_queryset(self):
#         medico = get_object_or_404(Medico, user=self.request.user)
#         agendas = Agenda.objects.filter(medico=medico.pk)
#         consultas = Consulta.objects.filter(agenda__in=agendas, status_cons="Agendada")

#         data_consulta = self.request.GET.get('data_consulta')
#         if data_consulta:
#             data_consulta = datetime.strptime(data_consulta, '%Y-%m-%d').date()
#             consultas = consultas.filter(agenda__dia=data_consulta)
#             return consultas
#         else:
#             return consultas

# class ClientesListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):

#     model = Consulta
#     login_url = 'accounts:login'
#     template_name= 'medicos/prontuarios_lista.html'
#     context_object_name = 'consultas'

#     def get_queryset(self):
#         medico = get_object_or_404(Medico, user=self.request.user)
#         agendas = Agenda.objects.filter(medico=medico.pk)
#         consultas = Consulta.objects.filter(agenda__in=agendas, status_cons="Concluída")

#         data_consulta = self.request.GET.get('data_consulta')
#         if data_consulta:
#             data_consulta = datetime.strptime(data_consulta, '%Y-%m-%d').date()
#             consultas = consultas.filter(agenda__dia=data_consulta)
#             return consultas
#         else:
#             return consultas

class BaseConsultasListView(ListView):

    model = Consulta
    login_url = 'accounts:login'
    template_name = None
    context_object_name = 'consultas'
    status_cons_filter = None

    def get_queryset(self):
        medico = get_object_or_404(Medico, user=self.request.user)
        agendas = Agenda.objects.filter(medico=medico.pk)
        consultas = Consulta.objects.filter(agenda__in=agendas, status_cons=self.status_cons_filter)

        data_consulta = self.request.GET.get('data_consulta')
        if data_consulta:
            data_consulta = datetime.strptime(data_consulta, '%Y-%m-%d').date()
            consultas = consultas.filter(agenda__dia=data_consulta)
            return consultas
        else:
            return consultas
    
class ConsultasListView(LoginRequiredMixin, TestMixinIsAdmin, BaseConsultasListView):
    template_name = 'medicos/consultas_lista.html'
    status_cons_filter = "Agendada"

class ProntuarioListView(LoginRequiredMixin, TestMixinIsAdmin, BaseConsultasListView):
    template_name = 'medicos/prontuarios_lista.html'
    status_cons_filter = "Concluída"

class CreateProntuarioView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Prontuario
    login_url = 'accounts:login'
    template_name = 'medicos/prontuario_add.html'
    form_class = CreateConsultaForm
    success_url = reverse_lazy('medicos:medico_perfil')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = get_object_or_404(Consulta, pk= self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        consulta = get_object_or_404(Consulta, pk=self.kwargs['pk'])
        form.instance.consulta = consulta # adiciona o id da consulta na tabela de prontuario
        consulta.status_cons = "Concluída" # atualiza o status da consulta como concluida
        consulta.save()
        return super().form_valid(form)
    
class ProntuarioDetailView(LoginRequiredMixin, TestMixinIsAdmin, DetailView):
    
    model = Consulta
    login_url = 'accounts:login'
    template_name = 'medicos/prontuario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prontuario = get_object_or_404(Prontuario, consulta_id=self.get_object().pk)
        context['prontuario'] = prontuario
        return context

# VIEWS - PERFIL ADMIN

class MedicoCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Medico
    login_url = 'accounts:login'
    template_name = 'medicos/cadastro.html'
    fields = ['nome', 'crm', 'email', 'telefone', 'especialidade']
    success_url = reverse_lazy('medicos:medicos_lista')
    
class MedicoListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'medicos/medicos_lista.html'

    def get_queryset(self):
        return Medico.objects.all().order_by('-pk')
    
class EspecialidadeCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Especialidade
    login_url = 'accounts:login'
    template_name = 'medicos/cadastro.html'
    fields = ['nome',]
    success_url = reverse_lazy('medicos:especialidade_lista')
    
class EspecialidadeListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'medicos/especialidade_lista.html'

    def get_queryset(self):
        return Especialidade.objects.all().order_by('-pk')


class AgendaCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Agenda
    login_url = 'accounts:login'
    template_name = 'medicos/agenda_cadastro.html'
    fields = ['medico', 'dia', 'horario']
    success_url = reverse_lazy('medicos:agenda_lista')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AgendaUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):

    model = Agenda
    login_url = 'accounts:login'
    template_name = 'medicos/agenda_cadastro.html'
    fields = ['medico', 'dia', 'horario']
    success_url = reverse_lazy('medicos:agenda_lista')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AgendaDeleteView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    model = Agenda
    success_url = reverse_lazy('medicos:agenda_lista')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Consulta excluída com sucesso!")
        return reverse_lazy('medicos:agenda_lista')


class AgendaListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'medicos/agenda_lista.html'

    def get_queryset(self):
        return Agenda.objects.filter().order_by('-pk')

perfil = PerfilView.as_view()
atualizar_cadastro = CadastroUpdateView.as_view()
minha_agenda = MinhaAgendaListView.as_view()
consultas_lista = ConsultasListView.as_view()
prontuarios_lista = ProntuarioListView.as_view()
prontuario_add = CreateProntuarioView.as_view()
prontuario = ProntuarioDetailView.as_view()


medico_cadastro = MedicoCreateView.as_view()
medico_lista = MedicoListView.as_view()
especialidade_cadastro = EspecialidadeCreateView.as_view()
especialidade_lista = EspecialidadeListView.as_view()
agenda_cadastro = AgendaCreateView.as_view()
agenda_atualizar = AgendaUpdateView.as_view()
agenda_lista = AgendaListView.as_view()
agenda_deletar = AgendaDeleteView.as_view()


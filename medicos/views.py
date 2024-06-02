from django.db.models.base import Model as Model
from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Medico, Agenda, Especialidade
from .forms import Update_Medico_Form
from clientes.models import Consulta, Cliente
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
    login_url = 'accounts:login'
    form_class = Update_Medico_Form
    template_name = 'medicos/atualizar_dados.html'

    def get_success_url(self):
        return reverse_lazy('medicos:medico_perfil')

    def get_object(self, queryset=None):
        return get_object_or_404(Medico, user=self.request.user)
        
class HorariosListView(ListView):
    model = Agenda
    login_url = 'accounts:login'
    template_name = 'medicos/meus_horarios.html'
    context_object_name = 'agenda'

class ConsultasListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):

    model = Consulta
    login_url = 'accounts:login'
    template_name= 'medicos/minha_agenda.html'
    context_object_name = 'consultas'

    def get_queryset(self):
        medico = get_object_or_404(Medico, user=self.request.user)
        agendas = Agenda.objects.filter(medico=medico.pk)
        consultas = Consulta.objects.filter(agenda__in=agendas, status_cons="Agendada")

        data_consulta = self.request.GET.get('data_consulta')
        if data_consulta:
            data_consulta = datetime.strptime(data_consulta, '%Y-%m-%d').date()
            consultas = consultas.filter(agenda__dia=data_consulta)
            return consultas
        else:
            return consultas

class ClientesListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):

    model = Consulta
    login_url = 'accounts:login'
    template_name= 'medicos/prontuario_pacientes.html'
    context_object_name = 'consultas'

    def get_queryset(self):
        medico = get_object_or_404(Medico, user=self.request.user)
        agendas = Agenda.objects.filter(medico=medico.pk)
        consultas = Consulta.objects.filter(agenda__in=agendas, status_cons="Concluída")

        data_consulta = self.request.GET.get('data_consulta')
        if data_consulta:
            data_consulta = datetime.strptime(data_consulta, '%Y-%m-%d').date()
            consultas = consultas.filter(agenda__dia=data_consulta)
            return consultas
        else:
            return consultas
        
class ProntuarioDetailView(LoginRequiredMixin, TestMixinIsAdmin, DetailView):

    model = Consulta
    login_url = 'accounts:login'
    template_name = 'medicos/prontuario.html'
    context_object_name = 'consulta'

    def get_object(self):
        consulta = super().get_object()
        return consulta

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
horarios_disponiveis = HorariosListView.as_view()
listar_consultas = ConsultasListView.as_view()
clientes = ClientesListView.as_view()
prontuario = ProntuarioDetailView.as_view()


medico_cadastro = MedicoCreateView.as_view()
medico_lista = MedicoListView.as_view()
especialidade_cadastro = EspecialidadeCreateView.as_view()
especialidade_lista = EspecialidadeListView.as_view()
agenda_cadastro = AgendaCreateView.as_view()
agenda_atualizar = AgendaUpdateView.as_view()
agenda_lista = AgendaListView.as_view()
agenda_deletar = AgendaDeleteView.as_view()


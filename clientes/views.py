from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.utils import IntegrityError
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Cliente, Consulta
from medicos.models import Medico, Agenda, Especialidade
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConsultaForm
from django.http import JsonResponse
from datetime import datetime

class ClienteCreateView(LoginRequiredMixin ,CreateView):

    model = Cliente
    template_name = 'clientes/cadastro.html'
    fields = ['nome', 'sobre', 'sexo', 'cpf', 'telefone', 'cep', 'rua', 'bairro', 'cidade', 'estado', 'convenio']
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ClienteUpdateView(LoginRequiredMixin, UpdateView):

    model = Cliente
    login_url = reverse_lazy('accounts:login')
    template_name = 'accounts/update_user.html'
    fields = ['telefone', 'cep', 'rua', 'bairro', 'cidade', 'estado', 'convenio']
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

class ConsultaCreateView(LoginRequiredMixin, CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'clientes/cadastro.html'
    success_url = reverse_lazy('clientes:consulta_lista')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if self.request.method == 'POST':
            especialidade_id = self.request.POST.get('especialidade')
            if especialidade_id:
                form.fields['medico'].queryset = Medico.objects.filter(especialidade_id=especialidade_id).order_by('nome')
                
            medico_id = self.request.POST.get('medico')
            if medico_id:
                form.fields['dia'].queryset = Agenda.objects.filter(medico_id=medico_id).values('dia').distinct().order_by('dia')
                
            dia = self.request.POST.get('dia')
            if dia:
                form.fields['horario'].choices = [(agenda.horario, agenda.get_horario_display()) for agenda in Agenda.objects.filter(medico_id=medico_id, dia=dia)]
        else:
            form.fields['medico'].queryset = Medico.objects.none()
            form.fields['dia'].queryset = Agenda.objects.none()
            form.fields['horario'].choices = []
        return form

    def form_valid(self, form):
        try:
            cliente = Cliente.objects.get(user=self.request.user)
            medico = form.cleaned_data['medico']
            dia = form.cleaned_data['dia']
            horario = form.cleaned_data['horario']
            agenda, created = Agenda.objects.get_or_create(medico=medico, dia=dia, horario=horario)

            form.instance.cliente = cliente
            form.instance.agenda = agenda
            form.save()
            return super().form_valid(form)
        except IntegrityError as e:
            if 'UNIQUE constraint failed' in e.args[0]:
                messages.warning(self.request, 'Você não pode marcar esta consulta')
                return HttpResponseRedirect(reverse_lazy('clientes:consulta_create'))
        except Cliente.DoesNotExist:
            messages.warning(self.request, 'Complete seu cadastro')
            return HttpResponseRedirect(reverse_lazy('clientes:cliente_cadastro'))
        messages.info(self.request, 'Consulta marcada com sucesso!')
        return HttpResponseRedirect(reverse_lazy('clientes:consulta_lista'))

    """ def get_success_url(self):
        messages.success(self.request, 'Consulta marcada com sucesso!')
        return reverse_lazy('clientes:consulta_lista') """

def get_medicos_by_especialidade(request):
    especialidade_id = request.GET.get('especialidade_id')
    medicos = Medico.objects.filter(especialidade_id=especialidade_id).values('id', 'nome')
    return JsonResponse({'medicos': list(medicos)})

def get_dias_by_medico(request):
    medico_id = request.GET.get('medico_id')
    dias = Agenda.objects.filter(medico_id=medico_id).values('dia').distinct().order_by('dia')
    return JsonResponse({'dias': list(dias)})

def get_horarios_by_dia(request):
    dia = request.GET.get('dia')
    medico_id = request.GET.get('medico_id')
    horarios = Agenda.objects.filter(medico_id=medico_id, dia=dia).values('horario', 'id')
    return JsonResponse({'horarios': [{'id': horario['id'], 'horario': Agenda.HORARIOS[int(horario['horario'])-1][1]} for horario in horarios]})

""" class ConsultaCreateView(LoginRequiredMixin, CreateView):

    model = Consulta
    login_url = 'accounts:login'
    template_name = 'clientes/cadastro.html'
    fields = ['agenda']
    success_url = reverse_lazy('clientes:consulta_lista')
    
    def form_valid(self, form):
        try:
            form.instance.cliente = Cliente.objects.get(user=self.request.user)
            form.save()
        except IntegrityError as e:
            if 'UNIQUE constraint failed' in e.args[0]:
                messages.warning(self.request, 'Você não pode marcar esta consulta')
                return HttpResponseRedirect(reverse_lazy('clientes:consulta_create'))
        except Cliente.DoesNotExist:
            messages.warning(self.request, 'Complete seu cadastro')
            return HttpResponseRedirect(reverse_lazy('clientes:cliente_cadastro'))
        messages.info(self.request, 'Consulta marcada com sucesso!')
        return HttpResponseRedirect(reverse_lazy('clientes:consulta_lista')) """
    
class ConsultaUpdateView(LoginRequiredMixin, UpdateView):

    model = Consulta
    login_url = 'accounts:login'
    template_name = 'clientes/cadastro.html'
    fields = ['agenda']
    success_url = reverse_lazy('medicos:consulta_lista')
    
    def form_valid(self, form):
        form.instance.cliente = Cliente.objects.get(user=self.request.user)
        return super().form_valid(form)
    
    def alterar_consulta(request, consulta_id):
        consulta = get_object_or_404(Consulta, pk=consulta_id)
        form = Consulta(instance=consulta)
        if request.method == 'POST':
            form = Consulta(request.POST, instance=consulta)
            if form.is_valid():
                form.save()
                messages.success(request, 'Consulta alterada com sucesso!')
                return redirect('clientes:consulta_lista')
        return render(request, 'alterar_consulta.html', {'form': form, 'consulta': consulta})
    
class ConsultaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Consulta
    success_url = reverse_lazy('clientes:consulta_list')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Consulta excluída com sucesso!")
        return reverse_lazy('clientes:consulta_lista')

    """ def test_func(self):
        consulta = self.get_object()
        return consulta.cliente.user == self.request.user

    def handle_no_permission(self):
        raise Http404("Você não tem permissão para excluir esta consulta.")

def excluir_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, pk=consulta_id)
    if request.method == 'POST':
        consulta.delete()
        messages.success(request, 'Consulta excluída com sucesso!')
        return redirect('clientes:consulta_lista')
    return redirect('clientes:consulta_lista') """

class ConsultaListView(LoginRequiredMixin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'clientes/consulta_lista.html'

    def get_queryset(self):
        user=self.request.user
        try:
            cliente = Cliente.objects.get(user=user)
        except Cliente.DoesNotExist:
            messages.warning(self.request, 'Crie uma Consulta')
            return None
        try:
            consultas = Consulta.objects.filter(cliente=cliente).order_by('-pk')
        except Consulta.DoesNotExist:
            messages.warning(self.request, 'Crie uma Consulta')
            return None
        return consultas
    


cliente_cadastro = ClienteCreateView.as_view()
cliente_atualizar = ClienteUpdateView.as_view()
consulta_lista = ConsultaListView.as_view()
consulta_cadastro = ConsultaCreateView.as_view()
consulta_atualizar = ConsultaUpdateView.as_view()
consulta_excluir = ConsultaDeleteView.as_view()

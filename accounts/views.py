from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.views.generic import CreateView, UpdateView, FormView, DetailView, View
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.views import (
    LoginView, LogoutView,
    )
from .models import User
from .forms import UserAdminCreationForm
from clientes.models import Cliente

@login_required
def redirect_user_function(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return reverse('accounts:admin_perfil')
        if request.user.is_staff:
            return reverse('medicos:medico_perfil')
        else:
            return reverse('clientes:cliente_perfil') 
    else:
        # Se o usuário não estiver autenticado, redirecione para a página de login
        return reverse('accounts:login')


class RedirectUserView(View):
    @method_decorator(login_required)
    def get(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_user_function(request))
    
class PerfilView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/dashboard.html'
    login_url = reverse_lazy('accounts:login')
    
    def get_object(self):
        return self.request.user

class Login(LoginView):
    
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse('accounts:redirect_user')  
    
class Logout(LogoutView):
    template_name = 'accounts/logged_out.html'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super().get(request, *args, **kwargs)

class RegisterView(CreateView):

    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('accounts:login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        nome = form.cleaned_data['name']
        cpf = form.cleaned_data['cpf']
        # Cria uma instância de Paciente associada ao novo usuário
        Cliente.objects.create(user=self.object, nome=nome, cpf=cpf)
        messages.info(self.request, "Cadastro realizado com sucesso! Faça seu login.")
        
        return response

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name': 'Django E-commerce',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(
                            subject,
                            email,
                            "admin@exemple.com",
                            [user.email],
                            fail_silently=False
                        )
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    
                    return redirect('accounts:password_reset_done')
    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="accounts/password/password_reset.html",
        context={
            "form":form,
        })

class UpdateUserView(LoginRequiredMixin, UpdateView):

    model = User
    login_url = reverse_lazy('accounts:login')
    template_name = 'accounts/update_user.html'
    fields = ['username', 'email']
    success_url = reverse_lazy('accounts:login')

    def get_object(self):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/update_password.html'
    login_url = reverse_lazy('accounts:login')
    success_url = reverse_lazy('accounts:login')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)



admin_perfil = PerfilView.as_view()
login = Login.as_view()
logout = Logout.as_view()
register = RegisterView.as_view()
update_user = UpdateUserView.as_view()
update_password = UpdatePasswordView.as_view()
redirect_user = RedirectUserView.as_view()
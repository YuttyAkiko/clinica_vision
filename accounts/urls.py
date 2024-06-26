
from django.urls import path, reverse_lazy, include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.redirect_user, name='redirect_user'),
    path('perfil/', views.admin_perfil, name='admin_perfil'),
    path('alterar-dados/', views.update_user, name='update_user'),
    path('alterar-senha/', views.update_password, name='update_password'),
    path('cadastro/', views.register, name='register'),
    path('entrar/', views.login, name='login'),
    path('sair/', views.logout, name='logout'),  # URLs de autenticação do DRF,
    path('recuperar-senha/',
        views.password_reset_request,
        name='password_reset'
    ),
    path('recuperar-senha-ok/', 
        auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password/password_reset_done.html'
        ),
        name='password_reset_done',
    ),
    path('recuperar-senha-completo/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password/password_reset_complete.html'
            ),
            name='password_reset_complete',
    ),
    path('recuperar-senha-confirmar/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password/password_reset_confirm.html',
        success_url=reverse_lazy("accounts:password_reset_complete")
        ),
        name='password_reset_confirm'
    ),
    path(
        'password_reset_confirm',
        views.password_reset_request,
        name="password_reset"
    )

]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

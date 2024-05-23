from django.apps import AppConfig


class ClientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientes'

class SeuAppConfig(AppConfig):
    name = 'seu_app'

    def ready(self):
        import seu_app.signals


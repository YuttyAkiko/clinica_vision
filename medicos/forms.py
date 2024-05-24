from django import forms
from .models import (Especialidade, Medico, Agenda)

class Update_Medico_Form(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ('nome','sobrenome','genero','email',
                  'crm','telefone','especialidade')
        
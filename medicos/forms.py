from django import forms
from .models import (Especialidade, Medico, Agenda)

class Update_Medico_Form(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ('nome','sobrenome','genero','email',
                  'crm','telefone','especialidade')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['readonly'] = True
        self.fields['sobrenome'].widget.attrs['readonly'] = True
        self.fields['genero'].widget.attrs['readonly'] = True
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input-estilizado'})
            if field_name not in ['genero','especialidade','crm','telefone']:
                field.widget.attrs.update({'maxlength': '30', 'size': '40'})
            
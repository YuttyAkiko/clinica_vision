from django import forms
from .models import Medico
from clientes.models import Prontuario

# class Update_Medico_Form(forms.ModelForm):
#     class Meta:
#         model = Medico
#         fields = ('nome','sobrenome','genero','email','crm','telefone','especialidade')
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['nome'].widget.attrs['readonly'] = True
#         self.fields['sobrenome'].widget.attrs['readonly'] = True
#         self.fields['genero'].widget.attrs['readonly'] = True
        
#         for field_name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'input-estilizado'})
#             if field_name not in ['genero','especialidade','crm','telefone']:
#                 field.widget.attrs.update({'maxlength': '40', 'size': '40'})
#             if field_name == 'telefone':
#                 field.widget.attrs.update({'placeholder': '(00) 0000-0000'})

class CreateProntuarioForm(forms.ModelForm):

    class Meta:
        model = Prontuario
        fields = ('motivo','sintomas','observacoes','laudo')


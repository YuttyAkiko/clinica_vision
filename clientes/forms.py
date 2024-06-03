from django import forms
from clientes.models import Consulta
from medicos.models import Medico, Especialidade, Agenda

class ConsultaForm(forms.ModelForm):
    especialidade = forms.ModelChoiceField(queryset=Especialidade.objects.all(), required=True)
    medico = forms.ModelChoiceField(queryset=Medico.objects.none(), required=True)
    agenda = forms.ModelChoiceField(queryset=Agenda.objects.none(), required=True)
    data_agenda = forms.DateField(label='Data', widget=forms.DateInput(attrs={'type': 'date'}))
    hora_agenda = forms.TimeField(label='Hora', widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Consulta
        fields = ['especialidade', 'medico', 'data_agenda', 'hora_agenda', 'tipo_pag_cons']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'especialidade' in self.data:
            try:
                especialidade_id = int(self.data.get('especialidade'))
                self.fields['medico'].queryset = Medico.objects.filter(especialidade_id=especialidade_id).order_by('nome')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['medico'].queryset = self.instance.agenda.medico.especialidade.medicos.order_by('nome')

        if 'medico' in self.data:
            try:
                medico_id = int(self.data.get('medico'))
                self.fields['agenda'].queryset = Agenda.objects.filter(medico_id=medico_id).order_by('dia', 'horario')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['agenda'].queryset = self.instance.agenda.medico.agenda.order_by('dia', 'horario')

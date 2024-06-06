""" from django import forms
from .models import Consulta
from medicos.models import Medico, Agenda, Especialidade

class ConsultaForm(forms.ModelForm):
    especialidade = forms.ModelChoiceField(queryset=Especialidade.objects.all(), required=True)
    medico = forms.ModelChoiceField(queryset=Medico.objects.none(), required=True)
    dia = forms.ModelChoiceField(queryset=Agenda.objects.none(), required=True, label="Dia")
    horario = forms.ChoiceField(choices=[], required=True, label="Horário")

    class Meta:
        model = Consulta
        fields = ['especialidade', 'medico', 'dia', 'horario']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'especialidade' in self.data:
            try:
                especialidade_id = int(self.data.get('especialidade'))
                self.fields['medico'].queryset = Medico.objects.filter(especialidade_id=especialidade_id).order_by('nome')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['medico'].queryset = self.instance.especialidade.medico_set.order_by('nome')

        if 'medico' in self.data:
            try:
                medico_id = int(self.data.get('medico'))
                self.fields['dia'].queryset = Agenda.objects.filter(medico_id=medico_id).values('dia').distinct().order_by('dia')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['dia'].queryset = self.instance.medico.agenda_set.values('dia').distinct().order_by('dia')

        if 'dia' in self.data:
            try:
                dia = self.data.get('dia')
                medico_id = int(self.data.get('medico'))
                agendas = Agenda.objects.filter(medico_id=medico_id, dia=dia)
                self.fields['horario'].choices = [(agenda.horario, agenda.get_horario_display()) for agenda in agendas]
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            agendas = Agenda.objects.filter(medico=self.instance.medico, dia=self.instance.dia)
            self.fields['horario'].choices = [(agenda.horario, agenda.get_horario_display()) for agenda in agendas]
        else:
            self.fields['horario'].choices = []
 """
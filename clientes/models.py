from django.conf import settings
from django.db.models.fields.related import ForeignKey, OneToOneField
from django_cpf_cnpj.fields import CPFField
from django.core.validators import RegexValidator
from django.db import models
from medicos.models import Agenda

class Convenio(models.Model):
    nome_convenio = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nome_convenio

class Cliente(models.Model):
    nome = models.CharField(max_length=30, verbose_name="nome", default='')
    sobrenome = models.CharField(max_length=50, verbose_name="sobrenome", default='')
    cpf = CPFField(verbose_name="CPF",
                    max_length=50,
                    unique=True,)
    data_nasc  = models.DateField(auto_now=False, auto_now_add=False, verbose_name="nascimento", default='2000-01-01')
    SEXO = (
        ("M", "Masculino"),
        ("F", "Feminino")
    )
    sexo = models.CharField(max_length=9, choices=SEXO,)
    phone_regex = RegexValidator(
    regex=r'^\(?\d{2}\)?[\s.-]?\d{4,5}-?\d{4}$',
    message="O número precisa estar neste formato: (00) 00000-0000 ou (00) 0000-0000")

    telefone = models.CharField(verbose_name="Telefone",
                                validators=[phone_regex],
                                max_length=17, null=True, blank=True)
    cep = models.CharField(max_length=8, verbose_name="CEP", default='00000000')
    rua = models.CharField(max_length=255, blank=True, null=True, verbose_name="rua")
    bairro = models.CharField(max_length=255, blank=True, null=True, verbose_name="bairro")
    cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name="cidade")
    estado = models.CharField(max_length=2, blank=True, null=True, verbose_name="estado")
    email = models.EmailField(max_length=300, verbose_name="e-mail", default='seu_email@email.com')
    status_cad_pac = models.BooleanField(verbose_name="ativar cadastro", default=True)
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE, blank=True, null=True, verbose_name="convênio") # Relacionamento (1,n)
    num_carteirinha = models.IntegerField(blank=True, default=0, verbose_name="carteirinha")
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuário', 
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f'{self.user.name}'
    
class Consulta(models.Model):
    agenda =  OneToOneField(Agenda, on_delete=models.CASCADE, related_name='consulta')
    cliente = ForeignKey(Cliente, on_delete=models.CASCADE, related_name='consulta')
    TIPOS_PAGAMENTO = (
        ('Convênio','Convênio'),
        ('Cartão','Cartão'),
        ('Dinheiro','Dinheiro'),
        ('Pix','Pix')
    )
    tipo_pag_cons = models.CharField(max_length=10, choices=TIPOS_PAGAMENTO, default=TIPOS_PAGAMENTO)
    STATUS_PAGAMENTO = (
        ('Pago','Pago'),
        ('Pendente', 'Pendente')
    )
    status_pag_cons = models.CharField(max_length=10, choices=STATUS_PAGAMENTO, default=STATUS_PAGAMENTO) # Select "Yes" ou "No" para o status de pagamento.
    STATUS_CONSULTA = (
        ('Concluída', 'Concluída'),
        ('Cancelada', 'Cancelada'),
        ('Agendada', 'Agendada'),
        ('Remarcada', 'Remarcada'),
    )
    status_cons = models.CharField(max_length=10, choices=STATUS_CONSULTA, default=STATUS_CONSULTA)
    motivo = models.CharField(max_length=199, default='')
    sintomas = models.TextField(max_length=2000, null=True, blank=True)
    observacoes = models.TextField(max_length=2000, null=True, blank=True)
    laudo = models.TextField(max_length=2000, null=True, blank=True)
    
    class Meta:
        unique_together = ('agenda', 'cliente')
        
    def __str__(self):
        return f'{self.agenda} - {self.cliente}'

class Receita(models.Model):
    consulta = models.ForeignKey('Consulta', on_delete=models.CASCADE) # Relacionamento (1,n)
    data = models.DateTimeField(auto_now_add=True)
    L_esf_OD = models.CharField(max_length=30, null=True)
    L_esf_OE = models.CharField(max_length=30, null=True)
    L_cil_OD = models.CharField(max_length=30, null=True)
    L_cil_OE = models.CharField(max_length=30, null=True)
    L_eixo_OD = models.CharField(max_length=30, null=True)
    L_eixo_OE = models.CharField(max_length=30, null=True)
    L_dp_OD = models.CharField(max_length=30, null=True)
    L_dp_OE = models.CharField(max_length=30, null=True)
    P_esf_OD = models.CharField(max_length=30, null=True)
    P_esf_OE = models.CharField(max_length=30, null=True)
    P_cil_OD = models.CharField(max_length=30, null=True)
    P_cil_OE = models.CharField(max_length=30, null=True)
    P_eixo_OD = models.CharField(max_length=30, null=True)
    P_eixo_OE = models.CharField(max_length=30, null=True)
    P_dp_OD = models.CharField(max_length=30, null=True)
    P_dp_OE = models.CharField(max_length=30, null=True)

class Exame(models.Model):
    id_consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    tipo_exame = models.CharField(max_length=30)
    valor_exame = models.FloatField()
    TIPOS_PAGAMENTO = (
            ('Convênio','Convênio'),
            ('Cartão','Cartão'),
            ('Dinheiro','Dinheiro'),
            ('Pix','Pix')
        )
    tipo_pag_ex = models.CharField(max_length=10, choices=TIPOS_PAGAMENTO)
    STATUS_PAGAMENTO = (
            ('Pago','Pago'),
            ('Pendente', 'Pendente')
        )
    status_pag_ex = models.CharField(max_length=10, choices=STATUS_PAGAMENTO) # Select "Yes" ou "No" para o status de pagamento.
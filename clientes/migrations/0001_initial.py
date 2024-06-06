<<<<<<< HEAD
# Generated by Django 5.0.4 on 2024-05-23 16:06
=======
# Generated by Django 5.0.4 on 2024-06-06 15:34
>>>>>>> 74c90b8ed65ea8a489ee6dc9a3271a4cb91f86be

import django.core.validators
import django.db.models.deletion
import django_cpf_cnpj.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_convenio', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=30, verbose_name='nome')),
                ('sobrenome', models.CharField(default='', max_length=50, verbose_name='sobrenome')),
                ('cpf', django_cpf_cnpj.fields.CPFField(max_length=50, unique=True, verbose_name='CPF')),
                ('data_nasc', models.DateField(default='2000-01-01', verbose_name='nascimento')),
<<<<<<< HEAD
                ('sexo', models.CharField(choices=[('MAS', 'Maculino'), ('FEM', 'Feminino')], max_length=9)),
                ('telefone', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="O número precisa estar neste formato:                         '+99 99 9999-0000'.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Telefone')),
=======
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=9)),
                ('telefone', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='O número precisa estar neste formato: (00) 00000-0000 ou (00) 0000-0000', regex='^\\(?\\d{2}\\)?[\\s.-]?\\d{4,5}-?\\d{4}$')], verbose_name='Telefone')),
>>>>>>> 74c90b8ed65ea8a489ee6dc9a3271a4cb91f86be
                ('cep', models.CharField(default='00000000', max_length=8, verbose_name='CEP')),
                ('rua', models.CharField(blank=True, max_length=255, null=True, verbose_name='rua')),
                ('bairro', models.CharField(blank=True, max_length=255, null=True, verbose_name='bairro')),
                ('cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='cidade')),
                ('estado', models.CharField(blank=True, max_length=2, null=True, verbose_name='estado')),
                ('email', models.EmailField(default='seu_email@email.com', max_length=300, verbose_name='e-mail')),
                ('status_cad_pac', models.BooleanField(default=True, verbose_name='ativar cadastro')),
                ('num_carteirinha', models.IntegerField(blank=True, default=0, verbose_name='carteirinha')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
                ('convenio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.convenio', verbose_name='convênio')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('tipo_pag_cons', models.CharField(choices=[('Convênio', 'Convênio'), ('Cartão', 'Cartão'), ('Dinheiro', 'Dinheiro'), ('Pix', 'Pix')], default=(('Convênio', 'Convênio'), ('Cartão', 'Cartão'), ('Dinheiro', 'Dinheiro'), ('Pix', 'Pix')), max_length=10)),
                ('status_pag_cons', models.CharField(choices=[('Pago', 'Pago'), ('Pendente', 'Pendente')], default=(('Pago', 'Pago'), ('Pendente', 'Pendente')), max_length=10)),
                ('status_cons', models.CharField(choices=[('Concluída', 'Concluída'), ('Cancelada', 'Cancelada'), ('Agendada', 'Agendada'), ('Remarcada', 'Remarcada')], default=(('Concluída', 'Concluída'), ('Cancelada', 'Cancelada'), ('Agendada', 'Agendada'), ('Remarcada', 'Remarcada')), max_length=10)),
                ('motivo', models.CharField(default='', max_length=199)),
                ('sintomas', models.TextField(blank=True, max_length=2000, null=True)),
                ('observacoes', models.TextField(blank=True, max_length=2000, null=True)),
                ('laudo', models.TextField(blank=True, max_length=2000, null=True)),
=======
                ('tipo_pag_cons', models.CharField(choices=[('Convênio', 'Convênio'), ('Cartão', 'Cartão'), ('Dinheiro', 'Dinheiro'), ('Pix', 'Pix')], default='', max_length=10)),
                ('status_pag_cons', models.CharField(choices=[('Pago', 'Pago'), ('Pendente', 'Pendente')], default='', max_length=10)),
                ('status_cons', models.CharField(choices=[('Concluída', 'Concluída'), ('Cancelada', 'Cancelada'), ('Agendada', 'Agendada'), ('Remarcada', 'Remarcada')], default=(('Concluída', 'Concluída'), ('Cancelada', 'Cancelada'), ('Agendada', 'Agendada'), ('Remarcada', 'Remarcada')), max_length=10)),
>>>>>>> 74c90b8ed65ea8a489ee6dc9a3271a4cb91f86be
                ('agenda', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='consulta', to='medicos.agenda')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consulta', to='clientes.cliente')),
            ],
            options={
                'unique_together': {('agenda', 'cliente')},
            },
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='Exame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_exame', models.CharField(max_length=30)),
                ('valor_exame', models.FloatField()),
                ('tipo_pag_ex', models.CharField(choices=[('Convênio', 'Convênio'), ('Cartão', 'Cartão'), ('Dinheiro', 'Dinheiro'), ('Pix', 'Pix')], max_length=10)),
                ('status_pag_ex', models.CharField(choices=[('Pago', 'Pago'), ('Pendente', 'Pendente')], max_length=10)),
                ('id_consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.consulta')),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('L_esf_OD', models.CharField(max_length=30, null=True)),
                ('L_esf_OE', models.CharField(max_length=30, null=True)),
                ('L_cil_OD', models.CharField(max_length=30, null=True)),
                ('L_cil_OE', models.CharField(max_length=30, null=True)),
                ('L_eixo_OD', models.CharField(max_length=30, null=True)),
                ('L_eixo_OE', models.CharField(max_length=30, null=True)),
                ('L_dp_OD', models.CharField(max_length=30, null=True)),
                ('L_dp_OE', models.CharField(max_length=30, null=True)),
                ('P_esf_OD', models.CharField(max_length=30, null=True)),
                ('P_esf_OE', models.CharField(max_length=30, null=True)),
                ('P_cil_OD', models.CharField(max_length=30, null=True)),
                ('P_cil_OE', models.CharField(max_length=30, null=True)),
                ('P_eixo_OD', models.CharField(max_length=30, null=True)),
                ('P_eixo_OE', models.CharField(max_length=30, null=True)),
                ('P_dp_OD', models.CharField(max_length=30, null=True)),
                ('P_dp_OE', models.CharField(max_length=30, null=True)),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.consulta')),
=======
            name='Prontuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=199)),
                ('sintomas', models.TextField(max_length=2000)),
                ('observacoes', models.TextField(max_length=2000)),
                ('laudo', models.TextField(max_length=2000)),
                ('consulta', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='clientes.consulta')),
>>>>>>> 74c90b8ed65ea8a489ee6dc9a3271a4cb91f86be
            ],
        ),
    ]

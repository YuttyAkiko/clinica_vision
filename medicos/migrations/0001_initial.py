<<<<<<< HEAD
# Generated by Django 5.0.4 on 2024-05-23 16:06
=======
# Generated by Django 5.0.4 on 2024-06-06 15:34
>>>>>>> 74c90b8ed65ea8a489ee6dc9a3271a4cb91f86be

import django.core.validators
import django.db.models.deletion
import medicos.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('valor_consulta', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=200, verbose_name='Nome')),
                ('sobrenome', models.CharField(default='', max_length=200, verbose_name='Sobrenome')),
<<<<<<< HEAD
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('crm', models.CharField(max_length=200, verbose_name='CRM')),
                ('telefone', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='O número precisa estar neste formato: (00) 00000-0000 ou (00) 0000-0000', regex='^\\(?\\d{2}\\)?[\\s.-]?\\d{4,5}-?\\d{4}$')], verbose_name='Telefone')),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicos', to='medicos.especialidade')),
=======
                ('genero', models.CharField(choices=[('Feminino', 'Feminino'), ('Masculimo', 'Masculino')], default='', max_length=9)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('crm', models.CharField(max_length=200, verbose_name='CRM')),
                ('telefone', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='O número precisa estar neste formato: (00) 00000-0000 ou (00) 0000-0000', regex='^\\(?\\d{2}\\)?[\\s.-]?\\d{4,5}-?\\d{4}$')], verbose_name='Telefone')),
                ('especialidade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicos', to='medicos.especialidade')),
                ('user', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
>>>>>>> 74c90b8ed65ea8a489ee6dc9a3271a4cb91f86be
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(help_text='Insira uma data para agenda', validators=[medicos.models.validar_dia])),
<<<<<<< HEAD
                ('horario', models.CharField(choices=[('1', '07:00 ás 08:00'), ('2', '08:00 ás 09:00'), ('3', '09:00 ás 10:00'), ('4', '10:00 ás 11:00'), ('5', '11:00 ás 12:00')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
=======
                ('horario', models.CharField(choices=[('1', '07:00 ás 08:00'), ('2', '08:00 ás 09:00'), ('3', '09:00 ás 10:00'), ('4', '10:00 ás 11:00'), ('5', '11:00 ás 12:00'), ('6', '13:00 ás 14:00'), ('7', '14:00 ás 15:00'), ('8', '15:00 ás 16:00'), ('9', '16:00 ás 17:00'), ('10', '17:00 ás 18:00')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
                ('especialidade', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='medicos.especialidade')),
>>>>>>> 74c90b8ed65ea8a489ee6dc9a3271a4cb91f86be
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agenda', to='medicos.medico')),
            ],
            options={
                'unique_together': {('horario', 'dia')},
            },
        ),
    ]

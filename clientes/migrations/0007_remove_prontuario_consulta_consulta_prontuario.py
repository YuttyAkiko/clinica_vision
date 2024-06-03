# Generated by Django 5.0.4 on 2024-06-03 22:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_alter_prontuario_consulta_alter_prontuario_laudo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prontuario',
            name='consulta',
        ),
        migrations.AddField(
            model_name='consulta',
            name='prontuario',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='consulta_prontuario', to='clientes.consulta'),
        ),
    ]

# Generated by Django 5.0.4 on 2024-06-03 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_alter_prontuario_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prontuario',
            name='consulta',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='consulta_prontuario', to='clientes.consulta'),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='laudo',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='motivo',
            field=models.CharField(max_length=199),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='observacoes',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='prontuario',
            name='sintomas',
            field=models.TextField(max_length=2000),
        ),
    ]

# Generated by Django 5.0.4 on 2024-06-03 23:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_remove_consulta_prontuario_prontuario_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prontuario',
            name='consulta',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='clientes.consulta'),
        ),
    ]
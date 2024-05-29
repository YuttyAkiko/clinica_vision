# Generated by Django 5.0.4 on 2024-05-24 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0002_medico_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='genero',
            field=models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], default='', max_length=9),
        ),
    ]
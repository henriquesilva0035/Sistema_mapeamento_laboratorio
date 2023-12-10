# Generated by Django 4.2.7 on 2023-12-10 19:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materiais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_material', models.CharField(max_length=30)),
                ('reservado', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Material',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reserva', models.DateField()),
                ('data_devolucao', models.DateField()),
                ('data_solicitacao', models.DateField(default=datetime.date.today)),
                ('materiais', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='materiais.materiais')),
                ('usuarios', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario')),
            ],
            options={
                'verbose_name': 'Reserva',
            },
        ),
    ]

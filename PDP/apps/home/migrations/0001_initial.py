# Generated by Django 3.2.12 on 2024-05-14 19:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliação',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processCode', models.CharField(default='TI-03-2024', max_length=10)),
                ('numAvaliador', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Collaborators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(default='N/A', max_length=100)),
                ('Apelido', models.CharField(default='N/A', max_length=100)),
                ('Departamento', models.CharField(default='N/A', max_length=100)),
                ('NumColab', models.IntegerField(default=0)),
                ('NumAvali', models.IntegerField(default=0)),
                ('Func', models.CharField(default='N/A', max_length=100)),
                ('Data', models.DateField(default=django.utils.timezone.now)),
                ('Grupo', models.CharField(default='N/A', max_length=100)),
                ('DirUni', models.IntegerField(default=0)),
                ('Pin', models.CharField(default='0000', max_length=4)),
                ('Ano', models.DateField(default=django.utils.timezone.now)),
                ('FaltaJust', models.FloatField(default=0)),
                ('FaltaInjust', models.FloatField(default=0)),
            ],
        ),
    ]

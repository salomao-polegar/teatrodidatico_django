# Generated by Django 4.1.2 on 2022-10-19 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teatrodidatico', '0022_alter_fotos_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('modalidade', models.CharField(choices=[('P', 'Presencial'), ('O', 'Online')], max_length=200)),
                ('data_inscriaco_inicial', models.DateField()),
                ('data_inscricao_final', models.DateField()),
                ('local', models.CharField(blank=True, max_length=200, null=True)),
                ('observacoes', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramaCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('conteudo', models.TextField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teatrodidatico.cursos')),
            ],
        ),
    ]

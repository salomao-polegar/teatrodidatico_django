# Generated by Django 4.1.2 on 2022-10-19 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teatrodidatico', '0029_alter_programacurso_curso_alter_textos_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='modalidade',
            field=models.CharField(choices=[('P', 'Atividade presencial'), ('O', 'Atividade online')], max_length=200),
        ),
    ]

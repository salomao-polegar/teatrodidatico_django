# Generated by Django 4.1.2 on 2022-10-17 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teatrodidatico', '0018_alter_agenda_espetaculo_alter_agenda_inscricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculo',
            name='tipo',
            field=models.CharField(choices=[('1', 'Currículo'), ('2', 'Premio')], max_length=20, verbose_name='Tipo'),
        ),
    ]

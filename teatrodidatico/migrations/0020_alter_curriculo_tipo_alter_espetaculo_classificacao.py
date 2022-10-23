# Generated by Django 4.1.2 on 2022-10-17 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teatrodidatico', '0019_alter_curriculo_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculo',
            name='tipo',
            field=models.CharField(choices=[('1', 'Currículo'), ('2', 'Premio')], max_length=1, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='espetaculo',
            name='classificacao',
            field=models.CharField(choices=[('0', 'Livre'), ('10', 'Recomendado para maiores de 10 anos'), ('12', 'Recomendado para maiores de 12 anos'), ('14', 'Recomendado para maiores de 14 anos'), ('16', 'Recomendado para maiores de 16 anos'), ('18', 'Recomendado para maiores de 18 anos')], max_length=2, verbose_name='Classificação indicatica'),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-14 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teatrodidatico', '0004_remove_atividades_is_espetaculo_atividades_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividades',
            name='agradecimentos',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='atividades',
            name='classificacao',
            field=models.CharField(choices=[(0, 'Livre'), (10, 'Recomendado para maiores de 10 anos'), (12, 'Recomendado para maiores de 12 anos'), (14, 'Recomendado para maiores de 14 anos'), (16, 'Recomendado para maiores de 16 anos'), (18, 'Recomendado para maiores de 18 anos')], max_length=40),
        ),
        migrations.AlterField(
            model_name='atividades',
            name='sinopse',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='atividades',
            name='trilha_sonora',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
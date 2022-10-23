# Generated by Django 4.1.2 on 2022-10-14 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teatrodidatico', '0007_rename_atividades_atividade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='espetaculo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='teatrodidatico.atividade'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='idade',
            field=models.CharField(choices=[('0', 'Livre'), ('10', 'Recomendado para maiores de 10 anos'), ('12', 'Recomendado para maiores de 12 anos'), ('14', 'Recomendado para maiores de 14 anos'), ('16', 'Recomendado para maiores de 16 anos'), ('18', 'Recomendado para maiores de 18 anos')], max_length=20),
        ),
    ]

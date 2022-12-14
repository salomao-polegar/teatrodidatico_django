# Generated by Django 4.1.2 on 2022-10-17 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teatrodidatico', '0017_alter_curriculo_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='espetaculo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='teatrodidatico.espetaculo'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='inscricao',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Link para inscrição, se houver'),
        ),
        migrations.AlterField(
            model_name='curriculo',
            name='espetaculo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='teatrodidatico.espetaculo'),
        ),
        migrations.AlterField(
            model_name='curriculo',
            name='evento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='teatrodidatico.evento'),
        ),
        migrations.AlterField(
            model_name='curriculo',
            name='premio',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Prêmio'),
        ),
        migrations.AlterField(
            model_name='espetaculo',
            name='foto_principal',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/%d/%m/%Y/'),
        ),
        migrations.AlterField(
            model_name='espetaculo',
            name='trilha_sonora',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='espetaculo',
            name='video',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Vídeo (link do youtube)'),
        ),
        migrations.AlterField(
            model_name='fotos',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/%d/%m/%Y/'),
        ),
        migrations.AlterField(
            model_name='integrantes',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]

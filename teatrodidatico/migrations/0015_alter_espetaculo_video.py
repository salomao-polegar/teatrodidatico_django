# Generated by Django 4.1.2 on 2022-10-15 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teatrodidatico', '0014_espetaculo_video_alter_espetaculo_classificacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espetaculo',
            name='video',
            field=models.CharField(blank=True, max_length=200, verbose_name='Vídeo (link do youtube)'),
        ),
    ]

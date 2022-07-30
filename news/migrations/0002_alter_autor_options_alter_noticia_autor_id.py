# Generated by Django 4.0.6 on 2022-07-30 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterField(
            model_name='noticia',
            name='autor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.autor', verbose_name='Autor'),
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-31 20:31

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('tcc', '0004_alter_ultimapartida_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ultimapartida',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='tcc/static/images', variations={}, verbose_name='Imagem'),
        ),
    ]

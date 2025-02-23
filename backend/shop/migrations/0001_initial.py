# Generated by Django 5.1.6 on 2025-02-20 00:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Panorama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('image', models.ImageField(upload_to='panoramas/', verbose_name='Imagen 360 (JPG)')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Hotspot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField(help_text='Valor entre 0 y 100', verbose_name='Coordenada X')),
                ('y', models.FloatField(help_text='Valor entre 0 y 100', verbose_name='Coordenada Y')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Descripción')),
                ('panorama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotspots', to='shop.panorama')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]

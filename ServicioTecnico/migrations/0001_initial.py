# Generated by Django 4.0.5 on 2022-07-09 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('cedula', models.CharField(max_length=10, verbose_name='Cedula')),
                ('telefono', models.CharField(max_length=9, verbose_name='Telefono')),
                ('telefonoMovil', models.CharField(max_length=10, verbose_name='TelefonoMovil')),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('numSerie', models.CharField(max_length=14, verbose_name='Numero de Serie')),
                ('observaciones', models.CharField(max_length=500, verbose_name='Observaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaEmision', models.DateField(verbose_name='Fecha de Emisión')),
                ('subTotalProductos', models.FloatField(verbose_name='Sub Total de Productos')),
                ('valorTotal', models.FloatField(verbose_name='Valor Total')),
                ('fechaCierre', models.DateField(verbose_name='Fecha de Cierre')),
                ('estado', models.CharField(max_length=30, verbose_name='Estaodo')),
                ('subTotalServicios', models.FloatField(verbose_name='Sub Total Servicios')),
                ('tipo', models.CharField(max_length=30, verbose_name='Direccion')),
            ],
        ),
    ]

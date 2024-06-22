# Generated by Django 5.0.6 on 2024-06-19 00:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_rut', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('correo_electronico', models.EmailField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id_documento', models.AutoField(primary_key=True, serialize=False)),
                ('nom_documento', models.CharField(max_length=255)),
                ('tipo_documento', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id_notificacion', models.AutoField(primary_key=True, serialize=False)),
                ('id_usuario', models.IntegerField()),
                ('tipo_usuario', models.CharField(choices=[('cliente', 'Cliente'), ('abogado', 'Abogado')], max_length=10)),
                ('mensaje', models.TextField()),
                ('fecha', models.DateField()),
                ('leido', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Abogado',
            fields=[
                ('id_abogado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('especialidad', models.CharField(max_length=255)),
                ('ano_experiencia', models.IntegerField()),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='abogados.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id_contrato', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_contrato', models.DateField()),
                ('monto_contrato', models.DecimalField(decimal_places=2, max_digits=10)),
                ('modalidad_pago', models.CharField(max_length=255)),
                ('observacion', models.TextField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abogados.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Causa',
            fields=[
                ('id_causas', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('tipo_causas', models.CharField(max_length=255)),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('estado', models.CharField(max_length=255)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abogados.cliente')),
                ('contrato', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='abogados.contrato')),
                ('documento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='abogados.documento')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_pago', models.DateField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo_pago', models.CharField(max_length=255)),
                ('abogado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='abogados.abogado')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoCuenta',
            fields=[
                ('id_estado_cuenta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('ingresos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gastos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('beneficio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abogados.pago')),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-02 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abogados', '0005_remove_notificacion_rut_usuario_notificacion_cliente_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='causa',
        ),
        migrations.DeleteModel(
            name='Causa',
        ),
    ]

# Generated by Django 4.1.4 on 2023-03-30 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_campana_intcal_respuesta_alter_marca_mar_apellido_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campana',
            old_name='intcal_respuesta',
            new_name='cam_estado',
        ),
    ]

# Generated by Django 4.0 on 2021-12-14 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addToStorage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipments',
            old_name='EquipmentType_id',
            new_name='equipmentType_id',
        ),
    ]

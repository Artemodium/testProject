# Generated by Django 4.0 on 2021-12-13 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('serialNumberMask', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Equipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialNumber', models.CharField(max_length=50, unique=True)),
                ('EquipmentType_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='addToStorage.equipmenttype')),
            ],
        ),
    ]

from django.db import models


class EquipmentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    serialNumberMask = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Equipments(models.Model):
    id = models.IntegerField
    equipmentType_id = models.ForeignKey('EquipmentType', on_delete=models.PROTECT, null=True)
    serialNumber = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.serialNumber

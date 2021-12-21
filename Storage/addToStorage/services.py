from .models import Equipments, EquipmentType
import re


def getSerialsFromBase():
    res = []
    for e in list(Equipments.objects.all()):
        res.append(e.serialNumber)
    return res


def parsingSerials(data):
    serials = re.findall(r'[\S]+[^, \n]+', data[list(data.keys())[1]])
    mask = data[list(data.keys())[0]].serialNumberMask
    correct = [s for s in serials if re.fullmatch(mask, s)]
    correct = list(set(correct))
    incorrect = [s.strip() for s in serials if not re.fullmatch(mask, s)]
    doubles = [s.strip() for s in correct if s in getSerialsFromBase()]
    correct = [s.strip() for s in correct if s not in getSerialsFromBase()]
    return {'correct': correct, 'incorrect': incorrect, 'doubles':doubles}


def insertTobase(data, serials):
    equipmentType_id = data[list(data.keys())[0]].id
    for s in serials:
        equipment = EquipmentType.objects.get(id=equipmentType_id)
        serial = Equipments(serialNumber=s, equipmentType_id=equipment)
        serial.save()
    return

from django import forms
from .models import EquipmentType


class AddEqiupmentsForm(forms.Form):
    equipment = forms.ModelChoiceField(queryset=EquipmentType.objects.all(),
                                       empty_label="Выбрать",
                                       label='Тип оборудования',
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    serials = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 100px'}),
                              label='Серийные номера')

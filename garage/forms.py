from django import forms
from .models import ServiceRecord, Motorcycle


class ServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceRecord
        # Перечисляем поля, которые пользователь должен заполнить сам.
        # Поле 'motorcycle' мы не включаем, потому что подставим его сами (мы же знаем, на странице какого байка находимся).
        fields = ['title', 'date', 'mileage', 'cost', 'notes']

        # Небольшая красота: добавим календарь для поля даты
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class MotorcycleForm(forms.ModelForm):
    class Meta:
        model = Motorcycle
        fields = ['brand', 'model', 'year', 'vin']
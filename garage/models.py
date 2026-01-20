from django.db import models


class Motorcycle(models.Model):
    brand = models.CharField(max_length=50, verbose_name="Марка")
    model = models.CharField(max_length=50, verbose_name="Модель")
    year = models.IntegerField(verbose_name="Год выпуска")
    vin = models.CharField(max_length=17, blank=True, null=True, verbose_name="VIN")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class ServiceRecord(models.Model):
    # Связь с мотоциклом: удалил мот -> удалились записи (CASCADE)
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE, verbose_name="Мотоцикл")
    title = models.CharField(max_length=100, verbose_name="Вид работ")
    date = models.DateField(verbose_name="Дата")
    mileage = models.IntegerField(verbose_name="Пробег (км)")
    cost = models.IntegerField(default=0, verbose_name="Стоимость")
    notes = models.TextField(blank=True, verbose_name="Заметки")

    def __str__(self):
        return f"{self.title} ({self.date})"

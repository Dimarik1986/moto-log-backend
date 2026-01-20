from django.shortcuts import render, get_object_or_404, redirect # <-- Добавили сюда
from django.contrib import messages # Для красивых уведомлений
from .utils import get_moto_data_by_vin # Наша функция

from .forms import ServiceForm, MotorcycleForm
from .models import Motorcycle


def moto_list(request):
    # Достаем все мотоциклы из базы
    motorcycles = Motorcycle.objects.all()
    # Отдаем их в шаблон index.html
    return render(request, 'garage/index.html', {'motorcycles': motorcycles})


def moto_detail(request, pk):
    # Ищем мотоцикл по ID. Если нет - 404.
    moto = get_object_or_404(Motorcycle, pk=pk)

    # Достаем все записи ремонта для ЭТОГО мотоцикла
    # Помнишь related_name или просто обратную связь?
    # Django по умолчанию делает set: servicerecord_set
    services = moto.servicerecord_set.all().order_by('-date')

    return render(request, 'garage/detail.html', {'moto': moto, 'services': services})


def add_service(request, pk):
    # 1. Находим мотоцикл, к которому добавляем запись
    moto = get_object_or_404(Motorcycle, pk=pk)

    if request.method == 'POST':
        # Если данные пришли - заполняем ими форму
        form = ServiceForm(request.POST)
        if form.is_valid():
            # commit=False означает "создай объект, но пока не пиши в базу"
            service = form.save(commit=False)
            # Привязываем запись к конкретному мотоциклу
            service.motorcycle = moto
            # Теперь сохраняем окончательно
            service.save()
            # Перекидываем пользователя обратно на страницу мотоцикла
            return redirect('moto_detail', pk=pk)
    else:
        # Если просто открыли страницу - даем пустую форму
        form = ServiceForm()

    return render(request, 'garage/add_service.html', {'form': form, 'moto': moto})


def add_motorcycle(request):
    # Пустой словарь для данных формы
    initial_data = {}

    # 1. ПРОВЕРКА: Нажал ли юзер кнопку "Найти по VIN"?
    # (Это GET-запрос, потому что мы просто запрашиваем данные, не сохраняя)
    if 'search_vin' in request.GET:
        vin = request.GET.get('vin_search_field')
        found_data = get_moto_data_by_vin(vin)

        if found_data:
            # Если нашли - подставим данные в форму
            initial_data = {
                'vin': vin,
                'brand': found_data['brand'],
                'model': found_data['model'],
                'year': found_data['year']
            }
            messages.success(request, f"Нашли байк: {found_data['brand']} {found_data['model']}")
        else:
            messages.error(request, "Ничего не найдено. Проверьте VIN.")

    # 2. ОБРАБОТКА СОХРАНЕНИЯ (POST)
    if request.method == 'POST':
        form = MotorcycleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('moto_list')
    else:
        # Если это просто открытие страницы ИЛИ мы вернулись с данными VIN
        form = MotorcycleForm(initial=initial_data)

    return render(request, 'garage/add_moto.html', {'form': form})
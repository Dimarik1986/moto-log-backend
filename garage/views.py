from django.shortcuts import render, get_object_or_404, redirect # <-- Добавили сюда

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
    if request.method == 'POST':
        form = MotorcycleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('moto_list')  # После сохранения кидаем на главную
    else:
        form = MotorcycleForm()

    return render(request, 'garage/add_moto.html', {'form': form})
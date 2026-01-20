from django.urls import path
from . import views

urlpatterns = [
    # Пустая строка '' означает главную страницу этого раздела
    path('', views.moto_list, name='moto_list'),
    path('moto/<int:pk>/', views.moto_detail, name='moto_detail'),
    path('moto/<int:pk>/add/', views.add_service, name='add_service'),
    path('add-moto/', views.add_motorcycle, name='add_moto'),
]
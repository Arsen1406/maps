from django.urls import path

from yandex_map import views

urlpatterns = [
    path('', views.YandexMap.as_view(), name='index'),
]

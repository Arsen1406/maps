# maps
## Тестовое задание

Это тестовое задание.
На данном сервисе есть 1 эндпоинт:
- http://127.0.0.1:8000/


## Функционал проекта
На странице по адресу `http://127.0.0.1:8000/` есть 3 поля для ввода
- Широта
- Долгота
- Увеличение
Необходимо заполнить все параметры и тогда появятсязначения tile фрагмент карты
Так же появится кнопка, которая приведет Вас на карту Яндекс с заданными координатами.

## Технологии
- Python
- Django
- HTML
- CSS

## Системные требования

| Процессор  | ОЗУ  | Память |
| :------------ |:---------------:| -----:|
| 4 ядра      | 4 GB | 8 GB |
                
----

## Запуск проекта
Для запуска проекта на своей машине:
Клонируйте его на свой компьютер

`git clone <ssh ссылка на проект>`

Перейдите в папку с файлом с проектом

`cd maps`

Создайте виртуальное окружение и активируйте его

`python -m venv venv`

`source venv/bin/activate`

Перейдите в дирректорию с бекэндом приложения, обновите pip и установите зависимости
```
cd maps/
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Затем запустите проект:
```
python manage.py runserver
```

## Запуск проекта через docker

Перейдите в дирректорию /maps, там выполните комманду:

```
sudo docker compose up --build 
```

## Автор
Григорян Арсен
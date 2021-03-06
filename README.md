# where_to_go

Сайт-интерактивная карта с самыми интересными местами Москвы для посещения.
Представляет собой карту Москвы, на которой отмечены интересные места. При
щелчке на конкретное место открываются подробности и фотографии.

[Демо-версия сайта](http://fdrov.pythonanywhere.com/) (доступно до 28.09.2021).

![главная страница](https://github.com/fdrov/where_to_go/blob/master/screenshots/main_page.png)

## Как запустить

Для запуска сайта вам понадобится Python 3.8+ версии. Скачайте код с GitHub.
Затем установите зависимости

```sh
pip install -r requirements.txt
```

Проведите миграции

```shell
python3 manage.py migrate
```

Запустите сервер

```sh
python3 manage.py runserver
```

Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Переменные окружения

Создайте .env файл по шаблону .env.template и заполните вашими данными.

## Заполняем базу данных тестовыми данными

Добавьте через административную панель несколько локаций. Или воспользуйтесь
**менеджмент-командой**:

```sh
python manage.py load_place url
```

, где `url` - адрес json файла в формате  **http://адрес/файла.json**. Можно
указать несколько через пробел `url1 url2 ... url_n`.
[Примеры файлов](https://github.com/devmanorg/where-to-go-places/tree/master/places)

## Возможности админки

- добавлять локации (описание, координаты)
- добавлять и сортировать фотографии
- редактор текста WYSIWYG

### Разное

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде
* Код написан в учебных целях [Devman](https://dvmn.org/)
* Тестовые данные взяты с сайта [KudaGo](https://kudago.com/)
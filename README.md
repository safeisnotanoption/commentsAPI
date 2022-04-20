# commentsAPI
REST API для системы комментариев блога

# Сборка и запуск
1. Скачать проект, установить необходимые библиотеки
```
pip install -r requirements.txt
```
2. Произвести миграцию 
```
python manage.py makemigrations commentsapi
python manage.py migrate
```
3. Запустить проект
```
python manage.py runserver
```

# Методы API
**articles/** - получить список статей/добавить статью
**articles/<int:pk>/** - получить определённую статью по id
**articles/<int:article_id>/comments/** - получить все комментарии к статье вплоть до 3 уровня вложенности/добавить комментарий к статье
**articles/<int:article_id>/comments/<int:pk>/** - получить определённый комментарий по id
**articles/<int:article_id>/comments/<int:pk>/get_children** - получить все вложенные комментарии для комментария 3 уровня.

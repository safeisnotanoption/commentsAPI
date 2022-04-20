# commentsAPI
REST API для системы комментариев блога

# Сборка и запуск
1. Установить необходимые библиотеки
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
`articles/` - получить список статей/добавить статью

`articles/<article_id>/` - получить определенную статью по id

`articles/<article_id>/comments/` - получить все комментарии к статье вплоть до 3 уровня вложенности/добавить комментарий к статье

`articles/<article_id>/comments/<comment_id>/` - получить определенный комментарий по id

`articles/<article_id>/comments/<comment_id>/get_children` - получить все вложенные комментарии для комментария 3 уровня.

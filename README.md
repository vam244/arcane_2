

<h3 align="center">Qriosity 2.0</h3>


> For running it locally use

```sh
python local.py runserver
```

> instead of

```sh
python manage.py runserver
```
changed made by vamsi:
start instructions:
1. comment out import urls quiz.urls
#url(r'^algo/questions/(?P<pk>.*)/$',views.showanswer,name='showanswer')
and also comment out
# from django.conf.urls import url,include
2. run 'python local.py makemigrations' and python local.py migrate
3. run all pyhton comands with local.py instead of manage.py
4.changed the end time in quiz.views to restart the game otherwise it will show game is closed.
5. go to admin panel by using this 'http://127.0.0.1:8000/harrypotter/user' as url and crete a player.
6. create a super user in django admin by python local.py createsuperuser command


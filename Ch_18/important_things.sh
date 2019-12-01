
# venv

# *nix
learning_log$ source ll_env/bin/activate
# win
learning_log$ ll_env\Scripts\activate

(ll_env)learning_log$ deactivate

(ll_env)learning_log$ pip install Django
(ll_env)learning_log$ django-admin.py startproject learning_log .

# Создание базы данных
(ll_env)learning_log$ python manage.py migrate


# Просмотр проекта
(ll_env)learning_log$ python manage.py runserver

# Команда startapp имя_приложения приказывает Django создать инфраструктуру,
# необходимую для построения приложения.
(ll_env)learning_log$ python manage.py startapp learning_logs

# Каждый раз, когда вы захотите изменить данные, которыми управляет Learning
# Log, выполните эти три действия: внесите изменения в models.py, вызовите
# makemigrations для learning_logs и прикажите Django выполнить миграцию
# проекта (migrate).
(ll_env)learning_log$ python manage.py makemigrations learning_logs
(ll_env)learning_log$ python manage.py migrate


# Страницы на базе форм добавляются
# практически так же, как и те страницы, которые мы уже строили ранее: вы опреде-
# ляете URL, пишете функцию представления и создаете шаблон.

# Мы снова определим URL, напишем новую функцию и шаблон
# и создадим ссылку на страницу. Но сначала нужно добавить в forms.py еще один
# класс.


# Вам также придется установить ряд пакетов, упрощающих работу проектов
# Django на реальных серверах. В активной виртуальной среде введите следующие
# команды:
(ll_env)learning_log$ pip install dj-database-url
(ll_env)learning_log$ pip install dj-static
(ll_env)learning_log$ pip install static3
(ll_env)learning_log$ pip install gunicorn

:'
Обязательно вводите команды по одной, чтобы вы знали, если при установке како-
го-либо пакета возникнет проблема. Пакет dj-database-url помогает Django взаи-
модействовать с базой данных, используемой Heroku, пакеты dj-static и static3
позволяют Django правильно управлять статическими файлами, а gunicorn — сер-
вер, способный предоставлять доступ к приложениям в реальной среде. (Статиче-
ские файлы содержат стилевые правила и файлы JavaScript.)
'

:'
Heroku необходимо знать, от каких пакетов зависит наш проект, поэтому мы вос-
пользуемся pip для построения файла со списком. Оставаясь в активной виртуаль-
ной среде, введите следующую команду:
'

(ll_env)learning_log$ pip freeze > requirements.txt

# Мерджить все фиксы в мастер!!!

стр.449

heroku login
heroku ps
heroku open

#Закрепление и отправка изменений
(ll_env)learning_log$ git commit -am "Set DEBUG=False for Heroku."
(ll_env)learning_log$ git status
(ll_env)learning_log$ git push heroku master





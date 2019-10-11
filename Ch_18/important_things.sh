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




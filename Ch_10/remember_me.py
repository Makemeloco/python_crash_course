import json


def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запрашивает новое имя пользователя"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")


def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        answer = input("Hello! You are " + username + "? y/n\n")
        if answer == 'y':
            print("Welcome back, " + username + "!")
        else:
            get_new_username()


greet_user()

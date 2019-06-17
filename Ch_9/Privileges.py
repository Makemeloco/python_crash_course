class User():
    """Иницилизируем пользователя."""

    def __init__(self, first_name, last_name, age, phone):
        """Иницилизируем имя и фамилию."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = phone
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title())
        print(str(self.age) + " лет.")
        print("Номер телефона " + str(self.phone) + ".")

    def greet_user(self):
        print("Привет, " + self.first_name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges():
    """отдельный класс для свойств админа"""

    def __init__(self, privs=(
            "разрешено добавлять сообщения",
            "разрешено удалять пользователей",
            "разрешено банить пользователей")):
        """инициализируем."""
        self.privs = privs

    def show_privileges(self):
        """отображаем информацию о привилегиях админа."""
        print("The admin can: " + (', '.join(self.privs)) + ".")


class Admin(User):
    """класс, описывающий тип пользователя."""

    def __init__(self, first_name, last_name, age, phone):
        """
        Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля.
        """
        super().__init__(first_name, last_name, age, phone)
        self.privileges = Privileges()


user = Admin('emma', 'stone', 26, 89595554455)

user.describe_user()
user.greet_user()
user.privileges.show_privileges()

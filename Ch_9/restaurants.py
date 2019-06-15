class Restaurant():
    """docstring for Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Иницилизируем атрибуты имя и тип кухни"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Выводим имя и тип кухни"""
        print(self.restaurant_name.title() + " is restaraunt name.")
        print(self.cuisine_type.title() + " is cuisine type.")

    def open_restraunt(self):
        """Выводим сообщение о том, что ресторан открыт."""
        print(self.restaurant_name.title() + " is open.")

    def set_number_served(self, number):
        """задаем количество обслуженных посетителей."""
        self.number_served = number

    def increment_number_served(self, number_of_day):
        """инкременируем количество обслуженных посетителей."""
        self.number_served += number_of_day


restaraunt = Restaurant('wokie chan', 'chinese')
restaraunt2 = Restaurant('vilanella', 'italian')
restaraunt3 = Restaurant('teremok', 'russian')
restaraunt.number_served = 7
print(restaraunt.number_served)
restaraunt.number_served = 367
print(restaraunt.number_served)
restaraunt.set_number_served(2333)
print(restaraunt.number_served)
restaraunt.increment_number_served(59)
print(restaraunt.number_served)

print("The restaraunt name is " + restaraunt.restaurant_name.title() + ".")
print("The cuisine type is " + restaraunt.cuisine_type + ".")
restaraunt.describe_restaurant()
restaraunt.open_restraunt()

restaraunt2.describe_restaurant()
restaraunt3.describe_restaurant()


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


user = User('emma', 'stone', 26, 89595554455)

user.describe_user()
user.greet_user()
user.increment_login_attempts()
print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

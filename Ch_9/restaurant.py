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

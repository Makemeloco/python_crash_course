class Employee:
    """Класс представляет работника."""

    def __init__(self, first_name, second_name, salary):
        self.first_name = first_name.title()
        self.second_name = second_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Увеличивает оклад на 5000."""
        self.salary += amount

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Тесты для модуля employee.py."""

    def setUp(self):
        """Создаем экземпляр класса Employee для тестирования."""
        self.kate = Employee('kate', 'avadzheva', 34000)

    def test_give_default_raise(self):
        """Проверяем, что повышение оклада по умолчанию работает корректно."""
        self.kate.give_raise()
        self.assertEqual(self.kate.salary, 39000)

    def test_give_custom_case(self):
        """Проверяем, что кастомное повышение оклада работает корректно."""
        self.kate.give_raise(10000)
        self.assertEqual(self.kate.salary, 44000)


unittest.main()

from random import randint


class Die:
    """класс, описывающий кубик."""

    def __init__(self, sides=6):
        """Инициализируем атрибуты кубика."""

        self.sides = sides

    def roll_die(self, rolls):
        """бросок кубика"""
        for i in range(0, rolls):
            x = randint(1, self.sides)
            print(x)


six_sides_die = Die()
six_sides_die.roll_die(10)
print('\n\n\n')
ten_sides_die = Die(10)
ten_sides_die.roll_die(10)
print('\n\n\n')
twenty_sides_die = Die(20)
twenty_sides_die.roll_die(10)

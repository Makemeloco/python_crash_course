def make_shirt(shirt_size='L', shirt_text='I love Python.'):
    """Выводит информацию о футболке."""
    print("\nРазмер футболки: " + shirt_size + ".")
    print("Текст на футболке: " + shirt_text + ".")

make_shirt('L', 'Возвращаемое значение')
make_shirt(shirt_size='M', shirt_text='Возвращаемое значение')
make_shirt()

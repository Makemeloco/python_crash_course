import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# Назначение заголовка диаграммы и меток осей.
plt.title("Квадрат числа", fontsize=24)
plt.xlabel("Значение числа", fontsize=14)
plt.ylabel("Квадрат от числа", fontsize=14)

# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', labelsize=14)

plt.show()

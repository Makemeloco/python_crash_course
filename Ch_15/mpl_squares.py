import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)

# Назначение заголовка диаграммы и меток осей.
plt.title("Квадрат числа", fontsize=14)
plt.xlabel("Значение числа", fontsize=14)
plt.ylabel("Квадрат от числа", fontsize=14)

# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', labelsize=14)

plt.show()

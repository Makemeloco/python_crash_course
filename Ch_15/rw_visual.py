import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Новые блуждания строятся до тех пор,
# пока программа остается активной.
while True:
    # Построение случайного блуждания
    # и нанесение точек на диаграмму.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Темная цветовая схема.
    plt.style.use('dark_background')

    # Назначение размера области просмотра.
    plt.figure(figsize=(10, 6))

    # Генерация точек случайного блуждания.
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.viridis, edgecolor='none', s=1)

    # Выделение первой и последней точек.
    plt.scatter(0, 0, c='blue', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow',
                edgecolors='none', s=100)

    # Удаление осей.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    # Предложение сгенерировать и отобразить
    # ещё один экземпляр диаграммы (предидущий затирается).
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

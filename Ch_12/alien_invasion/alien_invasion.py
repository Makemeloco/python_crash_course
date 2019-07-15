import sys
import pygame


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    screen = pygame.set_caption("Alien Invasion")

    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


run_game()
import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    """Класс для создания звезд."""

    def __init__(self, ai_settings, screen):
        """Создает объект звезды."""
        super().__init__()
        self.screen = screen

        # Создание звезды в позиции (0,0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, ai_settings.star_width,
                                ai_settings.star_height)
        self.rect.x = randint(0, 1200)
        self.rect.y = randint(0, 800)
        self.color = ai_settings.star_color

    def draw_star(self):
        """Выводит звезды."""
        pygame.draw.rect(self.screen, self.color, self.rect)

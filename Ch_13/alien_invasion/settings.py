class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 26)

        # Настройки корабля.
        self.ship_speed_factor = 1.5

        # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 0
        self.bullets_allowed = 3

        # Параметры звезды
        self.star_width = 1
        self.star_height = 1
        self.star_color = 255, 255, 153
        self.stars_allowed = 100

        # Настройки пришельцев.
        self.alien_speed_factor = 1

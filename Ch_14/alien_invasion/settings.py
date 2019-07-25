class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 26)

        # Настройки корабля.
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Параметры пули
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 30
        self.bullet_color = 0, 255, 204
        self.bullets_allowed = 3

        # Параметры звезды
        self.star_width = 1
        self.star_height = 1
        self.star_color = 255, 255, 153
        self.stars_allowed = 100

        # Настройки пришельцев.
        self.alien_speed_factor = 1.5
        self.fleet_drop_speed = 5
        # fleet_direction = 1 обозначает движение вправо; а -1 - влева.
        self.fleet_direction = 1

        # Темп ускорения игры.
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

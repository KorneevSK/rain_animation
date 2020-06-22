class Settings():
    """Класс для хранения всех настроек игры"""
    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1080
        self.screen_height = 560
        self.bg_color = (146, 169, 250)

        self.drop_speed_factor = 1
        self.rain_drop_factor = 10
        self.rain_direction = 1  # 1 - вправо, -1 - влево
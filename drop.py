import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
    """Представление одной капли"""
    def __init__(self, ai_settings, screen):
        """Инициализация капли и задание начальной позиции"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения капли и назначение атрибута rect
        self.image = pygame.image.load('drop.bmp')
        self.rect = self.image.get_rect()

        # Каждая новая капля появляется в верхнем левом углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной позиции капли
        self.x = float(self.rect.x)
        # self.y = float(self.rect.y)

    def update(self):
        """Перемещает каплю вниз"""
        self.rect.y += self.ai_settings.drop_speed_factor
        # self.rect.y = self.y

    def check_edges(self):
        """Возвращает True, если капля находится у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True

    def blitme(self):
        """Выводит каплю в текущем положении"""
        self.screen.blit(self.image, self.rect)
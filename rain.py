import pygame
from settings import Settings
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # Инициализация игры и создание объекта экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Rain")
    # Создание группы капель
    drops = Group()
    gf.create_rain(ai_settings, screen, drops)
    drops_max = len(drops.copy())

    # Запуск основного цикла игры
    while True:
        gf.check_events()
        gf.update_drops(ai_settings, screen, drops, drops_max)
        gf.update_screen(ai_settings, screen, drops)


run_game()
import sys
import pygame
from drop import Drop

def check_keydown_events(event):
    """Обработка нажатия клавиш"""
    if event.key == pygame.K_q:
        sys.exit()

def check_events():
    """Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)

def update_screen(ai_settings, screen, drops):
    """Обновляет изображения на экране и отображает новый экран"""
    # При каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    # Все пули выводятся позади изображений корабля и пришельцев
    drops.draw(screen)
    # Отображение последнего прорисованного окна
    pygame.display.flip()

def get_number_drops(ai_settings, drop_width):
    """Вычисляет количества капель в ряду"""
    # Интервал между соседними каплями равен одной ширине капли
    available_space_x = ai_settings.screen_width - (drop_width)
    number_drops_x = int(available_space_x / (2 * drop_width))
    return number_drops_x

def get_number_rows(ai_settings, drop_height):
    """Определяет количество рядов, помещающихся на экране"""
    available_space_y = (ai_settings.screen_height - (drop_height))
    number_rows = int(available_space_y / (2 * drop_height))
    return number_rows

def create_drop(ai_settings, screen, drops, drop_number, row_number):
    """Создание капли и размещение её в ряду"""
    drop = Drop(ai_settings, screen)
    drop_width = drop.rect.width
    drop.x = drop_width + 2 * drop_width * drop_number
    drop.rect.x = drop.x
    drop.rect.y = drop.rect.height + 2 * drop.rect.height * row_number
    drops.add(drop)

def create_rain(ai_settings, screen, drops):
    """Создаёт дождь капель"""
    # Создание капли и вычисление количества капель в ряду
    drop = Drop(ai_settings, screen)
    number_drops_x = get_number_drops(ai_settings, drop.rect.width)
    number_rows = get_number_rows(ai_settings, drop.rect.height)
    # Создание капель
    for row_number in range(number_rows):
        for drop_number in range(number_drops_x):
            create_drop(ai_settings, screen, drops, drop_number, row_number)

def check_rain_edges(ai_settings, screen, drops):
    """Реагирует на достижения каплей края экрана"""
    for drop in drops.sprites():
        if drop.check_edges():
            create_row_drops(ai_settings, screen, drops, 1)
            break

def create_row_drops(ai_settings, screen, drops, row_number):
    drop = Drop(ai_settings, screen)
    number_drops_x = get_number_drops(ai_settings, drop.rect.width)
    for drop_number in range(number_drops_x):
        drop = Drop(ai_settings, screen)
        drop_width = drop.rect.width
        drop.x = drop_width + 2 * drop_width * drop_number
        drop.rect.x = drop.x
        drop.rect.y = 0
        drops.add(drop)


def update_drops(ai_settings, screen, drops, drops_max):
    """Проверяет, достиг ли дождь края экрана, после чего обновляет позиции всех капель на экране"""
    drops.update()
    for drop in drops.copy():
        if drop.rect.top >= ai_settings.screen_height:
            drops.remove(drop)
    if drops_max == len(drops.copy()):
        pass
    else:
        check_rain_edges(ai_settings, screen, drops)
    print(len(drops.copy()))
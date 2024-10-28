import pygame as pg
import math
import game
import show_animation

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800


def show_menu():
    pg.init()
    display = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    while True:
        display.fill((0, 0, 0))  # Чёрный фон для меню
        font = pg.font.Font(None, 74)
        title = font.render("Меню", True, (255, 255, 255))
        play_button = font.render("Играть в игру", True, (255, 255, 255))
        animation_button = font.render("Смотреть анимацию", True, (255, 255, 255))
        exit_button = font.render("Выход", True, (255, 255, 255))

        display.blit(title, (DISPLAY_WIDTH // 2 - title.get_width() // 2, 50))
        display.blit(play_button, (DISPLAY_WIDTH // 2 - play_button.get_width() // 2, 150))
        display.blit(animation_button, (DISPLAY_WIDTH // 2 - animation_button.get_width() // 2, 250))
        display.blit(exit_button, (DISPLAY_WIDTH // 2 - exit_button.get_width() // 2, 350))

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:  # Играть в игру
                    return "play"
                elif event.key == pg.K_2:  # Смотреть анимацию
                    return "animation"
                elif event.key == pg.K_3:  # Выход
                    pg.quit()
                    exit()
    pg.quit()

# Показ меню
choice = show_menu()

# Игровой цикл (если выбрана игра)
if choice == "play":
    game.play_game()

# Показ анимации (если выбрана анимация)
elif choice == "animation":
    show_animation.show_animation()

pg.quit()

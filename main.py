import pygame as pg
import math
import game
import show_animation

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 450
K_ENTER = 13
FPS = 60


def show_menu():
    pg.init()
    display = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pg.display.set_caption('Плывущая лодочка')
    running = True
    clock = pg.time.Clock()
    current_choise = 2
    while running:
        clock.tick(FPS)
        modes = ['game', 'animation', 'exit']
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == K_ENTER:
                return modes[current_choise]
            if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                current_choise = (current_choise + 1) % 3
            if event.type == pg.KEYDOWN and event.key == pg.K_UP:
                if current_choise > 0:
                    current_choise = (current_choise - 1) % 3
                else:
                    current_choise = 2
            display.fill((0, 0, 0))  # Чёрный фон для меню
            big_font = pg.font.Font(None, 100)
            regular_font = pg.font.Font(None, 74)
            title = big_font.render("Меню", True, (255, 255, 255))
            if current_choise == 0:
                play_button = regular_font.render("Играть в игру", True, (128, 166, 255))
            else:
                play_button = regular_font.render("Играть в игру", True, (255, 255, 255))
            if current_choise == 1:
                animation_button = regular_font.render("Смотреть анимацию", True, (128, 166, 255))
            else:
                animation_button = regular_font.render("Смотреть анимацию", True, (255, 255, 255))
            if current_choise == 2:
                exit_button = regular_font.render("Выход", True, (128, 166, 255))
            else:
                exit_button = regular_font.render("Выход", True, (255, 255, 255))
            
            display.blit(title, (DISPLAY_WIDTH // 2 - title.get_width() // 2, 50))
            display.blit(play_button, (50, 150))
            display.blit(animation_button, (50, 210))
            display.blit(exit_button, (50, 270))

            pg.display.update()
            if event.type == pg.QUIT:
                pg.quit()
                exit()
    pg.quit()

# Показ меню
while True:
    choice = show_menu()
    # Игровой цикл (если выбрана игра)
    if choice == "game":
        game.play_game()
    # Показ анимации (если выбрана анимация)
    elif choice == "animation":
        show_animation.show_animation()
    elif choice == "exit":
        pg.quit()
        exit()

import pygame as pg
import math

pg.init()
display = pg.display.set_mode((int(1280 / 2), int(914 / 2)))
display_width = int(1280 / 2)
display_height = int(914 / 2)
pg.display.set_caption("Лабораторная работа №5")
background_image = pg.image.load("backround_image.jpg")
background_image = pg.transform.scale(background_image, (int(1280 / 2), int(914 / 2)))

def move_ship(ship, display_width):
    if ship.rect.x + int(454 / 3) <= 0:
        ship.rect.x = display_width
    ship.rect = ship.rect.move(-1, 0)

def drop_the_star(star, start_x, start_y, x0, y0, alpha):
    star.rect.x = int((start_x - x0) * math.cos(math.radians(alpha)) - (start_y - y0) * math.sin(math.radians(alpha))) + x0
    star.rect.y = int((start_x - x0) * math.sin(math.radians(alpha)) + (start_y - y0) * math.cos(math.radians(alpha))) + y0

def show_menu():
    while True:
        display.fill((0, 0, 0))  # Чёрный фон для меню^M
        font = pg.font.Font(None, 74)
        title = font.render("Меню", True, (255, 255, 255))
        play_button = font.render("Играть в игру", True, (255, 255, 255))
        animation_button = font.render("Смотреть анимацию", True, (255, 255, 255))
        exit_button = font.render("Выход", True, (255, 255, 255))

        display.blit(title, (display_width // 2 - title.get_width() // 2, 50))
        display.blit(play_button, (display_width // 2 - play_button.get_width() // 2, 150))
        display.blit(animation_button, (display_width // 2 - animation_button.get_width() // 2, 250))
        display.blit(exit_button, (display_width // 2 - exit_button.get_width() // 2, 350))

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

def play_game():
    pass

def show_animation():
    # Загрузка картинки корабля
    ship_image = pg.image.load("./ship_454_487.png")
    ship_image = pg.transform.scale(ship_image, (int(454 / 3), int(487 / 3)))
    sprites = pg.sprite.Group()

    # Создание спрайта звезды
    star = pg.sprite.Sprite()
    star_cnv = pg.Surface((10, 10))
    star_cnv.fill("#502169")
    pg.draw.circle(star_cnv, "#ffff00", (5, 5), 2)
    star.image = star_cnv
    star.rect = star.image.get_rect()
    sprites.add(star)
    star.rect.x = 505
    star.rect.y = 2

    # Создание спрайта корабля
    ship = pg.sprite.Sprite()
    ship.image = ship_image
    ship.rect = ship.image.get_rect()
    sprites.add(ship)
    ship.rect.x = display_width
    ship.rect.y = display_height - 330

    # Музыка на фон
    pg.mixer.music.load("background_sound.mp3")
    pg.mixer.music.play()

    game_end = False
    alpha = 0
    while not game_end:
        alpha += 0.0625
        if alpha > 50:
            alpha = 0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_end = True
        move_ship(ship, display_width)
        drop_the_star(star, 505, 2, 481, 193, alpha)
        display.blit(background_image, (0, 0))
        sprites.draw(display)
        pg.display.update()
        pg.time.delay(10)



# Показ меню
choice = show_menu()

# Игровой цикл (если выбрана игра)
if choice == "play":
    play_game()

# Показ анимации (если выбрана анимация)
elif choice == "animation":
    show_animation()

pg.quit()


import pygame as pg
import math

def move_ship(ship, display_width):
    if ship.rect.x + int(454 / 3) <= 0:
        ship.rect.x = display_width
    ship.rect = ship.rect.move(-1, 0)

def drop_the_star(star,start_x, start_y, x0, y0, alpha):
    star.rect.x = int((start_x - x0) * math.cos(math.radians(alpha)) - (start_y - y0) * math.sin(math.radians(alpha))) + x0
    star.rect.y = int((start_x - x0) * math.sin(math.radians(alpha)) + (start_y - y0) * math.cos(math.radians(alpha))) + y0
    
pg.init()
display = pg.display.set_mode((int(1280 / 2), int(914 / 2)))
# Получения размеров окна
display_width = int(1280 / 2)
display_height = int(914 / 2)
pg.display.set_caption("Лабораторная работа №5")

# Загрузка фонового изображения
background_image = pg.image.load("backround_image.jpg")
background_image = pg.transform.scale(background_image, (int(1280 / 2), int(914 / 2)))

# Прикрипление фонового изображения
display.blit(background_image, (0, 0))
pg.display.update()

# Загружаем картинку корабля
ship_image = pg.image.load("./ship_454_487.png")
ship_image = pg.transform.scale(ship_image, (int(454 / 3), int(487 / 3)))
# Получаем все спрайты
sprites = pg.sprite.Group()

# Создадим спрайт звезды
star = pg.sprite.Sprite()
star_cnv = pg.Surface((10, 10))
star_cnv.fill("#502169")
pg.draw.circle(star_cnv, "#ffff00", (5, 5), 2)
star.image = star_cnv
star.rect = star.image.get_rect()
sprites.add(star)
star.rect.x = 505
star.rect.y = 2

# Создадим спрайт корабля
ship = pg.sprite.Sprite()
ship.image = ship_image
ship.rect = ship.image.get_rect()
sprites.add(ship)
ship.rect.x = display_width
ship.rect.y = display_height - 330

# Добавлление успокаивающей музыки на фон
pg.mixer.music.load("background_sound.mp3")
pg.mixer.music.play()

# Игровой цикл
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

    
pg.quit()

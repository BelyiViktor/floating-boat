import pygame as pg
import random

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
SHIP_SPEED = 1
BULLET_SPEED = 20
MONSTER_SPEED = 2

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Класс для корабля
class Ship(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./resources/images/ship_454_487.png")
        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - 100
        self.rect.y = SCREEN_HEIGHT // 2

    def update(self, move_left):
        # Движение корабля вверх и вниз
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and self.rect.y > 0:
            self.rect.y -= 2 * SHIP_SPEED
        if keys[pg.K_DOWN] and self.rect.y < SCREEN_HEIGHT - self.rect.height:
            self.rect.y += 2 * SHIP_SPEED

        # Движение влево с увеличенной скоростью
        if move_left:
            self.rect.x -= SHIP_SPEED + 2  # Увеличиваем скорость при движении влево
        else:
            self.rect.x -= SHIP_SPEED  # Течение несет корабль

# Класс для снаряда
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((10, 5))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= BULLET_SPEED
        if self.rect.x < 0:
            self.kill()  # Удалить снаряд, если он вышел за экран

# Класс для монстра
class Monster(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./resources/images/octopus.png")
        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randint(0, SCREEN_HEIGHT)

    def update(self):
        self.rect.x += MONSTER_SPEED
        if self.rect.x < 0:
            self.kill()  # Удалить, если выходит за экран

# Класс для камня
class Rock(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./resources/images/rock.png")
        self.image = pg.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randint(50, SCREEN_HEIGHT)

    def update(self):
        self.rect.x += MONSTER_SPEED  # Двигаем камень с той же скоростью, что и монстра
        if self.rect.x < 0:
            self.kill()  # Удалить, если выходит за экран

# Функция для отображения текста
def show_message(pg, display, text, color, size):
    font = pg.font.Font(None, size)
    message = font.render(text, True, color)
    display.blit(message, (SCREEN_WIDTH // 2 - message.get_width() // 2, SCREEN_HEIGHT // 2 - message.get_height() // 2))
    pg.display.update()
    pg.time.delay(2000)  # Задержка для отображения сообщения

def play_game():
    # Основная программа
    pg.init()
    display = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Кораблик против моря")
    clock = pg.time.Clock()

    # Группы спрайтов
    all_enemy_sprites = pg.sprite.Group()
    bullets = pg.sprite.Group()
    monsters = pg.sprite.Group()
    rocks = pg.sprite.Group()

    # Создаем корабль
    group_for_ship = pg.sprite.Group()
    ship = Ship()
    group_for_ship.add(ship)

    # Игровой цикл
    running = True
    game_over = False

    while running:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and not game_over:  # Выстрел
                    bullet = Bullet(ship.rect.x, ship.rect.y + 50)
                    all_enemy_sprites.add(bullet)
                    bullets.add(bullet)

        move_left = pg.key.get_pressed()[pg.K_LEFT]  # Проверка, нажата ли клавиша влево

        if not game_over:
            all_enemy_sprites.update()
            ship.update(move_left=move_left)

            # Создание монстров и камней
            if random.random() < 0.005:  # 1% шанс создать монстра
                monster = Monster()
                all_enemy_sprites.add(monster)
                monsters.add(monster)
            
            if random.random() < 0.005:  # 2% шанс создать камень
                rock = Rock()
                all_enemy_sprites.add(rock)
                rocks.add(rock)

            # Проверка на столкновения
            for bullet in bullets:
                hit_monsters = pg.sprite.spritecollide(bullet, monsters, True)
                if hit_monsters:
                    bullet.kill()

            hit_rocks = pg.sprite.spritecollide(ship, rocks, False)
            hit_monsters = pg.sprite.spritecollide(ship, monsters, False)

            # Проверка на поражение
            if hit_rocks or hit_monsters:
                print('Code was here')
                game_over = True
                running = False

            # Проверка на победу
            if ship.rect.x < 0:
                show_message(pg, display, "Вы победили!", WHITE, 50)
                exit()

        # Отображение
        display.fill(BLUE)  # Фон моря
        all_enemy_sprites.draw(display)
        group_for_ship.draw(display)
        pg.display.flip()
    
    if game_over:
        show_message(pg, display, "Игра окончена: вы проиграли!", WHITE, 50)
    exit()


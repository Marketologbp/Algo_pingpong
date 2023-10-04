from pygame import *

init()
size = [700, 500]
main_window = display.set_mode(size)
display.set_caption('Пинг Понг')


class GameSprite(sprite.Sprite):
    def __init__(self, player, width, height, sprite_picture, sprite_speed_x, sprite_speed_y, sprite_x, sprite_y):
        super().__init__()
        self.player = player
        self.sprite_picture = transform.scale(image.load(sprite_picture), (width, height))
        self.sprite_speed_x = sprite_speed_x
        self.sprite_speed_y = sprite_speed_y
        self.rect = self.sprite_picture.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y

        def show_sprite(self):
            main_window.blit(self.sprite_picture, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        buttons_pressed = key.get_pressed()

        if buttons_pressed[K_UP] and self.rect.y != 0:
            self.rect.y -= self.sprite_speed
        if buttons_pressed[K_DOWN] and self.rect.y != 440:
            self.rect.y += self.sprite_speed
        if buttons_pressed[K_LEFT] and self.rect.x != 0:
            self.rect.x -= self.sprite_speed
        if buttons_pressed[K_RIGHT] and self.rect.x != 640:
            self.rect.x += self.sprite_speed


class Enemy(GameSprite):
    def moving(self):
        if self.rect.x >= 640 or self.rect.x <= 440:
            self.sprite_speed *= -1
        self.rect.x += self.sprite_speed
        if self.player == '1':
            if buttons_pressed[K_w] and self.rect.y >= 0:
                self.rect.y -= self.sprite_speed_y
            if buttons_pressed[K_s] and self.rect.y <= 440:
                self.rect.y += self.sprite_speed_y
        elif self.player == '2':
            if buttons_pressed[K_UP] and self.rect.y >= 0:
                self.rect.y -= self.sprite_speed_y
            if buttons_pressed[K_DOWN] and self.rect.y <= 440:
                self.rect.y += self.sprite_speed_y
        else:
            pass


class Ball(GameSprite):
    def update(self):
        if self.rect.y <= 0 or self.rect.y >= 440:
            self.sprite_speed_y *= -1
        self.rect.y += self.sprite_speed_y


background = transform.scale(image.load('background.jpg'), size)
player_1 = Player('1', 60, 60, 'blue_racket.png', 0, 10, 0, 250)
player_2 = Player('2', 60, 60, 'red_racket.png', 0, 10, 640, 250)
ball = Ball(' ', 60, 60, 'ball.png', 10, 10, 300, 300)

font.init()
font = font.Font(None, 70)

clock = time.Clock()
FPS = 60

game_exit = True
finish_level = False
finish_game = False

while game_exit:
    for game_event in event.get():
        if game_event.type == QUIT:
            game_exit = False

    player_1.update()
    player_2.update()
    ball.update()

    main_window.blit(background, (0, 0))
    player_1.show_sprite()
    player_2.show_sprite()
    ball.show_sprite()

    display.update()
    clock.tick(FPS)
    clock.tick(FPS)
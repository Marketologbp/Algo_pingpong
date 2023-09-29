from pygame import *

size = [700, 500]
main_window = display.set_mode(size)
display.set_caption('Пинг Понг')

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_picture, sprite_speed, sprite_x, sprite_y):
        super().__init__()
        self.sprite_picture = transform.scale(image.load(sprite_picture), (60, 60))
        self.sprite_speed = sprite_speed
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


background = transform.scale(image.load('background.jpg'), size)

font.init()
font = font.Font(None, 70)

clock = time.Clock()
FPS = 60

game_exit = True
finish_level = False

while game_exit:
    for game_event in event.get():
        if game_event.type == QUIT:
            game_exit = False

    main_window.blit(background, (0, 0))

    display.update()
    clock.tick(FPS)
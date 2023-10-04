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
        self.rect.y += self.sprite_speed_y
        self.rect.x += self.sprite_speed_x
        if self.rect.y <= 0 or self.rect.y >= 440:
            self.sprite_speed_y *= -1


background = transform.scale(image.load('background.jpg'), size)
player_1 = Player('1', 60, 60, 'blue_racket.png', 0, 10, 0, 250)
player_2 = Player('2', 60, 60, 'red_racket.png', 0, 10, 640, 250)
ball = Ball(' ', 60, 60, 'ball.png', 1, 1, 300, 300)

font.init()
font = font.Font(None, 70)
font_win_1 = font.render('Player 1 win!', True, (0, 0, 255))
font_win_2 = font.render('Player 2 win!', True, (255, 0, 0))

clock = time.Clock()
FPS = 60

game_exit = True
finish_game = True

while game_exit:
    for game_event in event.get():
        if game_event.type == QUIT:
            game_exit = False

    if finish_game:
        player_1.update()
        player_2.update()
        ball.update()

        main_window.blit(background, (0, 0))
        player_1.show_sprite()
        player_2.show_sprite()
        ball.show_sprite()

        if sprite.collide_rect(ball, player_1) or  sprite.collide_rect(ball, player_2):
            ball.sprite_speed_x *= -1

        if ball.rect.x >= 760:
            main_window.blit(font_win_1, (200, 200))
            finish_game = False
        if ball.rect.x <= -60:
            main_window.blit(font_win_2, (200, 200))
            finish_game = False

        display.update()
        clock.tick(FPS)

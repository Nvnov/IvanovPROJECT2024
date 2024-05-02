import pygame
pygame.init()
W = 1280
H = 720
screen = pygame.display.set_mode((W, H))

#Вступительный фон


bg_sound1 = pygame.mixer.Sound('sounds/Вступление.mp3')
bg_sound2 = pygame.mixer.Sound('sounds/Фон звук.mp3')
bg_sound1.set_volume(0.05)
bg_sound2.set_volume(0.05)
mouse = pygame.image.load('images/MOUSE.png').convert_alpha()

icon = pygame.image.load('images/icon_gorilla.png').convert_alpha()

font ='FONTS/8-bit Arcade In.ttf'
font_large = pygame.font.Font(font, 100)
font_small = pygame.font.Font(font, 50)


player_jump = [
    pygame.image.load('images/Player JUMP/JUMP LEFT.png').convert_alpha(),
    pygame.image.load('images/Player JUMP/JUMP RIGHT.png').convert_alpha()
    ]
player_IDLE = [
    pygame.image.load('images/Player IDLE/idle 1-1.png').convert_alpha(),
    pygame.image.load('images/Player IDLE/idle 1-2.png').convert_alpha(),
    pygame.image.load('images/Player IDLE/idle 1-3.png').convert_alpha(),
    pygame.image.load('images/Player IDLE/idle 1-4.png').convert_alpha()
]
player_win = [
    pygame.image.load('images/Player WIN/WIN IDLE 1.png').convert_alpha(),
    pygame.image.load('images/Player WIN/WIN IDLE 2.png').convert_alpha(),
    pygame.image.load('images/Player WIN/WIN IDLE 3.png').convert_alpha()
]
player_walk_right = [
    pygame.image.load('images/Player Walk Right/Right 1.png').convert_alpha(),
    pygame.image.load('images/Player Walk Right/Right 2.png').convert_alpha(),
    pygame.image.load('images/Player Walk Right/Right 3.png').convert_alpha(),
    pygame.image.load('images/Player Walk Right/Right 4.png').convert_alpha(),
    pygame.image.load('images/Player Walk Right/Right 5.png').convert_alpha(),
    pygame.image.load('images/Player Walk Right/Right 6.png').convert_alpha(),
    pygame.image.load('images/Player Walk Right/Right 7.png').convert_alpha(),
    pygame.image.load('images/Player Walk Right/Right 8.png').convert_alpha()
]
player_walk_left = [
    pygame.image.load('images/Player Walk Left/Left 1.png').convert_alpha(),
    pygame.image.load('images/Player Walk Left/Left 2.png').convert_alpha(),
    pygame.image.load('images/Player Walk Left/Left 3.png').convert_alpha(),
    pygame.image.load('images/Player Walk Left/Left 4.png').convert_alpha(),
    pygame.image.load('images/Player Walk Left/Left 5.png').convert_alpha(),
    pygame.image.load('images/Player Walk Left/Left 6.png').convert_alpha(),
    pygame.image.load('images/Player Walk Left/Left 7.png').convert_alpha(),
    pygame.image.load('images/Player Walk Left/Left 8.png').convert_alpha()
]
MenuBG = pygame.image.load('images/MENU1280.png').convert_alpha()
SettingsBG = pygame.image.load('images/SETTINGS.png').convert_alpha()
VideoBG = pygame.image.load('images/VIDEO.png').convert_alpha()
GameBG = pygame.image.load('images/GameBG.png').convert_alpha()

StartMenu = pygame.image.load('images/STARTMENU.png').convert_alpha()
#Земля
ground_image = pygame.image.load('images/Ground.png')
GROUND_H = ground_image.get_height()

enemy_dead_image = pygame.image.load('images/enemy/DEAD ENEMY RIGHT.png').convert_alpha()
enemy_dead_image = pygame.transform.scale(enemy_dead_image, (200, 50))

#Враг
enemy_dead_image = pygame.image.load('images/enemy/DEAD ENEMY LEFT.png').convert_alpha()
enemy_dead_image = pygame.transform.scale(enemy_dead_image, (200, 50))

#Враг
enemy_image = pygame.image.load('images/enemy/ENEMY RIGHT.png').convert_alpha()
enemy_image = pygame.transform.scale(enemy_image, (200, 100))

player_dead_image = pygame.image.load('images/Player DEAD/Player DEAD.png').convert_alpha()
player_dead_image = pygame.transform.scale(player_dead_image, (180, 222))

#Игрок
player_image = pygame.image.load('images/Player/Player.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (180, 222))

FPS = 60

class Entity:



    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = 5
        self.x_speed = 0
        self.y_speed = 0
        self.is_out = False
        self.is_dead = False
        self.jump_speed = -9
        self.gravity = 0.3
        self.is_grounded = False

    def handle_input(self):
        pass

    def kill(self, dead_image):
        self.image = dead_image
        self.is_dead = True
        self.x_speed = -self.x_speed
        self.y_speed = self.jump_speed


    def update(self):
        self.rect.x += self.x_speed
        self.y_speed += self.gravity
        self.rect.y += self.y_speed

        if self.is_dead:
            if self.rect.top > H - GROUND_H:
                self.is_grounded = True
        else:
            self.handle_input()

            if self.rect.bottom > H - GROUND_H:
                self.is_grounded = True
                self.y_speed = 0
                self.rect.bottom = H - GROUND_H

    def draw(self, surface):
        surface.blit(self.image, self.rect)



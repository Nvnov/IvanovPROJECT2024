import pygame
from Entity import Entity

W = 1280
H = 720
screen = pygame.display.set_mode((W, H))

ground_image = pygame.image.load('images/Ground.png')
GROUND_H = ground_image.get_height()
StartMenu = pygame.image.load('images/STARTMENU.png').convert_alpha()
StartMenu = pygame.transform.scale(StartMenu, (0, 0))
StartMenu_x = 0

enemy_dead_image = pygame.image.load('images/enemy/DEAD ENEMY RIGHT.png').convert_alpha()
enemy_dead_image = pygame.transform.scale(enemy_dead_image, (200, 50))

#Враг
enemy_dead_image = pygame.image.load('images/enemy/DEAD ENEMY LEFT.png').convert_alpha()
enemy_dead_image = pygame.transform.scale(enemy_dead_image, (200, 50))

#Враг
enemy_image = pygame.image.load('images/enemy/ENEMY RIGHT.png').convert_alpha()
enemy_image = pygame.transform.scale(enemy_image, (200, 100))

player_jump = [
    pygame.image.load('images/Player JUMP/JUMP LEFT.png').convert_alpha(),
    pygame.image.load('images/Player JUMP/JUMP RIGHT.png').convert_alpha()
    ]
player_idle = [
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


player_dead_image = pygame.image.load('images/Player DEAD/Player DEAD.png').convert_alpha()
player_dead_image = pygame.transform.scale(player_dead_image, (180, 222))

#Игрок
player_image = pygame.image.load('images/Player/Player.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (180, 222))


class Player(Entity):
    def __init__(self):
        super().__init__(player_image)
        self.respawn()


    def handle_input(self):
        self.x_speed = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x_speed = -self.speed
        elif keys[pygame.K_d]:
            self.x_speed = self.speed

        if self.is_grounded and keys[pygame.K_w]:
            self.is_grounded = False
            self.jump()

    def respawn(self):
        self.is_out = False
        self.is_dead = False
        self.rect.midbottom = (W // 2, H - GROUND_H)

    def jump(self):
        self.y_speed = self.jump_speed


    def killing(self):
        self.y_speed = self.jump_speed


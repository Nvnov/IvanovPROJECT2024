import pygame
from Entity import Entity

W = 1280
H = 720
screen = pygame.display.set_mode((W, H))

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

player_dead_image = pygame.image.load('images/Player/DEAD PLAYER 2.png').convert_alpha()
player_dead_image = pygame.transform.scale(player_dead_image, (180, 222))

#Игрок
player_image = pygame.image.load('images/Player/Player 2.png').convert_alpha()
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


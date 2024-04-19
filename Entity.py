import pygame

W = 1280
H = 720
screen = pygame.display.set_mode((W, H))

#Вступительный фон
OpenBG = pygame.image.load('images/Вступительный фон 1.png').convert_alpha()
OpenBG = pygame.transform.scale(OpenBG, (0, 0))
OpenBG_x = 0

ground_image = pygame.image.load('images/Ground.png').convert_alpha()
ground_image = pygame.transform.scale(ground_image, (300, 165))
GROUND_H = ground_image.get_height()

enemy_dead_image = pygame.image.load('images/enemy/DEAD ENEMY RIGHT.png').convert_alpha()
enemy_dead_image = pygame.transform.scale(enemy_dead_image, (200, 50))

#Враг
enemy_dead_image = pygame.image.load('images/enemy/DEAD ENEMY LEFT.png').convert_alpha()
enemy_dead_image = pygame.transform.scale(enemy_dead_image, (200, 50))

#Враг
enemy_image = pygame.image.load('images/enemy/ENEMY RIGHT.png').convert_alpha()
enemy_image = pygame.transform.scale(enemy_image, (200, 100))

player_dead_image = pygame.image.load('images/Player/DEAD Player 2.png').convert_alpha()
player_dead_image = pygame.transform.scale(player_dead_image, (180, 222))

#Игрок
player_image = pygame.image.load('images/Player test R/Player 2.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (180, 222))

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



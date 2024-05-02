import pygame
from Entity import Entity, bg_sound1, bg_sound2, mouse, icon, font, font_large, font_small, player_jump, player_IDLE, player_win, player_walk_right, player_walk_left, MenuBG, SettingsBG, VideoBG, GameBG, StartMenu, player_image, player_dead_image, enemy_image, enemy_dead_image, GROUND_H, ground_image
pygame.init()
W = 1280
H = 720
screen = pygame.display.set_mode((W, H))




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


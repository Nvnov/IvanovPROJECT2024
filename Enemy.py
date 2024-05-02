import pygame
import random
from Entity import Entity, bg_sound1, bg_sound2, mouse, icon, font, font_large, font_small, player_jump, player_IDLE, player_win, player_walk_right, player_walk_left, MenuBG, SettingsBG, VideoBG, GameBG, StartMenu, player_image, player_dead_image, enemy_image, enemy_dead_image, GROUND_H, ground_image
pygame.init()

W = 1280
H = 720
screen = pygame.display.set_mode((W, H))



class Enemy(Entity):
    def __init__(self):
        super().__init__(enemy_image)
        self.spawn()

    def spawn(self):
        direction = random.randint(0, 1)

        if direction == 0:
            self.x_speed = self.speed
            self.rect.bottomright = (0, 0)
        else:
            self.x_speed = -self.speed
            self.rect.bottomleft = (W, 0)

    def update(self):
        super().update()
        if self.x_speed > 0 and self.rect.left > W or self.x_speed < 0 and self.rect.right < 0:
            self.is_out = True
import pygame, sys, threading, Entity, random
from Entity import Entity
from Player import Player
from Enemy import Enemy
from Loading import LoadingScreen
from buttons import Buttons
pygame.init()


W = 1280
H = 720
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption('Gorilla: The Legacy of the Berserker')
icon = pygame.image.load('images/icon_gorilla.png').convert_alpha()
pygame.display.set_icon(icon)

#Музыка
bg_sound1 = pygame.mixer.Sound('sounds/Вступление.mp3')
bg_sound2 = pygame.mixer.Sound('sounds/Фон звук.mp3')
bg_sound1.set_volume(0.05)
bg_sound2.set_volume(0.05)


FPS = 60
clock = pygame.time.Clock()



font_path ='FONTS/8-bit Arcade In.ttf'
font_large = pygame.font.Font(font_path, 100)
font_small = pygame.font.Font(font_path, 50)


game_over = False
retry_text = font_small.render('---PRESS ANY KEY---', True, (255, 255, 255))
retry_rect = retry_text.get_rect()
retry_rect.midtop = (W // 2, H // 2)

player_jump = [
    pygame.image.load('images/Player JUMP/Player JUMP 1.png').convert_alpha(),
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



MenuBG = pygame.image.load('images/MENUBG.png').convert_alpha()
GameBG = pygame.image.load('images/GameBG.png').convert_alpha()
#Вступительный фон
OpenBG = pygame.image.load('images/Вступительный фон 1.png')
OpenBG = pygame.transform.scale(OpenBG, (1280, 720)).convert_alpha()
OpenBG_x = 0
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



Player = Player()


enemys = []
INIT_DELAY = 2000
spawn_delay = INIT_DELAY
DECREASE_BASE = 1.50
last_spawn_time = pygame.time.get_ticks()


def switch_scene(lvl):
    global current_scene
    current_scene =lvl




def LoadScreen():

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_BACKSPACE:
                switch_scene(MainMenu)
                running = False
        loading_screen = LoadingScreen(screen)

        clock.tick(60)
        loading_screen.update()
        loading_screen.draw()
        pygame.display.flip()

def MainMenu():

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                switch_scene(GameLVL1)

                running = False

        screen.fill((92, 148, 252))
        bg_sound1.play()
        screen.blit(MenuBG, (0, H - GROUND_H))





        pygame.display.flip()


def GameLVL1():

    global last_spawn_time, spawn_delay
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                switch_scene(MainMenu)
                running = False
            elif e.type == pygame.KEYDOWN:
                if Player.is_out:
                    score = 0
                    spawn_delay = INIT_DELAY
                    lst_spawn_time = pygame.time.get_ticks()
                    Player.respawn()
                    enemys.clear()
        bg_sound1.stop()
        bg_sound2.play()
        score = 0
        clock.tick(FPS)

        screen.blit(GameBG, (0, H - GROUND_H))

        screen.blit(ground_image, (0, H - GROUND_H))
        score_text = font_large.render(str(score), True, (255, 255, 255))
        score_rect = score_text.get_rect()

        if Player.is_out:
            score_rect.midbottom = (W // 2, H // 2)

            screen.blit(retry_text, retry_rect)
        else:
            Player.update()
            Player.draw(screen)

            now = pygame.time.get_ticks()
            elapsed = now - last_spawn_time
            if elapsed > spawn_delay:
                last_spawn_time = now
                enemys.append(Enemy())

            for enemy in list(enemys):
                if enemy.is_out:
                    enemys.remove(enemy)
                else:
                    enemy.update()
                    enemy.draw(screen)


                if not Player.is_dead and not enemy.is_dead and Player.rect.colliderect(enemy.rect):
                   if Player.rect.bottom - Player.y_speed < enemy.rect.top:
                       enemy.kill(enemy_dead_image)
                       Player.jump()
                       score += 1
                       spawn_delay = INIT_DELAY / (DECREASE_BASE ** score)
                   else:
                       Player.kill(player_dead_image)





            score_rect.midtop = (W // 2, 3)

        screen.blit(score_text, score_rect)
        pygame.display.flip()






switch_scene(LoadScreen)
while current_scene is not None:
    current_scene()

quit()

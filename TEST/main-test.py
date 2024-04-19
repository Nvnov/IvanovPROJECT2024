import pygame
import sys
from buttons import Buttons

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((640, 480, )) # flags=pygame.NOFRAME (без рамок)
pygame.display.set_caption('Gorilla: The Legacy of the Berserker')
icon = pygame.image.load('../images/icon_gorilla.png').convert_alpha()
pygame.display.set_icon(icon)

myfont = pygame.font.Font('../FONTS/8-bit Arcade In.ttf', 50)
text_surface = myfont.render('Press any button', True, 'black')

# Загрузочный экран
loading = True
while loading:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    font = pygame.font.Font('../FONTS/8-bit Arcade In.ttf', 36)
    text = font.render('Загрузкa...', 1, 'white')
    text_rect = text.get_rect(center=(screen.get_width/2, screen.get_height/2))
    screen.blit(text, text_rect)

    pygame.display.flip()
    loading = False

Start1 = pygame.image.load('../images/Вступительный фон 1.png').convert_alpha()
bg2 = pygame.image.load('../images/Spriters/Zamok 1.png').convert_alpha()

walk_left = [
    pygame.image.load('../images/Player test L/test-LEFT 1.png').convert_alpha(),
    pygame.image.load('../images/Player test L/test-LEFT 2.png').convert_alpha(),
    pygame.image.load('../images/Player test L/test-LEFT 3.png').convert_alpha(),
    pygame.image.load('../images/Player test L/test-LEFT 4.png').convert_alpha(),
]
walk_left = pygame.transform.scale(ground_image, (180, 222))
walk_right = [
    pygame.image.load('../images/Player test R/test-RIGHT 1.png').convert_alpha(),
    pygame.image.load('../images/Player test R/test-RIGHT 2.png').convert_alpha(),
    pygame.image.load('../images/Player test R/test-RIGHT 3.png').convert_alpha(),
    pygame.image.load('../images/Player test R/test-RIGHT 4.png').convert_alpha(),
]
walk_right = pygame.transform.scale(ground_image, (180, 222))
STAY = pygame.image.load('../images/Player/STAY.png').convert_alpha()

mob = pygame.image.load('../images/enemy/ENEMY LEFT.png').convert_alpha()
mob_x = 650
STAY_x = 0
Start1_x = 0
Start1_y = 0
bg_x = 0
player_x = 120
player_y = 270



player_anim_count = 0
player_speed = 2

bg_sound = pygame.mixer.Sound('../sounds/Вступление.mp3')
bg_sound.set_volume(0.15)

is_jump = False
jump_count = 10
clock.tick(10)
##bg_sound.play()

gameplay = True

current_scene = None
def switch_scene(lvl):
    global current_scene
    current_scene = lvl

def Start():
    running = True
    while running:
        for e in pygame.event.get():
             if e.type == pygame.QUIT:
                 running = False
                 switch_scene(None)
             elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                switch_scene(Menu)
                running = False
    screen.fill((255, 0, 0))
    pygame.display.update()

def Menu():
    running = True
    while running:
        for e in pygame.event.get():
             if e.type == pygame.QUIT:
                 running = False
                 switch_scene(None)
             elif e.type == pygame.KEYDOWN and e.key == pygame.K_TAB:
                 switch_scene(lvl1)
                 running = False
    screen.fill((255, 0, 0))
    pygame.display.update()

def lvl1():
    mob_x = 250
    STAY_x = 0
    Start1_x = 0
    Start1_y = 0
    bg_x = 0
    player_x = 120
    player_y = 270



    running = True
    while running:
        screen.blit(bg2, (bg_x, 0))
        screen.blit(bg2, (bg_x + 640, 0))
        screen.blit(walk_right[player_anim_count], (120, 270))

        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        screen.blit(mob, (mob_x, 250))

        if gameplay:
            keys = pygame.key.get_pressed()






            if keys[pygame.K_a] and player_x > 0:
                player_x -= player_speed
                screen.blit(walk_left[player_anim_count], (player_x, player_y))
            elif keys[pygame.K_d] and player_x < 590:
                player_x += player_speed
                screen.blit(walk_right[player_anim_count], (player_x, player_y))


            if not is_jump:
                if keys[pygame.K_SPACE]:
                    is_jump = True

            else:
                if jump_count >= -10:
                    if jump_count > 0:
                        player_y -= (jump_count ** 2) / 2
                    else:
                        player_y += (jump_count ** 2) / 2

                    jump_count -= 1
                else:
                    is_jump = False
                    jump_count = 10






            bg_x -= 2
            if bg_x == -640:
                bg_x = 0


            mob_x -= 10
        else:
            screen.fill((87,88,89))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
switch_scene(Start)
while current_scene is not None:
        current_scene()

sys.exit()

pygame.quit()
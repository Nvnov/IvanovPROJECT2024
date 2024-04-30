import pygame, sys, threading, Entity, random
from Entity import Entity
from Player import Player
from Enemy import Enemy
from Loading import LoadingScreen
from buttons import Buttons
pygame.init()


W = 1280
H = 720
FPS = 60
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption('Gorilla: The Legacy of the Berserker')
icon = pygame.image.load('images/icon_gorilla.png').convert_alpha()
pygame.display.set_icon(icon)

#Музыка
bg_sound1 = pygame.mixer.Sound('sounds/Вступление.mp3')
bg_sound2 = pygame.mixer.Sound('sounds/Фон звук.mp3')
bg_sound1.set_volume(0.05)
bg_sound2.set_volume(0.05)




clock = pygame.time.Clock()



font ='FONTS/8-bit Arcade In.ttf'
font_large = pygame.font.Font(font, 100)
font_small = pygame.font.Font(font, 50)


game_over = False
retry_text = font_small.render('---PRESS ANY KEY---', True, (255, 255, 255))
retry_rect = retry_text.get_rect()
retry_rect.midtop = (W // 2, H // 2)

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



MenuBG = pygame.image.load('images/MENU.png').convert_alpha()
SettingsBG = pygame.image.load('images/SETTINGS.png').convert_alpha()
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



Player = Player()


enemys = []
INIT_DELAY = 2000
MIN_SPAWN_DELAY = 200
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
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                MainMenu()
                running = False
        loading_screen = LoadingScreen(screen)

        clock.tick(60)
        loading_screen.update()
        loading_screen.draw()
        pygame.display.flip()
def StartMenu():

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(StartMenu, (0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                switch_scene(MainMenu)
                running = False

        pygame.display.flip()

def MainMenu():

    start_button = Buttons(W/5-(252/2), 150, 252, 74, "Start", "Button.png", "ButtonHover.png", "sounds/click.mp3")
    settings_button = Buttons(W/5-(252/2), 300, 252, 74, "Settings", "Button.png", "ButtonHover.png", "sounds/click.mp3")
    exit_button = Buttons(W/5-(252 / 2), 450, 252, 74, "Exit", "Button.png", "ButtonHover.png", "sounds/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(MenuBG, (0, 0))
        font = pygame.font.Font("FONTS/8-bit Arcade In.ttf", 70)

        text_surface = font.render("|Gorilla The Legacy of the Berserker|", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(W / 2, 47))
        screen.blit(text_surface, text_rect)

        text_surface = font.render("|Nvnov|", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(W / 2, 660))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                print("GO!")
                fade()
                GameLVL1()

            if event.type == pygame.USEREVENT and event.button == settings_button:
                print("Settings!")
                fade()
                Settings_menu()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                print("Bye!")
                pygame.quit()
                sys.exit()



            for btn in [start_button, settings_button, exit_button]:
                btn.handle_event(event)

        for btn in [start_button, settings_button, exit_button]:
            btn.check_hovered(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def Settings_menu():

    audio_button = Buttons(W / 5 - (252 / 2), 150, 252, 74, "Audio", "Button.png", "ButtonHover.png","sounds/click.mp3")
    video_button = Buttons(W / 5 - (252 / 2), 300, 252, 74, "Video", "Button.png", "ButtonHover.png","sounds/click.mp3")
    back_button = Buttons(W / 5 - (252 / 2), 450, 252, 74, "Back", "Button.png", "ButtonHover.png", "sounds/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(SettingsBG, (0, 0))

        font = pygame.font.Font("FONTS/8-bit Arcade In.ttf", 70)
        text_surface = font.render("|Settings|", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(W / 2, 47))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                print("Back!")
                fade()
                MainMenu()


            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, video_button, back_button]:
            btn.check_hovered(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def GameLVL1():
    global last_spawn_time, spawn_delay
    score = 0
    last_spawn_time = pygame.time.get_ticks()
    spawn_delay = INIT_DELAY
    restart_button = Buttons(W / 5 - (252 / 2), 150, 252, 74, "Restart", "Button.png", "ButtonHover.png","sounds/click.mp3")

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    MainMenu()
                    return False
                if Player.is_out:
                    score = 0
                    last_spawn_time = pygame.time.get_ticks()
                    spawn_delay = INIT_DELAY
                    Player.respawn()
                    enemys.clear()




        if not Player.is_out:
            bg_sound1.stop()
            bg_sound2.play()

        clock.tick(FPS)
        screen.blit(GameBG, (0, H - GROUND_H))
        screen.blit(ground_image, (0, H - GROUND_H))

        if Player.is_out:
            score_rect = retry_text.get_rect()
            score_rect.midbottom = (W // 2, H // 2)
            screen.blit(retry_text, score_rect)





        else:
            Player.update()
            Player.draw(screen)
            now = pygame.time.get_ticks()
            if now - last_spawn_time > spawn_delay:
                last_spawn_time = now
                enemys.append(Enemy())

            for enemy in enemys[:]:
                if enemy.is_out:
                    enemys.remove(enemy)
                else:
                    enemy.update()
                    enemy.draw(screen)
                    if Player.rect.colliderect(enemy.rect):
                        if not Player.is_dead and not enemy.is_dead:
                            if Player.rect.bottom - Player.y_speed < enemy.rect.top:
                                enemy.kill(enemy_dead_image)
                                Player.jump()
                                score += 1
                                spawn_delay = max(INIT_DELAY / (DECREASE_BASE ** score), MIN_SPAWN_DELAY)
                            else:
                                Player.kill(player_dead_image)
                                Player.is_out = True

        score_text = font_large.render(str(score), True, (255, 255, 255))
        score_rect = score_text.get_rect()
        score_rect.midtop = (W // 2, 3)
        screen.blit(score_text, score_rect)
        pygame.display.flip()

    switch_scene(LoadScreen)



def fade():
    running = True
    fade_alpha = 0

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return False

        fade_surface = pygame.Surface((W, H))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False



        pygame.display.flip()
        clock.tick(FPS)

current_scene = LoadScreen()
while current_scene is not None:
    current_scene = current_scene()

pygame.quit()

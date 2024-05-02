import pygame, sys, threading, Entity, random
from Entity import Entity, bg_sound1, bg_sound2, mouse, icon, font, font_large, font_small, player_jump, player_IDLE, player_win, player_walk_right, player_walk_left, MenuBG, SettingsBG, VideoBG, GameBG, StartMenu, player_image, player_dead_image, enemy_image, enemy_dead_image, GROUND_H, ground_image
from Player import Player
from Enemy import Enemy
from Loading import LoadingScreen
from buttons import Buttons
from TEST import player_stand, walk_right, player_IDLE, walk_left, jumpRight, jumpLeft
pygame.init()

win = pygame.display.set_mode((1280, 720))

W = 1280
H = 720

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption('Gorilla: The Legacy of the Berserker')

pygame.display.set_icon(icon)

FPS = 60



clock = pygame.time.Clock()

pygame.mouse.set_visible(False)


game_over = False
retry_text = font_small.render('---PRESS ANY KEY---', True, (255, 255, 255))
retry_rect = retry_text.get_rect()
retry_rect.midtop = (W // 2, H // 2)

# Переменные для анимации
x = 50
y = 400
width = 64
height = 64
speed = 5
isJump = False
jumpCount = 10
left = False
right = False
animCount = 0
lastMove = "left"


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

    levels_button = Buttons(W/5-(252/2), 150, 252, 74, "Levels", "Button.png", "ButtonHover.png", "click.mp3")
    settings_button = Buttons(W/5-(252/2), 300, 252, 74, "Settings", "Button.png", "ButtonHover.png", "click.mp3")
    exit_button = Buttons(W/5-(252 / 2), 450, 252, 74, "Exit", "Button.png", "ButtonHover.png", "click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(MenuBG, (0, 0))
        bg_sound1.play()
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

            if event.type == pygame.USEREVENT and event.button == levels_button:
                print("GO!")
                fade()
                Levels_menu()

            if event.type == pygame.USEREVENT and event.button == settings_button:
                print("Settings!")
                fade()
                Settings_menu()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                print("Bye!")
                pygame.quit()
                sys.exit()



            for btn in [levels_button, settings_button, exit_button]:
                btn.handle_event(event)

        for btn in [levels_button, settings_button, exit_button]:
            btn.check_hovered(pygame.mouse.get_pos())
            btn.draw(screen)


        x, y = pygame.mouse.get_pos()
        screen.blit(mouse, (x, y))

        pygame.display.flip()



def Levels_menu():

    game1_button = Buttons(W / 5 - (252 / 2), 150, 252, 74, "Game 1", "Button.png", "ButtonHover.png","click.mp3")
    game2_button = Buttons(W / 5 - (252 / 2), 300, 252, 74, "Game 2", "Button.png", "ButtonHover.png","click.mp3")
    game3_button = Buttons(W / 5 - (252 / 2), 450, 252, 74, "Game 3", "Button.png", "ButtonHover.png", "click.mp3")
    back_button = Buttons(W / 2 - (152 / 2), 300, 400, 74, "Back", "Button.png", "ButtonHover.png", "click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(SettingsBG, (0, 0))

        font = pygame.font.Font("FONTS/8-bit Arcade In.ttf", 70)
        text_surface = font.render("|Levels|", True, (255, 255, 255))
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

            if event.type == pygame.USEREVENT and event.button == game1_button:
                print("Game 1!")
                fade()
                Game1()

            if event.type == pygame.USEREVENT and event.button == game2_button:
                print("Game 2!")
                fade()
                Game2()

            if event.type == pygame.USEREVENT and event.button == game3_button:
                print("Game 3!")
                fade()
                Game3()


            for btn in [game1_button, game2_button, game3_button, back_button]:
                btn.handle_event(event)

        for btn in [game1_button, game2_button, game3_button, back_button]:
            btn.check_hovered(pygame.mouse.get_pos())
            btn.draw(screen)


        x, y = pygame.mouse.get_pos()
        screen.blit(mouse, (x, y))
        pygame.display.flip()


def Settings_menu():

    audio_button = Buttons(W / 5 - (252 / 2), 150, 252, 74, "Audio", "Button.png", "ButtonHover.png","click.mp3")
    video_button = Buttons(W / 5 - (252 / 2), 300, 252, 74, "Video", "Button.png", "ButtonHover.png","click.mp3")
    back_button = Buttons(W / 5 - (252 / 2), 450, 252, 74, "Back", "Button.png", "ButtonHover.png", "click.mp3")

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

            if event.type == pygame.USEREVENT and event.button == audio_button:
                print("Back!")
                fade()
                Audio_menu()

            if event.type == pygame.USEREVENT and event.button == video_button:
                print("Video!")
                fade()
                Video_menu()


            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, video_button, back_button]:
            btn.check_hovered(pygame.mouse.get_pos())
            btn.draw(screen)


        x, y = pygame.mouse.get_pos()
        screen.blit(mouse, (x, y))
        pygame.display.flip()


def Audio_menu():

    music_button = Buttons(W / 5 - (252 / 2), 150, 252, 74, "music", "Button.png", "ButtonHover.png","click.mp3")
    back_button = Buttons(W / 5 - (252 / 2), 450, 252, 74, "Back", "Button.png", "ButtonHover.png", "click.mp3")

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

            if event.type == pygame.USEREVENT and event.button == music_button:
                print("Mute!")



            for btn in [music_button, back_button]:
                btn.handle_event(event)

        for btn in [music_button, back_button]:
            btn.check_hovered(pygame.mouse.get_pos())
            btn.draw(screen)


        x, y = pygame.mouse.get_pos()
        screen.blit(mouse, (x, y))
        pygame.display.flip()

def Video_menu():
    global W, H, screen, MenuBG
    fullscreen_button = Buttons(W / 5 - (252 / 2), 150, 252, 74, "Full screen", "Button.png", "ButtonHover.png","click.mp3")
    screen1_button = Buttons(W / 5 - (252 / 2), 300, 252, 74, "640x480", "Button.png", "ButtonHover.png","click.mp3")
    screen2_button = Buttons(W / 5 - (252 / 2), 450, 252, 74, "1280x720", "Button.png", "ButtonHover.png", "click.mp3")
    back_button = Buttons(W / 2 - (152 / 2), 300, 400, 74, "Back", "Button.png", "ButtonHover.png", "click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(VideoBG, (0, 0))

        font = pygame.font.Font("FONTS/8-bit Arcade In.ttf", 70)
        text_surface = font.render("|Video|", True, (255, 255, 255))
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

            if event.type == pygame.USEREVENT and event.button == fullscreen_button:
                change_video_mode(1920, 1080, pygame.FULLSCREEN)
                fade()


            if event.type == pygame.USEREVENT and event.button == screen1_button:
                change_video_mode(640, 480)
                fade()

            if event.type == pygame.USEREVENT and event.button == screen2_button:
                change_video_mode(1280, 720)
                fade()

            for btn in [fullscreen_button, screen1_button,screen2_button, back_button]:
                btn.handle_event(event)

        for btn in [fullscreen_button, screen1_button,screen2_button, back_button]:
            btn.check_hovered(pygame.mouse.get_pos())
            btn.draw(screen)


        x, y = pygame.mouse.get_pos()
        screen.blit(mouse, (x, y))
        pygame.display.flip()

def Game1():
    global last_spawn_time, spawn_delay
    score = 0
    last_spawn_time = pygame.time.get_ticks()
    spawn_delay = INIT_DELAY

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

            for enemy in enemys:
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
def Game2():
    global animCount
    win.fill((0, 0, 0))  # Заливка фона окна черным цветом

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walk_left[animCount // 8], (x, y))
        animCount += 1
    elif right:
        win.blit(walk_right[animCount // 8], (x, y))
        animCount += 1
    elif isJump:
        if lastMove == "right":
            win.blit(jumpRight, (x, y))
        else:
            win.blit(jumpLeft, (x, y))
        animCount += 1
    else:
        win.blit(player_stand, (x, y))
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > speed:
        x -= speed
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_d] and x < 800 - width - speed:
        x += speed
        left = False
        right = True
        lastMove = "right"
    else:
        left = False
        right = False
        animCount += 1
        if animCount >= len(player_IDLE) * 5:  # Умножаем на 10 для замедления анимации
            animCount = 0
        current_frame = player_IDLE[animCount // 10]  # Делим на 10 для замедления анимации
    if not isJump:
        if keys[pygame.K_w]:
            isJump = True
            animCount = 0
    else:
        if jumpCount >= -10:
            if jumpCount > 0:
                y -= (jumpCount ** 2) * 0.5
            else:
                y += (jumpCount ** 2) * 0.5
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    pygame.display.update()




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



def change_video_mode(w, h, fullscreen = 0 ):
    global W,H, screen, MenuBG, SettingsBG, VideoBG, GameBG, player_image, ground_image, enemy_image
    W, H = w, h
    screen = pygame.display.set_mode((W, H), fullscreen)
    MenuBG = pygame.transform.scale(MenuBG, (W, H))
    SettingsBG = pygame.transform.scale(SettingsBG, (W, H))
    VideoBG = pygame.transform.scale(VideoBG, (W, H))
    GameBG = pygame.transform.scale(GameBG, (W, H))
    player_image = pygame.transform.scale(player_image, (W, H))
    ground_image = pygame.transform.scale(ground_image, (W, H))
    enemy_image = pygame.transform.scale(enemy_image, (W, H))

current_scene = LoadScreen()
while current_scene is not None:
    current_scene = current_scene()

pygame.quit()

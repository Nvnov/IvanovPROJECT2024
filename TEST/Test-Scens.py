import pygame, sys, threading
from buttons import Buttons
from Player import Player
pygame.init()




screen = pygame.display.set_mode((1280, 720))
Start1 = pygame.image.load('../images/Вступительный фон 1.png')
Start1_x = 0
Start1_y = 0
Player = Player(screen)
CLOCK = pygame.time.Clock()



WORK = 100000000

LOADING_BG = pygame.image.load('../images/Loading Bar Background.png')
LOADING_BG_RECT = LOADING_BG.get_rect(center=(640, 360))

loading_bar = pygame.image.load('../images/Loading Bar.png')
loading_bar_rect = loading_bar.get_rect(midleft=(640, 360))
loading_finished = False
loading_progress = 0
loading_bar_width = 8

def doWork():
    global loading_finished, loading_progress

    for i in range(WORK):
        math_equation = 523687 / 789456 * 89456
        loading_progress = i

    loading_finished = True


font = pygame.font.SysFont("FONTS/8-bit Arcade In.ttf", 100)
finished = font.render("--- Press any button ---", 1, "White")
finished_rect = finished.get_rect(center=(640, 360))


threading.Thread(target=doWork).start()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.fill("Black")

        if not loading_finished:
            loading_bar_width = loading_progress / WORK * 720

            loading_bar = pygame.transform.scale(loading_bar, (int(loading_bar_width), 150))
            loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))

            screen.blit(LOADING_BG, LOADING_BG_RECT)
            screen.blit(loading_bar, loading_bar_rect)

        else:
            screen.blit(finished, finished_rect)

pygame.display.update()
CLOCK.tick(30)

current_scene = None
def switch_scene(lvl):
    global current_scene
    current_scene =lvl

def lvl1():
    running = True
    while running:

        for e in pygame.event.get():
             if e.type == pygame.QUIT:
                 running = False
                 switch_scene(None)
             elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                switch_scene(lvl2)
                running = False
    screen.blit(Start1, (Start1_x, Start1_y))
    pygame.display.update()

def lvl2():
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



switch_scene(lvl1)
while current_scene is not None:
    current_scene()






pygame.quit()
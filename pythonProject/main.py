import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1024, 735, )) # flags=pygame.NOFRAME (без рамок)
pygame.display.set_caption('Gorilla: The Legacy of the Berserker')
icon = pygame.image.load('images/icon_gorilla.png')
pygame.display.set_icon(icon)
screen.fill((33, 33, 33))



myfont = pygame.font.Font('fonts/8-bit Arcade In.ttf', 50)
text_surface = myfont.render('Press any button', True, 'black')

bg = pygame.image.load('images/Вступительный фон 1.png')


bg_sound = pygame.mixer.Sound('sounds/Вступление.mp3')
bg_sound.play()
running = True
while running:


    screen.blit(bg, (0, -0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill((104, 28, 35))

import pygame

# Инициализация Pygame
pygame.init()

# Создание окна игры
win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Игра с анимацией прыжка")

new_size = (150, 222)
# Загрузка спрайтов
player_stand = pygame.image.load('images/Player/Player.png')
player_stand = pygame.transform.scale(player_stand, (180, 222))
walk_right = [
    pygame.image.load('images/Player Walk Right/Right 1.png').convert_alpha(),
    pygame.image.load('images/Player Walk Right/Right 2.png').convert_alpha(),
    pygame.image.load('images/Player Walk Right/Right 3.png').convert_alpha(),
    pygame.image.load('images/Player Walk Right/Right 4.png').convert_alpha(),
    pygame.image.load('images/Player Walk Right/Right 5.png').convert_alpha(),
    pygame.image.load('images/Player Walk Right/Right 6.png').convert_alpha(),
    pygame.image.load('images/Player Walk Right/Right 7.png').convert_alpha(),
    pygame.image.load('images/Player Walk Right/Right 8.png').convert_alpha()
]
walk_right = [pygame.transform.scale(image, new_size) for image in walk_right]
player_IDLE = [
    pygame.image.load('images/Player IDLE/idle 1-1.png').convert_alpha(),
    pygame.image.load('images/Player IDLE/idle 1-2.png').convert_alpha(),
    pygame.image.load('images/Player IDLE/idle 1-3.png').convert_alpha(),
    pygame.image.load('images/Player IDLE/idle 1-4.png').convert_alpha(),
]
player_IDLE = [pygame.transform.scale(image, new_size) for image in player_IDLE]
walk_left = [
    pygame.image.load('images/Player Walk Left/Left 1.png').convert_alpha(),
    pygame.image.load('images/Player Walk Left/Left 2.png').convert_alpha(),
    pygame.image.load('images/Player Walk Left/Left 3.png').convert_alpha(),
    pygame.image.load('images/Player Walk Left/Left 4.png').convert_alpha(),
    pygame.image.load('images/Player Walk Left/Left 5.png').convert_alpha(),
    pygame.image.load('images/Player Walk Left/Left 6.png').convert_alpha(),
    pygame.image.load('images/Player Walk Left/Left 7.png').convert_alpha(),
    pygame.image.load('images/Player Walk Left/Left 8.png').convert_alpha()
]
walk_left = [pygame.transform.scale(image, new_size) for image in walk_left]
jumpRight = pygame.image.load('images/Player JUMP/JUMP RIGHT.png').convert_alpha()
jumpRight = pygame.transform.scale(jumpRight, (200, 222))
jumpLeft = pygame.image.load('images/Player JUMP/JUMP LEFT.png').convert_alpha()
jumpLeft = pygame.transform.scale(jumpLeft, (200, 222))
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

clock = pygame.time.Clock()

# Функция для отрисовки окна игры
def drawWindow():
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

    pygame.display.update()


def switch_scene(lvl):
    global current_scene
    current_scene =lvl
# Основной цикл игры
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


    drawWindow()

pygame.quit()
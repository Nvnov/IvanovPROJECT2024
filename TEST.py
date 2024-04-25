import pygame

# Инициализация Pygame
pygame.init()

# Создание окна игры
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Игра с анимацией прыжка")

# Загрузка спрайтов
player_stand = pygame.image.load('images/Player/Player.png')
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
jumpRight = [
    pygame.image.load('images/Player JUMP/JUMP RIGHT.png').convert_alpha()
    ]
jumpLeft = [
    pygame.image.load('images/Player JUMP/JUMP LEFT.png').convert_alpha()
    ]

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
lastMove = "right"

clock = pygame.time.Clock()

# Функция для отрисовки окна игры
def drawWindow():
    global animCount
    win.fill((0, 0, 0))  # Заливка фона окна черным цветом

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walk_left[animCount // 10], (x, y))
        animCount += 1
    elif right:
        win.blit(walk_right[animCount // 10], (x, y))
        animCount += 1
    elif isJump:
        if lastMove == "right":
            win.blit(jumpRight[animCount // 10], (x, y))
        else:
            win.blit(jumpLeft[animCount // 10], (x, y))
        animCount += 1
    else:
        win.blit(player_stand, (x, y))

    pygame.display.update()

# Основной цикл игры
run = True
while run:
    clock.tick(30)

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
        animCount = 0

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
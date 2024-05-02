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

# Функция для отрисовки окн
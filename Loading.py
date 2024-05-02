import pygame, sys, threading

pygame.init()

# Экран и Шрифт
screen = pygame.display.set_mode((1280, 720))
W = 1280
H = 720
pygame.display.set_caption('Gorilla: The Legacy of the Berserker')

FONT = pygame.font.SysFont("8-bit Arcade In", 100)
WORK = 1000000
CLOCK = pygame.time.Clock()


class LoadingScreen:
    def __init__(self, screen):
        self.screen = screen
        self.loading_bg = pygame.image.load("images/Loading Bar Background.png")
        self.loading_bg_rect = self.loading_bg.get_rect(center=(W // 2, H // 2))

        self.loading_bar = pygame.image.load("images/Loading Bar.png")
        self.loading_bar_rect = self.loading_bar.get_rect(midleft=(280, H // 2))
        self.loading_finished = False
        self.loading_progress = 0
        self.loading_bar_width = 8
        self.work = WORK


        # Запуск потока для выполнения работы
        threading.Thread(target=self.do_work).start()

    def do_work(self):
        for i in range(self.work):
            math_equation = 523687 / 789456 * 89456
            self.loading_progress = i
        self.loading_finished = True

    def update(self):
        if not self.loading_finished:
            self.loading_bar_width = self.loading_progress / self.work * 720
            self.loading_bar = pygame.transform.scale(self.loading_bar, (int(self.loading_bar_width), 150))
            self.loading_bar_rect = self.loading_bar.get_rect(midleft=(280, H // 2))

    def draw(self):
        self.screen.fill("#0d0e2e")
        self.screen.blit(self.loading_bg, self.loading_bg_rect)
        self.screen.blit(self.loading_bar, self.loading_bar_rect)
        if self.loading_finished:
            finished = FONT.render("Press BACKSPACE", True, "white")
            finished_rect = finished.get_rect(center=(W // 2, H // 2))
            self.screen.blit(finished, finished_rect)
        pygame.display.update()

        CLOCK.tick(60)
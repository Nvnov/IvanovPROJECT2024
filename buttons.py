import pygame
class Buttons:
    def __init__(self, x ,y ,w, h,  text, font, color, image_path, hover_image_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text

        self.font = font
        self.color = color

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (w, h))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        font = pygame.font.Font((None, 36))
        text_surface = font.render(self.text, True, (255,255,255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hovered(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))

            pygame.display.set_caption('Gorilla: The Legacy of the Berserker')
            icon = pygame.image.load('images/icon_gorilla.png').convert_alpha()
            pygame.display.set_icon(icon)

            myfont = pygame.font.Font('fonts/8-bit Arcade In.ttf', 50)
            text_surface = myfont.render('Press any button', True, 'black')
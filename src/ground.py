import pygame
import config

class Ground:
    def __init__(self):
        self.height = config.GROUND_HEIGHT
        self.rectangle = pygame.rect.Rect(
            0,
            config.SCREEN_HEIGHT - config.GROUND_HEIGHT,
            config.SCREEN_WIDTH,
            config.GROUND_HEIGHT
        )

    def draw(self, window):
        pygame.draw.rect(window, "red", self.rectangle)
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
        self.texture = pygame.image.load(config.BASE_PATH/'img/ground.png')
        self.texture = pygame.transform.scale(
            self.texture, (config.SCREEN_WIDTH, config.GROUND_HEIGHT)
        )

        self.ground_scroll = 0

    def draw(self, window):
        window.blit(self.texture, (self.ground_scroll, config.GROUND_Y))
        window.blit(self.texture, (self.ground_scroll + config.SCREEN_WIDTH, config.GROUND_Y))

        self.ground_scroll -= config.GROUND_SPEED
        if abs(self.ground_scroll) > config.SCREEN_WIDTH:
            self.ground_scroll = 0
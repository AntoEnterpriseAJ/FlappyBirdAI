import random

import pygame
import config

class Pipe:
    def __init__(self):
        self.active = True
        self.passed = False
        self.x = config.SCREEN_WIDTH
        self.texture_top = pygame.image.load(config.BASE_PATH/'img/pipe.png')
        self.texture_bottom = pygame.image.load(config.BASE_PATH/'img/pipe.png')

        gap_y = random.uniform(config.PIPE_GAP_SIZE, config.GROUND_Y - config.PIPE_GAP_SIZE * 2)

        self.top_pipe = pygame.Rect(self.x, 0, config.PIPE_WIDTH, gap_y)
        self.bottom_pipe = pygame.Rect(
            self.x,
            gap_y + config.PIPE_GAP_SIZE,
            config.PIPE_WIDTH,
            config.GROUND_Y - (gap_y + config.PIPE_GAP_SIZE - 1)
        )

        self.texture_top = pygame.transform.scale(
            self.texture_top,(config.PIPE_WIDTH, self.texture_top.get_height())
        )
        self.texture_top = pygame.transform.rotate(self.texture_top, 180)

        self.texture_bottom = pygame.transform.scale(
            self.texture_bottom, (config.PIPE_WIDTH, self.texture_bottom.get_height())
        )

    def draw(self, window):
        if not self.active:
            return

        top_pipe_coords = (self.top_pipe.x,
                           self.top_pipe.y - (self.texture_top.get_size()[1] - self.top_pipe.height))

        window.blit(self.texture_top, top_pipe_coords)
        window.blit(
            self.texture_bottom,
            (self.bottom_pipe.x, self.bottom_pipe.y),
            (0, 0, self.bottom_pipe.width, self.bottom_pipe.height)
        )

    def update(self, player):
        if not self.active:
            return

        self.x -= 1.0
        self.top_pipe.x = self.x
        self.bottom_pipe.x = self.x

        if self.x + config.PIPE_WIDTH <= player.rectangle.x:
            self.passed = True

        if self.x + config.PIPE_WIDTH <= 0:
            self.active = False

    def is_active(self):
        return self.active
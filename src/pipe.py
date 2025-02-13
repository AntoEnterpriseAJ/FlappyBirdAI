import random

import pygame
import config

class Pipe:
    def __init__(self):
        self.active = True
        self.passed = False
        self.x = config.SCREEN_WIDTH

        gap_y = random.uniform(config.PIPE_GAP_SIZE, config.GROUND_Y - config.PIPE_GAP_SIZE * 2)

        self.top_pipe = pygame.Rect(self.x, 0, config.PIPE_WIDTH, gap_y)
        self.bottom_pipe = pygame.Rect(
            self.x,
            gap_y + config.PIPE_GAP_SIZE,
            config.PIPE_WIDTH,
            config.GROUND_Y - (gap_y + config.PIPE_GAP_SIZE)
        )

    def draw(self, window):
        if not self.active:
            pass

        pygame.draw.rect(window, "red", self.top_pipe)
        pygame.draw.rect(window, "red", self.bottom_pipe)

    def update(self, player):
        if not self.active:
            pass

        self.x -= 1.0
        self.top_pipe.x = self.x
        self.bottom_pipe.x = self.x

        if self.x + config.PIPE_WIDTH <= player.rectangle.x:
            self.passed = True

        if self.x + config.PIPE_WIDTH <= 0:
            self.active = False

    def is_active(self):
        return self.active
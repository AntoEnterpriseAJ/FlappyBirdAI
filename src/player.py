import numpy as np
import pygame
from pygame.display import update

import config
import random
import brain

class Player:
    def __init__(self):
        self.active = True
        self.flapping = False
        self.velocity = 1.0
        self.color = random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255)
        self.rectangle = pygame.rect.Rect(
            config.SCREEN_WIDTH * 0.1,
            (config.SCREEN_HEIGHT - config.GROUND_HEIGHT - config.PLAYER_SIZE) / 2.0 ,
            config.PLAYER_SIZE,
            config.PLAYER_SIZE
            )

        self.brain = brain.Brain()
        self.vision = np.array([0.5, 1.0, 0.5])

    def draw(self, window, pipes):
        if self.active:
            pygame.draw.rect(window, self.color, self.rectangle)

            closest = pipes[0]
            for p in pipes:
                if not p.passed:
                    closest = p

            pygame.draw.line(window, "white", self.rectangle.center,
                             (self.rectangle.center[0], closest.top_pipe.bottom))
            pygame.draw.line(window, "white", self.rectangle.center,
                             (closest.top_pipe.x, self.rectangle.center[1]))
            pygame.draw.line(window, "white", self.rectangle.center,
                             (self.rectangle.center[0], closest.bottom_pipe.y))

    def update(self, pipes, ground):
        if self.pipe_collision(pipes) or self.bounds_collision(ground):
            self.active = False

        if self.active:
            self.rectangle.y += self.velocity
            self.velocity = min(self.velocity + config.VELOCITY_RATE, config.MAX_VELOCITY)
            self.update_vision(pipes)

            self.think()

    def update_vision(self, pipes):
        closest = pipes[0]
        for p in pipes:
            if not p.passed:
                closest = p

        self.vision[0] = max(0, self.rectangle.center[1] - closest.top_pipe.bottom) / 50
        self.vision[1] = max(0, self.rectangle.center[0] - closest.top_pipe.x) / 50
        self.vision[2] = max(0, self.rectangle.center[1] - closest.bottom_pipe.y) / 50

    def think(self):
        flap_chance = self.brain.make_prediction(self.vision)
        if flap_chance > 0.8:
            self.flap()

    def flap(self):
        if not self.flapping:
            self.velocity = -config.MAX_VELOCITY
            self.flapping = True

        if self.velocity >= 1:
            self.flapping = False

    def pipe_collision(self, pipes):
        for pipe in pipes:
            if self.rectangle.colliderect(pipe.bottom_pipe) or self.rectangle.colliderect(pipe.top_pipe):
                return True
        return False

    def bounds_collision(self, ground):
        if self.rectangle.y <= 0 or self.rectangle.colliderect(ground.rectangle):
            return True
        return False

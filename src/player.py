import pygame
import config
import random

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

    def draw(self, window):
        if self.active:
            pygame.draw.rect(window, self.color, self.rectangle)

    def update(self, pipes, ground):
        if self.pipe_collision(pipes) or self.bounds_collision(ground):
            self.active = False

        if self.active:
            self.rectangle.y += self.velocity
            self.velocity = min(self.velocity + config.VELOCITY_RATE, config.MAX_VELOCITY)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.flap()

    def flap(self):
        if not self.flapping:
            self.velocity = -config.MAX_VELOCITY
            self.flapping = True

        if self.velocity >= 3:
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

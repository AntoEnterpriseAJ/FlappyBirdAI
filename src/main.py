import collections
import pygame
import config
import pipe
from src.ground import Ground
from src.player import Player

pygame.init()
window = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

def poll_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def spawn_pipe(pipes):
    pipes.appendleft(pipe.Pipe())

def main():
    pipe_spawn_time = 0
    ground = Ground()
    pipes = collections.deque()
    player = Player()

    while True:
        poll_events()

        window.fill("purple")

        ground.draw(window)

        if pipe_spawn_time <= 0:
            spawn_pipe(pipes)
            pipe_spawn_time = config.PIPE_SPAWN_TIME

        for pipe in list(pipes):
            pipe.draw(window)
            pipe.update()

            if not pipe.is_active():
                pipes.pop()

        player.update(pipes, ground)
        player.draw(window)

        pygame.display.flip()
        pipe_spawn_time -= 1
        clock.tick(60)

if __name__ == '__main__':
    main()
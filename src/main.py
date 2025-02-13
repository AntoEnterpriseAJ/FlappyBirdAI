import collections
import pygame
import config
import pipe
from src.ground import Ground
from src.population import Population

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
    population_size = 100

    pipe_spawn_time = 0
    ground = Ground()
    pipes = collections.deque()
    population = Population(population_size)

    while True:
        poll_events()
        window.fill("purple")

        ground.draw(window)

        if pipe_spawn_time <= 0:
            spawn_pipe(pipes)
            pipe_spawn_time = config.PIPE_SPAWN_TIME

        for pipe in list(pipes):
            pipe.draw(window)
            pipe.update(population.players[0])

            if not pipe.is_active():
                pipes.pop()

        population.update_players(pipes, ground)
        population.draw(window, pipes)

        pygame.display.flip()
        pipe_spawn_time -= 1
        clock.tick(60)

if __name__ == '__main__':
    main()
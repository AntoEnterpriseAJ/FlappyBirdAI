import collections
import pygame
import config
import pipe
from src.ground import Ground
from src.population import Population

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

    pygame.init()
    window = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    bg_tex = pygame.image.load('img/bg.png')
    bg_tex = pygame.transform.scale(bg_tex, (config.SCREEN_WIDTH, config.GROUND_Y))

    while True:
        poll_events()
        window.blit(bg_tex, (0,0))
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
        population.log()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_k]:
            for p in population.players:
                p.alive = False
                pygame.time.delay(20)

        if population.is_extinct():
            population.next_gen()
            pipes.clear()
            pipe_spawn_time = 0

        pygame.display.flip()
        pipe_spawn_time -= 1
        clock.tick(60)

if __name__ == '__main__':
    main()
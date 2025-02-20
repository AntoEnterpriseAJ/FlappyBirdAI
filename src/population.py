import copy
import random
import numpy as np
import player
import config

class Population:
    def __init__(self, size):
        self.size = size

        self.current_gen = 1
        self.current_log_time = config.LOG_TIME

        self.players = []
        for i in range(size):
            self.players.append(player.Player())

    def update_players(self, pipes, ground):
        for p in self.players:
            p.update(pipes, ground)

    def draw(self, window, pipes):
        for p in self.players:
            if p.alive:
                p.draw(window, pipes)

    def is_extinct(self):
        extinct = True
        for p in self.players:
            if p.alive:
                extinct = False
                break

        return extinct

    def log(self):
        self.current_log_time += 1
        if self.current_log_time >= config.LOG_TIME:
            self.current_log_time = 0

            current_players = 0
            for p in self.players:
                if p.alive:
                    current_players += 1

            print(f"alive players: {current_players}")

    def calc_fitness(self):
        return sum(p.get_fitness() for p in self.players)

    def next_gen(self):
        print(f'previous fitness: {self.calc_fitness()}, current generation: {self.current_gen}')
        new_players = self.selection()
        self.crossover(new_players)
        self.current_gen += 1

    def selection(self):
        new_players = [None] * self.size

        cumulative = self.cumulative_probabilities()
        for i in range(self.size):
            choice = 1 - random.random()
            for j in range(len(cumulative)):
                if choice <= cumulative[j]:
                    new_players[i] = copy.deepcopy(self.players[j])
                    break

        return new_players

    def crossover(self, new_players):
        offspring = [None] * self.size

        for i in range(0, len(new_players) - 1, 2):
            first_parent = new_players[i]
            second_parent = new_players[i + 1]

            offspring[i], offspring[i + 1] = self.cross(first_parent, second_parent)
            self.mutate(offspring[i])
            self.mutate(offspring[i + 1])

        if len(new_players) % 2 == 1:
            offspring[-1] = offspring[0]

        self.players = offspring

    @staticmethod
    def mutate(player, mutation_rate = 0.05, mutation_change = 0.2):
        weights = player.brain.weights
        for i in range(len(weights)):
            if random.random() < mutation_rate:
                weights[i] += random.uniform(-mutation_change, mutation_change)

    @staticmethod
    def cross(first_parent, second_parent):
        first_offspring = player.Player()
        second_offspring = player.Player()

        first_weights = first_parent.brain.weights
        second_weights = second_parent.brain.weights

        cross_point = np.random.randint(1, len(first_weights))

        first_offspring.brain.weights = np.concatenate(
            (first_weights[:cross_point],
            second_weights[cross_point:])
        )
        second_offspring.brain.weights = np.concatenate(
            (second_weights[:cross_point],
            first_weights[cross_point:])
        )

        return first_offspring, second_offspring

    def cumulative_probabilities(self):
        total_fitness = sum(p.get_fitness() for p in self.players)
        selection_probabilities = [p.get_fitness() / total_fitness for p in self.players]

        cumulative = [0] * self.size
        current_sum = 0
        for i in range(self.size):
            current_sum += selection_probabilities[i]
            cumulative[i] = current_sum

        return cumulative

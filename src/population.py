import player

class Population:
    def __init__(self, size):
        self.size = size
        self.players = []
        for i in range(size):
            self.players.append(player.Player())

    def update_players(self, pipes, ground):
        for p in self.players:
            p.update(pipes, ground)

    def draw(self, window, pipes):
        for p in self.players:
            if p.active:
                p.draw(window, pipes)
import random

import numpy as np

class Brain:
    def __init__(self):
        self.weights = np.array([random.uniform(-1, 1), random.uniform(-1, 1),
                                 random.uniform(-1, 1), random.uniform(-1, 1)])

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def make_prediction(self, vision):
        return self._sigmoid(np.dot(vision, self.weights))

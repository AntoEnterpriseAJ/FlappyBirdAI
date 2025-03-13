---

# Flappy Bird AI

## Overview

This project is a **Flappy Bird** game built using **Pygame**, where players are controlled by a **genetic algorithm**. The AI learns to navigate through pipes by evolving over multiple generations. Each player has a simple **perceptron-based** brain that makes jump decisions based on **environmental inputs**.

https://github.com/user-attachments/assets/11889f88-4a0b-47f3-b62b-611c1b3d250a

## Features

- **Flappy Bird Gameplay:** Classic mechanics with pipes, ground scrolling, and player movement.
- **Genetic Algorithm:**
  - Players evolve over generations, improving their performance.
  - Fitness is determined by survival time.
  - Selection, crossover, and mutation are used to optimize AI performance.
- **Pygame-based Rendering:** Visual representation of the AI playing the game.

## Installation

### Prerequisites

Make sure you have **Python 3.x** installed.

### Install Dependencies

```sh
pip install -r requirements.txt
```

## How It Works

### AI Brain

Each player has a **Brain**, which is a simple **perceptron** (a neural network with a single layer). It takes four inputs and decides whether to flap or not based on the weighted sum and a **sigmoid activation function**:

```python
class Brain:
    def __init__(self):
        self.weights = np.array([random.uniform(-1, 1) for _ in range(4)])
    
    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def make_prediction(self, vision):
        return self._sigmoid(np.dot(vision, self.weights))
```

<p align="center">
  <img src="https://github.com/user-attachments/assets/fee9d7d8-170b-4c6f-803d-7685f27dae5a" alt="Perceptron Diagram" width="600" />
</p>

### AI Evolution

- **Fitness Calculation:** The longer a player survives, the higher its fitness.
- **Selection:** A **roulette-wheel selection** method picks the best-performing birds.
- **Crossover:** The top-performing AI players combine their weights to produce offspring.
- **Mutation:** Small random changes are introduced to promote diversity.

## Controls

- **K Key:** Kills all players and starts the next generation.
- **Q Key:** Quit the game.

## License

This project is licensed under the **MIT License**.

---

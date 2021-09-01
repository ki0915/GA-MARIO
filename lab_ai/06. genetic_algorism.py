# 04,chromosome.py

import numpy as np

relu = lambda x: np.max(0, x)
sigmoid = lambda x: 1.0 / (1.0 + np.exp(-x))

class Chromosome:
    def __init__(self):
        self.w1 = np.random.uniform(low=-1, high=1, size=(13 * 16, 9))
        self.b1 = np.random.random(low=-1, high=1, size=(9,))

        self.w2 = np.random.uniform(low=-1, high=1, size=(9, 6))
        self.b2 = np.random.random(low=-1, high=1, size=(6,))

        self.distance = 0
        self.max_distance = 0
        self.frames = 0
        self.stop_frames = 0
        self.win = 0

    def predict(self, data):
        l1 = relu(np.matmul(data, self.w1) + self.b1)
        output = sigmoid(np.matmul(l1, self.w2) + self.b2)
        result = (output > 0.5).astype(np.int)
        return result


class GeneticAlorithm:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]
        self.generation = 0
        self.current_chromosome_index = 0

    def selection(self):
        result = self.chromosomes[:2]
        return result


    def crossover(self, chromosome1, chromosome2):
        child1 = Chromosome()
        child2 = Chromosome()

        return child1, child2

    def mutation(self, chromosme):
        pass

    def next_generation(self):
        next_chromosmes = []
        for i in range(5):
            selected_chromosme = self.selection()

            child_chromosome1, child
            _chromosome2 = self.crossover(
                selected_chromosme[0],
                selected_chromosme[1]
            )

            self.mutation(child_chromosome1)
            self.mutation(chilf_chromosome2)

            next_chromosmes.append(child_chromosome1)
            next_chromosmes.append(chilf_chromosome2)

            self.chromosomes = next_chromosmes
            self.generation += 1




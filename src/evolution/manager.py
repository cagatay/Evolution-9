from brain.NN import neural_network
from evolution import operators
from evolution.genome import song

class evolution(object):
    def __init__(self, name, evaluator, population_size, store, generation_count = 0, initialized = False):
        self.store = store
        self.name = name
        self.evaluator = neural_network.get_saved(evaluator, store)
        self.population_size = population_size
        self.generation_count = generation_count
        self.initialized = initialized
        if initialized:
            self.get_current_generation()
        else:
            self.current_generation = None

        self.save()

    def save(self):
        self.store.save_evolution(self.name,
                                  self.population_size,
                                  self.evaluator.name,
                                  self.generation_count,
                                  self.initialized)
        return

    def save_genomes(self):
        for g in self.current_generation:
            self.store.save_genome(g.name,
                                   g.genome,
                                   g.evolution,
                                   g.generation,
                                   g.individual_id,
                                   g.parent_1,
                                   g.parent_2,
                                   g.grade,
                                   g.status)
        return

    @classmethod
    def get_saved(cls, name, store):
        result = store.get_evolution(name)

        return cls(result[0], result[3], result[1], store, result[2], bool(result[4])) if result else None

    @classmethod
    def get_list(cls, store):
        result = store.get_evolution_list()

        return [x[0] for x in result] if result else None

    def initialize(self):
        self.current_generation = []

        for i in xrange(self.population_size):
            g = song(operators.random_genome(), self.name, 0, i)
            self.current_generation.append(g)

        self.initialized = True
        self.save_genomes()
        self.save()
        return

    def get_current_generation(self):
        result = self.store.get_genomes(self.name, self.generation_count)

        if result:
            self.current_generation = []

            for i in result:
                g = song(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                self.current_generation.append(g)

        return


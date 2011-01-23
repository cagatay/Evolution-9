from brain.NN import neural_network

class evolution(object):
    def __init__(self, name, evaluator, population_size, store, initialized = False):
        self.store = store
        self.name = name
        self.evaluator = neural_network.get_saved(evaluator, store)
        self.population_size = population_size
        self.generation_count = 0
        self.initialized = initialized

        self.save()

    def save(self):
        self.store.save_evolution(self.name,
                                  self.population_size,
                                  self.evaluator.name,
                                  self.generation_count,
                                  self.initialized)

    @classmethod
    def get_saved(cls, name, store):
        result = store.get_evolution(name)

        return cls(result[1], result[2], result[3], store) if result else None

    @classmethod
    def get_list(cls, store):
        result = store.get_evolution_list()

        return [x[0] for x in result] if result else None

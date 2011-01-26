from brain.NN import neural_network
from evolution import operators
from evolution.genome import song

class evolution(object):
    def __init__(self, name, evaluator, population_size, store, generation_count = 0, state='uninitialized'):
        self.store = store
        self.name = name
        self.evaluator = neural_network.get_saved(evaluator, store)
        self.population_size = population_size
        self.generation_count = generation_count
        self.state = state
        if self.state != 'uninitialized':
            self.get_current_generation()
        else:
            self.current_generation = None

        self.save()

    def save(self):
        self.store.save_evolution(self.name,
                                  self.population_size,
                                  self.evaluator.name,
                                  self.generation_count,
                                  self.state)
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

        return cls(result[0], result[3], result[1], store, result[2], result[4]) if result else None

    @classmethod
    def get_list(cls, store):
        result = store.get_evolution_list()

        return [x[0] for x in result] if result else None

    def initialize(self, console = None):
        self.current_generation = []

        for i in xrange(self.population_size):
            g = song(operators.random_genome(), self.name, 0, i)
            self.current_generation.append(g)

        self.state = 'evaluate'
        self.save_genomes()
        self.save()

        if console:
            console('%s is initialized'%self.name)
        return

    @property
    def initialized(self):
        return self.state != 'uninitialized'

    def get_current_generation(self):
        result = self.store.get_genomes(self.name, self.generation_count)

        if result:
            self.current_generation = []

            for i in result:
                g = song(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                self.current_generation.append(g)

        return

    def get_generation(self, generation):
        result = self.store.get_genomes(self.name, generation)

        if result:
            self.searched_generation = []
            
            for i in result:
                g = song(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
                self.searched_generation.append(g)

    def evaluate(self, console = None):
        self.results = []
        for g in self.current_generation:
            result = self.evaluator.evaluate(g.int_list)
            g.grade = result
            if console:
                console('%s evaluation result: %f'%(g.name, result))

        self.current_generation = sorted(self.current_generation, key=lambda x: x.grade, reverse=True)

        self.max_grade = self.current_generation[0].grade
        self.min_grade = self.current_generation[len(self.current_generation) - 1].grade
        self.avg_grade = sum([x.grade for x in self.current_generation])/self.population_size

        for i in range(self.population_size):
            if i < self.population_size/2:
                self.current_generation[i].status = 'selected'
            else:
                self.current_generation[i].status = 'eliminated'
        self.state = 'select'

        if console:
            console('Generation %d of %s : evaluation complete'%(self.generation_count, self.name))
        return

    def apply_selection(self, console = None):
        self.save_genomes()

        self.current_generation = self.current_generation[:self.population_size/2]
        self.state = 'reproduce'

        self.save()

        console('%s : applied selection on generation %d'%(self.name, self.generation_count))
        
        return

    def reproduce(self, console = None):
        self.generation_count += 1

        console('%s : reproducing of generation %d started'%(self.name, self.generation_count))

        pool = []
        
        index = 0
        while self.current_generation:
            l = len(self.current_generation) - 1

            if not l:
                break

            a = operators.r(l)

            parent_1 = self.current_generation[a]
            del self.current_generation[a]

            a = operators.r(l - 1)
            parent_2 = self.current_generation[a]

            del self.current_generation[a]

            child_1_g, child_2_g = operators.random_crossover(parent_1.note_list,
                                                              parent_2.note_list)
            operators.random_mutator(child_1_g)
            operators.random_mutator(child_2_g)

            parent_1.individual_id = index
            parent_1.status = 'created'
            parent_1.generation = self.generation_count
            parent_1.grade = 0.0
            index += 1

            parent_2.individual_id = index
            parent_2.status = 'created'
            parent_2.generation = self.generation_count
            parent_2.grade = 0.0
            index += 1

            child_1 = song(child_1_g,
                           self.name,
                           self.generation_count,
                           index,
                           parent_1.name,
                           parent_2.name)
            index += 1

            child_2 = song(child_2_g,
                           self.name,
                           self.generation_count,
                           index,
                           parent_1.name,
                           parent_2.name)
            index += 1

            t = parent_1.note_list
            operators.random_mutator(t)
            parent_1.set_genome(t)

            t = parent_2.note_list
            operators.random_mutator(t)
            parent_2.set_genome(t)

            pool += [parent_1, parent_2, child_1, child_2]

            console('created %s and %s from %s and %s'%(child_1.name, child_2.name, parent_1.name, parent_2.name))

        self.current_generation = pool

        self.save()
        self.save_genomes()
        self.state = 'evaluate'
        console('%s : created generation %d'%(self.name, self.generation_count))


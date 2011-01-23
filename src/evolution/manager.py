
class evolution(object):
    def __init__(self, name, evaluator, population_size, store, row_id):
        self.store = store
        self.name = name
        self.evaluator = evaluator
        self.population_size = population_size
        self.generation_count = 0

        if row_id is None:
            self.row_id = self.save()
        else:
            self.row_id = row_id

    def save(self):
        if self.row_id:
            self.store.update_evolution(self.row_id,
                                        self.generation_count,
                                        self.initialized)
        else:
            return self.store.new_evolution(self.name,
                                            self.evaluator,
                                            self.population_size,
                                            self.initialized)

    @classmethod
    def get_saved(cls, row_id, store):
        result = store.get_evolution(row_id)

        return cls(result[1], result[2], result[3], store, row_id) if result else None

    @classmethod
    def get_list(cls, store):
        result = store.get_evolution_list()

        return [tuple(x) for x in result] if result else None

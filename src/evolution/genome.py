from util import rttl

class Song(object):
    def __init__(self, genome):
        if type(genome) == 'list':
            self.note_list = genome
            self.genome = rttl.dump(genome)

        elif type(genome) == 'string':
            self.genome = genome
            self.note_list = rttl.parse(genome)

        self.int_list = rttl.to_int(self.note_list)

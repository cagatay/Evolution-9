import random

GENOME_LENGTH = 20

pitch_range = ['P', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
duration_range = [str(2**x) for x in range(6)]
octave_range = [str(x) for x in range(4, 8)]
dot_range = ['.', '']

##############################################################################
# Shortcuts
##############################################################################

r = lambda x: random.randint(0, x)

def r2(x):
    while(True):
        point_1 = r(x)
        point_2 = r(x)

        if point_1 != point_2:
            break

    if point_1 > point_2:
        point_1, point_2 = point_2, point_1

    return point_1, point_2

##############################################################################
# Generators
##############################################################################

def random_gene():
    pitch = random.choice(pitch_range)
    duration = random.choice(duration_range)
    octave = random.choice(octave_range)
    dot = random.choice(dot_range)

    return (duration + pitch + octave + dot)

def random_genome():
    genome = []

    for i in xrange(GENOME_LENGTH):
        genome.append(random_gene())

    return genome

##############################################################################
# Crossover operators
##############################################################################

def one_point_crossover(father, mother):
    point = r(GENOME_LENGTH -1)
    
    child_1 = father[:point] + mother[point:]
    child_2 = mother[:point] + father[point:]

    return child_1, child_2

def two_point_crossover(father, mother):
    point_1, point_2 = r2(GENOME_LENGTH - 1)
    
    child_1 = father[:point_1] + mother[point_1:point_2] + father[point_2:]
    child_2 = mother[:point_1] + father[point_1:point_2] + mother[point_2:]

    return child_1, child_2

def uniform_crossover(father, mother):
    pool = father + mother
    random.shuffle(pool)
    
    return pool[:GENOME_LENGTH], pool[GENOME_LENGTH:]

##############################################################################
# Mutation operators
##############################################################################

def swap_mutation(genome):
    point_1, point_2 = r2(GENOME_LENGTH - 1)

    genome[point_1], genome[point_2] = genome[point_2], genome[point_1]

def replace_mutation(genome):
    point = r(GENOME_LENGTH - 1)
    genome[point] = random_gene()

def scramble_mutation(genome):
    point_1, point_2 = r2(GENOME_LENGTH - 1)

    temp = genome[point_1:point_2]
    random.shuffle(temp)

    genome[point_1:point_2] = temp

def inversion_mutation(genome):
    point_1, point_2 = r2(GENOME_LENGTH - 1)

    temp = genome[point_1:point_2]
    temp.reverse()
    genome[point_1:point_2] = temp

crossover_operators = [one_point_crossover, two_point_crossover, uniform_crossover]
mutation_operators = [swap_mutation, replace_mutation, scramble_mutation, inversion_mutation]

random_crossover = lambda x, y: random.choice(crossover_operators)(x, y)
random_mutator = lambda x: random.choice(mutation_operators)(x)

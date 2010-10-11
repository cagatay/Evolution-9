'''
Created on Oct 5, 2010
 
@author: cagatay.yuksel
'''

from random import randrange
from random import random

from evolution9.midi.midiActions import createMIDI
from evolution9.evolution.storage import db

if __name__ == '__main__':
    db.initDatabase()
    composition = list()

    for i in range(10):
        pitch = randrange(40, 80)
        duration = random()
        composition.append((duration, pitch))
    
    createMIDI('output.mid', composition)
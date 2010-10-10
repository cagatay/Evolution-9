'''
Created on Oct 5, 2010
 
@author: cagatay.yuksel
'''

from random import randrange

from evolution9.midi.midiActions import createMIDI

composition = list()

for i in range(10):
    pitch = randrange(40, 80)
    composition.append((1, pitch))

createMIDI('output.mid', composition)
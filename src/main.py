'''
Created on Oct 6, 2010
 
@author: cagatay.yuksel
'''

from random import randrange
from random import random

from evolution9.midi.midiActions import createMIDI
from evolution9.evolution.storage import db
from pybrain.tools.shortcuts import buildNetwork
from mingus.midi.MidiFileIn import MIDI_to_Composition
from mingus.midi.MidiFileOut import write_Composition
from mingus.containers import *
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
import mingus.core.notes as notes
import RTTL
import os
import constants
from NN import NN



if __name__ == '__main__':
    songList = RTTL.parse(constants.INPUT_DIR + "beatles.txt")
    

    currentNN = NN("yeni",3,3)
    
    currentNN.train(songList[0])
    
    currentNN.saveNetworkToFile()
    
    
    
    
    
    
    
    
#    for song in list:
#        track = Track()
#        
#        for note in song.notes:
#            if not note[1]:
#                track.add_notes(None, note[0])
#            else:
#                currentNote = int(Note(note[1], note[2]))
#                track.add_notes(Note(note[1], note[2]), note[0])
#        composition = Composition()
#        composition.add_track(track)
#        composition.set_title(song.name)
#        write_Composition(constants.OUTPUT_DIR + song.name + ".mid", composition, song.bpm)
#    defDuration = 4
#    defOctave = 5
#    beat = 180
#    
#    track = Track()
#    track.add_notes("C#", 8)
#    track.add_notes("D", 8)
#    track.add_notes("C#", 8)
#    track.add_notes("E", defDuration)
#    track.add_notes(None, defDuration)
#    track.add_notes("E", defDuration)
#    track.add_notes(None, 8)
#    track.add_notes("E", defDuration)
#    track.add_notes(None, defDuration)
#    track.add_notes("E", 8)
#    
#    composition = Composition()
#    composition.add_track(track)
    
#    write_Composition(constants.OUTPUT_DIR + "1.mid", composition, beat)
#    midiFiles = os.listdir(constants.INPUT_DIR)
#    compositions = list()
#    
#    for fileName in midiFiles:
#        
#        (composition, beat) = MIDI_to_Composition(constants.INPUT_DIR + fileName)
#        #composition.add_note("C#")
#        write_Composition(constants.OUTPUT_DIR + fileName, composition, beat)
#        #compositions.append(composition)
#    
    
#    storage =  db.Database()
#    storage.initDatabase()
#    storage.printAll()
#    composition = list()
#
#
#    for i in range(10):
#        pitch = randrange(40, 80)
#        duration = random()
#        composition.append((duration, pitch))
    

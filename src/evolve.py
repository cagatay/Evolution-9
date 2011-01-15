#!/usr/bin/env python
'''
Created on Oct 6, 2010
 
@author: cagatay
'''

from random import randrange
from random import random

from evolution9.midi.midiActions import createMIDI
from evolution9.evolution.storage import db
from pybrain.tools.shortcuts import buildNetwork
from mingus.midi.MidiFileIn import MIDI_to_Composition
from mingus.midi.MidiFileOut import write_Track
from mingus.containers import *
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
import mingus.core.notes as notes
import mingus.core.value as value
import RTTL
import os
import constants
from NN import NN



if __name__ == '__main__':
    
    '''
    currentNN = NN("yeni",3,1)
    
    for song in songList:
        currentNN.addSong( song )
    
    currentNN.train()
    
    currentNN.saveNetworkToFile()
    
    #currentNN.readNetworkFromFile()
    
    songList = RTTL.parse(constants.INPUT_DIR + "metallica.txt")
    
    sonuc = currentNN.fitness( songList[0] )
    
    print sonuc
    
    sonuc = currentNN.fitness( songList[1] )
    
    print sonuc
    
    songList = RTTL.parse(constants.INPUT_DIR + "beatles.txt")
    
    sonuc = currentNN.fitness( songList[6] )
    
    print sonuc
    
    '''

    songs = RTTL.parse(constants.INPUT_DIR + "beatles.txt")
    for song in songs:
        track = Track()
        
        for n in song.track:
            track.add_notes(n.note, value.dots(n.duration, n.dot))
        write_Track(constants.OUTPUT_DIR + song.name + ".mid", track, song.tempo)
    
#    storage =  db.Database()
#    storage.initDatabase()
#    storage.printAll()
#    composition = list()

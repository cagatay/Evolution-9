#!/usr/bin/env python
'''
Created on Oct 6, 2010
 
@author: cagatay
'''

from pybrain.tools.shortcuts import buildNetwork
from mingus.midi.MidiFileIn import MIDI_to_Composition
from mingus.midi.MidiFileOut import write_Track
from mingus.containers import *
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
import mingus.core.notes as notes
import os
import constants
from brain import NN

def main():

    while(True):
        pass

if __name__ == '__main__':
    songs = RTTL.parse(constants.INPUT_DIR + "beatles.txt")
    for song in songs:
        track = Track()
        
        for n in song.track:
            track.add_notes(n.note, value.dots(n.duration, n.dot))
        write_Track(constants.OUTPUT_DIR + song.name + ".mid", track, song.tempo)

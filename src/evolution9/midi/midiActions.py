'''
Created on Oct 11, 2010

@author: cagatay.yuksel
'''

from evolution9.midi.MidiFile3 import MIDIFile
from evolution9.constants import OUTPUT_DIR

def createMIDI(filename, notes):
    midi = MIDIFile(1)
    track = 0
    time = 0
    tempo = 200
    channel = 0
    volume = 100
    
    midi.addTrackName(track, time, "track")
    midi.addTempo(track, time, tempo)
    
    for duration, pitch in notes:
        midi.addNote(track, channel, pitch, time, duration, volume)
        time += duration
    
    fileHandle = open(OUTPUT_DIR + filename, "wb")
    midi.writeFile(fileHandle)
    fileHandle.close()

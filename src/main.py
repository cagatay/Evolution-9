#===============================================================================
# Created on Oct 5, 2010
# 
# @author: cagatay
#===============================================================================

#Import the library
from midiutil.MidiFile3 import MIDIFile

# Create the MIDIFile Object with 1 track
MyMIDI = MIDIFile(1)

# Tracks are numbered from zero. Times are measured in beats.
track = 0
time = 0

# Add track name and tempo.
MyMIDI.addTrackName(track, time, "Sample Track")
MyMIDI.addTempo(track, time, 120)

# Add a note. addNote expects the following information:
track = 0
channel = 0
pitch = 60
time = 0
duration = 1
volume = 100

# Now add the note.
MyMIDI.addNote(track, channel, pitch, time, duration, volume)
MyMIDI.addNote(track, channel, pitch, time+1, duration, volume)
MyMIDI.addNote(track, channel, 70, time+2, duration, volume)
MyMIDI.addNote(track, channel, 80, time+3, duration, volume)
# And write it to disk.
binfile = open("../output/output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()


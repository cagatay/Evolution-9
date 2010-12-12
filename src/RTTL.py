'''
Created on 12 Ara 2010

@author: melih
'''

def parse(fileName):
    file = open(fileName)
    songList = list()
    
    
    for line in file:
        line = line.rstrip()
        noteList = list()
        parts = line.split(":")
        name = parts[0]
        defaults = parts[1]
        notes = parts[2]
        
        
        defaults = defaults.split(",")
        defaultDuration = int(defaults[0].split("=")[1])
        defaultOctave = int(defaults[1].split("=")[1])
        bpm = int(defaults[2].split("=")[1])
        
        
        notes = notes.split(",")
        for note in notes:
            note = note.upper()
            noteDuration = defaultDuration
            noteOctave = defaultOctave
            if note[0].isdigit():
                if note[1].isdigit():
                    noteDuration = int(note[:2])
                    note = note[2:]
                else:
                    noteDuration = int(note[0])
                    note = note[1:]
            if note[len(note) - 1].isdigit():
                noteOctave = int(note[len(note) - 1])
                note = note[0:len(note) - 1]
            
            if note.endswith("."):
                noteDuration = noteDuration * 1.5
                note = note[0:len(note) - 1]
            if note == "P":
                note = None
                
            noteList.append((noteDuration, note, noteOctave))
            
        rttl = RTTL()
        rttl.name = name
        rttl.notes = noteList
        rttl.bpm = bpm
        songList.append(rttl)
    
    return songList   
                
class RTTL:
    name = ""
    
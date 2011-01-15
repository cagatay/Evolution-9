'''
Created on 12 Ara 2010

@author: melih
'''

def parse(fileName):
    file = open(fileName)
    songs = list()
    
    
    for line in file:
        line = line.rstrip()
        track = list()
        parts = line.split(":")
        name = parts[0]
        defaults = parts[1]
        notes = parts[2]
        
        
        defaults = defaults.split(",")
        defaultDuration = int(defaults[0].split("=")[1])
        defaultOctave = int(defaults[1].split("=")[1])
        tempo = int(defaults[2].split("=")[1])
        
        
        notes = notes.split(",")
        for n in notes:
            n = n.upper()
            duration = defaultDuration
            octave = defaultOctave
            dot = 0
            if n[0].isdigit():
                if n[1].isdigit():
                    duration = int(n[:2])
                    n = n[2:]
                else:
                    duration = int(n[0])
                    n = n[1:]
            if n[len(n) - 1].isdigit():
                octave = int(n[len(n) - 1])
                n = n[0:len(n) - 1]
            
            if n.endswith("."):
                dot = 1
                n = n[0:len(n) - 1]
            if n == "P":
                n = None
                
            track.append(note(duration, n, octave, dot))
            
        songs.append(song(name, track, tempo))
    
    return songs   
                
class song:
     def __init__(self, name, track, tempo):
         self.name = name
         self.track = track
         self.tempo = tempo
class note:
     def __init__(self, duration, note, octave, dot):
         self.duration = duration
         self.note = note
         if self.note:
             self.note += '-' + str(octave)
         self.dot = dot

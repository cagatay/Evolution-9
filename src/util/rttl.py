'''
Created on 12 Ara 2010

@author: melih
'''

from util.music import note

def parse(rttl_string):
    rttl_string = rttl_string.strip()
    track = []
    parts = rttl_string.split(":")
    defaults = parts[1]
    notes = parts[2]
    
    if defaults:
        defaults = defaults.split(",")
        defaultDuration = int(defaults[0].split("=")[1])
        defaultOctave = int(defaults[1].split("=")[1])
    
    notes = notes.split(",")
    for n in notes:
        n = n.strip().upper()
        if defaults:
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
        if n.endswith("."):
            dot = 1
            n = n[0:len(n) - 1]
        if n[len(n) - 1].isdigit():
            octave = int(n[len(n) - 1])
            n = n[0:len(n) - 1]
        
        if n == "P":
            n = None
            
        track.append(note(n, duration, octave, dot))
        
    return track

def dump(note_list):
    out = '::'

    for note in note_list:
        out += str(note) + ','

    return out.rstrip(',')

def to_int(note_list):
    return [x.int_tuple() for x in note_list]

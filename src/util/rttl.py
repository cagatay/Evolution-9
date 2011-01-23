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
        defaultDuration = defaults[0].split("=")[1]
        defaultOctave = defaults[1].split("=")[1]
    
    notes = notes.split(",")
    for n in notes:
        n = n.strip().upper()
        if defaults:
            duration = defaultDuration
            octave = defaultOctave
        dot = ''
        if n[0].isdigit():
            if n[1].isdigit():
                duration = n[:2]
                n = n[2:]
            else:
                duration = n[0]
                n = n[1:]
        if n[len(n) - 1].isdigit():
            octave = n[len(n) - 1]
            n = n[0:len(n) - 1]
        if n.endswith("."):
            dot = '.'
            n = n[0:len(n) - 1]

        track.append(note(n, duration, octave, dot))
    return track

def dataset_from_file(file_uri):
    ds_file = file(file_uri)
    ds_list = []

    for line in ds_file:
        track = parse(line)
        ds_list.append(to_int(track))

    return ds_list

def dump(note_list):
    out = '::'

    for note in note_list:
        out += str(note) + ','

    return out.rstrip(',')

def to_int(note_list):
    return [x.int_tuple() for x in note_list]

import random

from mingus.containers.Note import Note
from mingus.core import value

note_range = ['P', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
duration_range = [str(2**x) for x in range(6)]
octave_range = [str(x) for x in range(4, 8)]
dot_range = ['.', '']

class note(object):
    def __init__(self, note, octave, duration, dot):
        self.note = note
        self.octave = octave
        self.duration = duration
        self.dot = dot

    def int_tuple(self):
        return (int(Note(self.note + '-' + self.octave)),
                value.dots(self.duration, int(bool(self.dot))))

    def __str__(self):
        return self.duration + self.note + self.octave + self.dot

def random_note():
    return note(random.choice(note_range),
                random.choice(octave_range),
                random.choice(duration_range),
                random.choice(dot_range))

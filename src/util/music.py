import random

from mingus.containers.Note import Note

note_range = ['P', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
duration_range = [str(2**x) for x in range(6)]
octave_range = [str(x) for x in range(4, 8)]

class note(object):
    def __init__(self, note, octave, duration):
        self.note = str(note)
        self.octave = '' if octave is None else octave
        self.duration = duration
        self.mingus_duration = int(duration)

        if self.note == 'P':
            self.mingus_note = None
        else:
            self.mingus_note = Note(self.note, int(self.octave))

    def int_tuple(self):
        return (int(self.mingus_note) if self.mingus_note else 0, self.mingus_duration)

    def __str__(self):
        return self.duration + self.note + self.octave

def random_note():
    return note(random.choice(note_range),
                random.choice(octave_range),
                random.choice(duration_range))

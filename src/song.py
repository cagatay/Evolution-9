from mingus.containers.Track import Track
from mingus.core import value

import util.RTTL

class Song(Track):
    def __init__(self, string):
        super.__init__()

        song = RTTL.parse(string)
        
        for item in song.track:
            self.add_notes(item.note, value.dots(item.duration, item.dot))

        self._notes = list()
        for bar in self:
            for item in bar:
                self.notes.append(int(item[2]), float(1/item[1]))

        @property
        def notes(self):
            return self._notes

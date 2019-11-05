import frequencies as fqs
from midiutil import MIDIFile
import numpy as np
import sys



arr = np.array(sys.argv[1:])
arr = arr.astype(np.int)

key = fqs.getMajorKey(69)

degrees = [key[degree] for degree in arr]
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 100   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(degrees):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
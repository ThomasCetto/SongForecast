from midiutil.MidiFile import MIDIFile



def clamp(n, min, max):
    return min if n < min else max if n > max else n



# create your MIDI object
mf = MIDIFile(1)     # only 1 track
track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 120)

# add some notes
channel = 0
volume = 10

import random

pitch = 45

import math

rand = lambda x: math.cos(2 * x) + math.sin(math.pi * x)

for i in range(1000):
    pitch = 50 + int(((rand(i/12)/2 + 0.2) * 15))
    pitch = clamp(pitch, 0, 255)
    time = i*0.75 + abs(rand(i/8)) / 3
    duration = abs(rand(i/5)) + 0.1
    mf.addNote(track, channel, pitch, time, duration, volume)

# write it to disk
with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)


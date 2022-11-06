musicSource = "midiFiles"
firstFilePath = "midiFiles/MIDI-Unprocessed_01_R1_2006_01-09_ORIG_MID--AUDIO_01_R1_2006_01_Track01_wav.midi"
secondFilePath = "midiFiles/ORIG-MIDI_03_7_6_13_Group__MID--AUDIO_09_R1_2013_wav--2.midi"

from mido import MidiFile
import os

allFiles = os.listdir(musicSource)
ind = 0
for file in allFiles:
    mid = MidiFile(f"{musicSource}/{file}", clip=True)
    mid.tracks.remove(mid.tracks[0])
    mid.save(f"midiFiles/{ind}.midi")
    ind += 1
    print(ind)
    




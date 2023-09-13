# this is the starting point for making a song using classes
# we can run this to produce a wav file with a song

import note
import song

duration = 1 # notes must be divisible by duration
note_data = [
"c4", 0.25, "C2", 0.5, "d3", 0.25, "d2", 1,
"a2", 0.5, "c2", 0.25, "C3", 0.25, "g3", 1,
]

notes = []
# build note objects using note_data
i = 0
while i < len(note_data)-1:
  notes.append(note.note(note_data[i], note_data[i+1]))
  i+=2

#simplesong = song.song(notes, duration, "simplesong")
#simplesong.randomize_and_save_song()

simplesong = song.song([], duration, "simplesong")
simplesong.make_random_notes(100)
simplesong.save_song()

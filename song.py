# this class represents a song
# a song has a collection of notes

import note as nt
import numpy as np
from scipy.io import wavfile
import random as ra
import utils

class song:
    def __init__(self, notes, durationseconds, filename):
        self.notes = notes
        self.durationseconds = durationseconds
        self.filename = filename

        # envelope properties and magic numbers
        self.factor = [0.68, 0.26, 0.03, 0.0, 0.03]
        self.length = [0.01, 0.6, 0.29, 0.1]
        self.decay = [0.05, 0.02, 0.005, 0.1]
        self.sustain_level = 0.05
        self.bar_factor = 2
        self.bit_rate = 44100
        self.dividend = 4096
    

    def set_names_and_durations(self):
        # take the notes list and make two lists for the utils function
        self.note_names = [note.name for note in self.notes]
        self.note_durations = [note.duration for note in self.notes]
    
    def outputwav(self, note_names, note_durations):
        # this method will get song data and output a wav file
        self.print_notes_code()
        songdata = utils.get_song_data(note_names, note_durations, self.bar_factor,
                                 self.factor, self.length, self.decay, self.sustain_level)
        
        data = songdata * (self.dividend/np.max(songdata))
        wavfile.write(f'data/{self.filename}.wav', self.bit_rate, data.astype(np.int16))
        return
    
    def print_notes_code(self):
        for i in range(len(self.note_names)):
            print(f'"{self.note_names[i]}", {self.note_durations[i]},')

    def save_song(self):
        self.set_names_and_durations()
        self.outputwav(self.note_names, self.note_durations)
    

    def randomize_and_save_song(self):

        self.set_names_and_durations()

        # randomize
        ra.shuffle(self.note_names)
        ra.shuffle(self.note_durations)

        self.outputwav(self.note_names, self.note_durations)
        return
    
    def get_piano_keys():
        return utils.get_keys()

    def make_random_notes(self, even_note_amount):
        assert even_note_amount % 2 == 0

        # given a target amount of notes, make up notes
        durations = [0.25, 0.5, 1]
        all_possible_notes = utils.get_keys()
        
        # trim off more extreme values
        trim_start = 28
        trim_end = len(all_possible_notes) - trim_start
        all_possible_notes = all_possible_notes[trim_start:trim_end]

        notes = []
        i = 0
        durations_sum = 0

        while i < even_note_amount:
            notename = ra.choice(all_possible_notes)
            noteduration = ra.choice(durations)
            durations_sum += noteduration
            notes.append(nt.note(notename, noteduration))
            i += 1

        # durations must sum to a whole, even number 
        # given the current sustain implementation
        attempts = 0
        max_attempts = 10

        while durations_sum % 2 != 0:
            # reduce some of the .5 notes by .25
            for note in notes:
                if note.duration == 0.5:
                    note.duration = 0.25
                    break

            durations_sum -= 0.25

            if attempts == max_attempts:
                break

        self.notes = notes

        return

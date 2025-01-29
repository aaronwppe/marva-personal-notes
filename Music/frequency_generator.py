# this module is meant to be a utility module for the music algorithm
import pandas as pd

# default frequency - C note in 4th octave
c4_freq = 261.63

western_notes = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
hindustani_notes = ('S', 'kR', 'R', 'kG', 'G', 'M', 'tM', 'P', 'kD', 'D', 'kN', 'N')

# This is a reference dictionary for all the hindustani notes' full names
# hindustani_note_names = {'S': 'Shadj',
#                          'kR': 'Komal Rishab',
#                          'R': 'Suddh Rishab',
#                          'kG': 'Komal Gandhar',
#                          'G': 'Suddh Gandhar',
#                          'M': 'Suddh Madhyam',
#                          'tM': 'Tivra Madhyam',
#                          'P': 'Pancham',
#                          'kD': 'Komal Dhaivat',
#                          'D': 'Suddh Dhaivat',
#                          'kN': 'Komal Nishad',
#                          'N': 'Suddh Nishad'}

# value that is to be multiplied to get next semitone
freq_multiplier = 2 ** (1/12)

# Function to generate frequencies of a single specified octave
def generate_octave_frequencies(start_freq=c4_freq, octave=4):
    freq = start_freq
    
    df = pd.DataFrame(columns=['Octave', 'Western Note', 'Hindustani Note', 'Frequency'])
    
    # set frequency of first note (C)
    df.loc[0] = [octave, western_notes[0], hindustani_notes[0], freq]

    # set frequencies for remaining notes (D to B)
    for western_note, hindustani_note in zip(western_notes[1:], hindustani_notes[1:]):
        freq *= freq_multiplier
        df.loc[len(df)] = [octave, western_note, hindustani_note, freq]
    
    return df

# Function to generate frequencies for notes in multiple octaves
# stop_octave parameter is exclusive
def generate_frequencies(start_freq, start_octave, stop_octave):
    freq = start_freq
    df_list = []
    
    for octave in range(start_octave, stop_octave):
        df = generate_octave_frequencies(freq, octave)
        freq = df.iloc[-1]['Frequency'] * freq_multiplier
        df_list.append(df)
        
    return pd.concat(df_list, ignore_index=True)
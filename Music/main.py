import frequency_generator as fg
import synthesizer
import pandas as pd

Note = fg.Note
Melody = fg.Melody

# C note in 4th octave
c4_freq = 261.626

### Generate frequencies of Sa('S') and Re('R1') note ###

# define the symbols
# refer to source link in frequency_generator module comments section for notation rules
Sa_symbol = 'S'
Re_symbol = 'R1'

# define corresponding Note objects
Sa_note = Note(Sa_symbol)
Re_note = Note(Re_symbol)

notes_tuple = (Sa_note, Re_note)

# generate our frequency dataframe 
df = fg.generate_frequencies_df(root_freq=c4_freq, notes=notes_tuple)\

# Uncomment to print generated dataframe
# print(df)

###################################################



### Another way to generate frequencies of Sa('S') and Re('R1') ###

notes_tuple = Note.str_to_notes(('S', 'R1'))
df = fg.generate_frequencies_df(root_freq=c4_freq, notes=notes_tuple)\

# Uncomment to print generated dataframe
# print(df)

###################################################



###  Generate 3 octave piano frequencies ###
octave_notes = fg.swara_notes

octave1 = [f'.{n.shruti_symbol}' for n in octave_notes]
# same as octave1 = ['.S', '.r2', '.R1', '.g2', '.G1', '.M1', '.m1', '.P', '.d2', '.D1', '.n2', '.N1']
# dot character before symbol means previous octave (Mandra)

octave2 = [n.shruti_symbol for n in octave_notes]
# same as octave2 = ['S', 'r2', 'R1', 'g2', 'G1', 'M1', 'm1', 'P', 'd2', 'D1', 'n2', 'N1']
# no dot character means current octave (Madhya)

octave3 = [f'{n.shruti_symbol}.' for n in octave_notes]
# same as octave3 = ['S.', 'r2.', 'R1.', 'g2.', 'G1.', 'M1.', 'm1.', 'P.', 'd2.', 'D1.', 'n2.', 'N1.']
# dot charcter after symbol means next octave (Taar)

all_octave_tuple = tuple(octave1 + octave2 + octave3)

# Returns a tuple of all the Note objects
all_octave_notes = Note.str_to_notes(all_octave_tuple)

df = fg.generate_frequencies_df(c4_freq, all_octave_notes)

# Uncomment to print 3 octave piano frequencies
# print(df)

###################################################



### Working with Raags ###

# define notes of all the raags
sargam_aroha = fg.sargam_notes 
sargam_avaroha = fg.sargam_notes[::-1]

yaman_raag_aroha = Note.str_to_notes(('.N1', 'R1', 'G1', 'm1', 'D1', 'N1', 'S.'))
yaman_raag_avaroha = Note.str_to_notes(('S.', 'N1', 'D1', 'P', 'm1', 'G1', 'R1', 'S'))

bhairavi_raag_aroha = Note.str_to_notes(('S', 'r2', 'G1', 'M1', 'P', 'd2', 'N1', 'S.'))
bhairavi_raag_avaroha = bhairavi_raag_aroha[::-1]

# define raags
sargam = Melody(sargam_aroha, sargam_avaroha)
yaman_raag = Melody(yaman_raag_aroha, yaman_raag_avaroha)
bhairavi_raag = Melody(bhairavi_raag_aroha, bhairavi_raag_avaroha)

# function to use synthesizer to play melody(raag) notes
def play_melody(melody: Melody, root_freq=c4_freq):
    up = fg.generate_frequencies_df(root_freq, notes=melody.ascending_scale)
    down = fg.generate_frequencies_df(root_freq, notes=melody.descending_scale)

    df = pd.concat([up, down], ignore_index=True)

    with synthesizer.Synthesizer() as synth:
        for freq_shruti in df['Freq_Shruti_Hz']:
            print(freq_shruti)
            synth.play_frequency(freq_shruti, 1.0)


# Uncomment any of the below lines to play the raga
# play_melody(bhairavi_raag)
# play_melody(yaman_raag)
# play_melody(sargam)

###################################################
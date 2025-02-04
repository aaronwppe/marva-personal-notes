from enum import Enum
import pandas as pd

'''
Notations and frequency ratios are taken from the source below

source: Vivek Bansod, & Mohit Sharma. (2019). 
    Mathematical Approach for Twenty-Two Microtones: Frequency Ratios in Hindustani Classical Music 
    & their Implementation in 22 Shruti Harmonium. 
    International Journal of Mathematics And Its Applications, 7(1), 245-252. 
    Retrieved from https://ijmaa.in/index.php/ijmaa/article/view/288
'''

'''
Notation rules for Saptak
    (1) dot character before symbol implies previous octave (Mandra)
    (2) no dot character implies current octave (Madhya)
    (3) dot charcter after symbol means next octave (Taar)
'''

# Defining Western musical notes as an Enum
class WesternNote(Enum):
    C = 'C'
    Cs = 'C#'
    D = 'D'
    Ds = 'D#'
    E = 'E'
    F = 'F'
    Fs = 'F#'
    G = 'G'
    Gs = 'G#'
    A = 'A'
    As = 'A#'
    B = 'B'

# Defining Hindustani classical Shrutis as an Enum
class Shruti(Enum):
    S  = 'S'
    r1 = 'r1'
    r2 = 'r2'
    R1 = 'R1'
    R2 = 'R2'
    g1 = 'g1'
    g2 = 'g2'
    G1 = 'G1'
    G2 = 'G2'
    M1 = 'M1'
    M2 = 'M2'
    m1 = 'm1'
    m2 = 'm2'
    P  = 'P'
    d1 = 'd1'
    d2 = 'd2'
    D1 = 'D1'
    D2 = 'D2'
    n1 = 'n1'
    n2 = 'n2'
    N1 = 'N1'
    N2 = 'N2'

# Enum for the three octaves (Saptaks) in Hindustani music
class Saptak(Enum):
    MANDRA = 1
    MADHYA = 2
    TAAR = 3

# Mapping Saptak Enum to readable names
saptak_names = {
    Saptak.MANDRA : 'Mandra',
    Saptak.MADHYA : 'Madhya',
    Saptak.TAAR : 'Taar'
}

# Western notes ordered by semitone position (used for frequency calculations)
western_notes_order = {
    WesternNote.C : 0,
    WesternNote.Cs : 1,
    WesternNote.D : 2,
    WesternNote.Ds : 3,
    WesternNote.E: 4,
    WesternNote.F: 5,
    WesternNote.Fs: 6,
    WesternNote.G: 7,
    WesternNote.Gs: 8,
    WesternNote.A: 9,
    WesternNote.As: 10,
    WesternNote.B: 11
}

# Shruti details including name and corresponding Swara
shruti_names = {
    Shruti.S  : {'shruti': None, 'swara': 'Shadja'},
    Shruti.r1 : {'shruti': 'Atikomal', 'swara': 'Rishabh'},
    Shruti.r2 : {'shruti': 'Komal', 'swara': 'Rishabh'},
    Shruti.R1 : {'shruti': 'Shuddha', 'swara': 'Rishabh'},
    Shruti.R2 : {'shruti': 'Teevra', 'swara': 'Rishabh'},
    Shruti.g1 : {'shruti': 'Atikomal', 'swara': 'Gandhar'},
    Shruti.g2 : {'shruti': 'Komal', 'swara': 'Gandhar'},
    Shruti.G1 : {'shruti': 'Shuddha', 'swara': 'Gandhar'},
    Shruti.G2 : {'shruti': 'Teevra', 'swara': 'Gandhar'},
    Shruti.M1 : {'shruti': 'Shuddha', 'swara': 'Madhyam'},
    Shruti.M2 : {'shruti': 'Ekashruti', 'swara': 'Madhyam'},
    Shruti.m1 : {'shruti': 'Teevra', 'swara': 'Madhyam'},
    Shruti.m2 : {'shruti': 'Teevratama', 'swara': 'Madhyam'},
    Shruti.P  : {'shruti': None, 'swara': 'Pancham'},
    Shruti.d1 : {'shruti': 'Atikomal', 'swara': 'Dhaivat'},
    Shruti.d2 : {'shruti': 'Komal', 'swara': 'Dhaivat'},
    Shruti.D1 : {'shruti': 'Shuddha', 'swara': 'Dhaivat'},
    Shruti.D2 : {'shruti': 'Teevra', 'swara': 'Dhaivat'},
    Shruti.n1 : {'shruti': 'Atikomal', 'swara': 'Nishad'},
    Shruti.n2 : {'shruti': 'Komal', 'swara': 'Nishad'},
    Shruti.N1 : {'shruti': 'Shuddha', 'swara': 'Nishad'},
    Shruti.N2 : {'shruti': 'Teevra', 'swara': 'Nishad'}
}

# Mapping Shrutis to Western notes
shruti_to_western_map = {
    Shruti.S  : WesternNote.C,

    Shruti.r1 : WesternNote.Cs,
    Shruti.r2 : WesternNote.Cs,

    Shruti.R1 : WesternNote.D,
    Shruti.R2 : WesternNote.D,

    Shruti.g1 : WesternNote.Ds,
    Shruti.g2 : WesternNote.Ds,

    Shruti.G1 : WesternNote.E,
    Shruti.G2 : WesternNote.E,

    Shruti.M1 : WesternNote.F,
    Shruti.M2 : WesternNote.F,

    Shruti.m1 : WesternNote.Fs,
    Shruti.m2 : WesternNote.Fs,

    Shruti.P  : WesternNote.G,

    Shruti.d1 : WesternNote.Gs,
    Shruti.d2 : WesternNote.Gs,

    Shruti.D1 : WesternNote.A,
    Shruti.D2 : WesternNote.A,

    Shruti.n1 : WesternNote.As,
    Shruti.n2 : WesternNote.As,

    Shruti.N1 : WesternNote.B,
    Shruti.N2 : WesternNote.B
}

# Reverse mapping Western notes to Shrutis
western_to_shruti_map = {v: k for k, v in shruti_to_western_map.items()}


# value that is to be multiplied to get next semitone
# this is based on the 12-Tone Equal Temperament (12-TET) Tuning
# western tuning
semitone_freq_multiplier = 2 ** (1 / 12)

# value that is to be multiplied to get next microtone(shruti)
shruti_freq_multipliers = {
    Shruti.S : 1,            
    Shruti.r1: 256 / 243,
    Shruti.r2: 16 / 15,
    Shruti.R1: 10 / 9,   
    Shruti.R2: 9 / 8,   
    Shruti.g1: 32 / 27,
    Shruti.g2: 6 / 5,   
    Shruti.G1: 5 / 4,
    Shruti.G2: 81 / 64,   
    Shruti.M1: 4 / 3,   
    Shruti.M2: 27 / 20,   
    Shruti.m1: 45 / 32,   
    Shruti.m2: 729 / 512, 
    Shruti.P : 3 / 2,         
    Shruti.d1: 128 / 81,   
    Shruti.d2: 8 / 5,   
    Shruti.D1: 5 / 3,
    Shruti.D2: 27 / 16, 
    Shruti.n1: 16 / 9,   
    Shruti.n2: 9 / 5,    
    Shruti.N1: 15 / 8,
    Shruti.N2: 243 / 128
}

# Multipliers for different octaves (Saptaks)
saptak_multipliers = {
    Saptak.MANDRA : 0.5,    # Lower octave (1/2 frequency)
    Saptak.MADHYA : 1.0,    # Middle octave (original frequency)
    Saptak.TAAR   : 2.0     # Higher octave (2x frequency)
}

# Default frequency (A4 = 440Hz)
a4_freq = 440.00

class Note:
    def __init__(self, shruti_symbol):
        self.shruti_symbol = shruti_symbol
        self.saptak = self.get_saptak(self.shruti_symbol)
        self.shruti = Shruti[self.shruti_symbol.strip('.')]

        self.western_note = self.get_western_note(self.shruti)
        self.western_symbol = self.western_note.value

    @staticmethod
    def get_saptak(symbol):
        if symbol.startswith('.'):
            saptak = Saptak.MANDRA

        elif symbol.endswith('.'):
            saptak = Saptak.TAAR
        
        else:
            saptak = Saptak.MADHYA
        
        return saptak
    
    @property
    def saptak_name(self):
        return saptak_names[self.saptak]

    @property
    def saptak_multiplier(self):
        return saptak_multipliers[self.saptak]
    
    def get_shruti_freq(self, root_freq):
        freq_multiplier = shruti_freq_multipliers[self.shruti]

        return self.saptak_multiplier * (root_freq * freq_multiplier)
    
    def get_western_freq(self, root_freq):
        order = western_notes_order[self.western_note]
        return root_freq * (2 ** (order / 12)) * self.saptak_multiplier
    
    @property
    def shruti_name(self):
        return shruti_names[self.shruti]['shruti']
    
    @property
    def swara_name(self):
        return shruti_names[self.shruti]['swara']
    
    @classmethod
    def str_to_notes(cls, str_tuple: tuple[str]):
        return tuple(Note(s) for s in str_tuple)
    
    @staticmethod
    def get_western_note(shruti):
        return shruti_to_western_map.get(shruti, None)

    
# Class representation of a raaga
class Melody:
    def __init__(self, ascending_scale: tuple[Note], descending_scale: tuple[Note]):
        self.ascending_scale = ascending_scale
        self.descending_scale = descending_scale

swara_notes = tuple(Note(shruti.value) for shruti in 
                        [Shruti.S, Shruti.r2, Shruti.R1, Shruti.g2, 
                         Shruti.G1, Shruti.M1, Shruti.m1, Shruti.P, 
                         Shruti.d2, Shruti.D1, Shruti.n2, Shruti.N1
                        ]
                    )   

sargam_notes = Note.str_to_notes(('S', 'R1', 'G1', 'M1', 'P', 'D1', 'N1', 'S.'))


# Generates a frequency table for given notes
def generate_frequencies_df(root_freq=a4_freq, notes=sargam_notes):

    df = pd.DataFrame(columns=['Saptak', 'Western_Symbol', 'Hindustani_Symbol', 'Shruti', 'Swara', 'Freq_12TET_Hz', 'Freq_Shruti_Hz'])
    
    for note in notes:
        freq_shruti = note.get_shruti_freq(root_freq)
        freq_western = note.get_western_freq(root_freq)

        df.loc[len(df)] = [note.saptak_name, note.western_symbol, note.shruti_symbol, note.shruti_name, note.swara_name, freq_western, freq_shruti]
    
    return df
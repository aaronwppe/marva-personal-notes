import pyaudio
import numpy as np

class Synthesizer:
    # Custom harmonics for a more tanpura-like sound
    tanpura_harmonics = [
        (1.0, 1.0),    # fundamental
        (0.5, 2.0),    # second harmonic
        (0.3, 3.0),    # third harmonic
        (0.2, 4.0),    # fourth harmonic
        (0.1, 5.0)     # fifth harmonic
    ]

    def __init__(self, harmonics=tanpura_harmonics):
        self.harmonics = harmonics
            
        self.p = pyaudio.PyAudio()
        self.sample_rate = 44100
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.p.terminate()
        
    def generate_harmonic_tone(self, frequency, duration):        
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)
        samples = np.zeros_like(t, dtype=float)
        
        # Add each harmonic
        for amplitude, harmonic_ratio in self.harmonics:
            samples += amplitude * np.sin(2 * np.pi * frequency * harmonic_ratio * t)
            
        # Normalize
        samples = samples / np.max(np.abs(samples))
        
        # Apply envelope
        envelope = np.ones_like(samples)
        attack = int(0.02 * self.sample_rate)  # 20ms attack
        decay = int(0.05 * self.sample_rate)   # 50ms decay
        envelope[:attack] = np.linspace(0, 1, attack)
        envelope[-decay:] = np.linspace(1, 0, decay)
        
        return (samples * envelope).astype(np.float32)
    
    def play_frequency(self, frequency, duration):
        samples = self.generate_harmonic_tone(frequency, duration)
        
        stream = self.p.open(format=pyaudio.paFloat32,
                           channels=1,
                           rate=self.sample_rate,
                           output=True)
        
        stream.write(samples.tobytes())
        stream.stop_stream()
        stream.close()
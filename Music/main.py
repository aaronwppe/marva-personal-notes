# this is a demo to the frequency_generator module

# To import this module you must have pandas installed
import frequency_generator as fg

# we will use this as our starting frequency
# C note in 3rd octave
c3_freq = 130.813

# we will generate frequencies of octave 3, octave 4 and octave 5
# so our range as start and stop will be (3, 6) as stop is exclusive
df = fg.generate_frequencies(start_freq=c3_freq, start_octave=3, stop_octave=6)

print(df)

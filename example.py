'''
writes a .wav file

you may need to install some libs with commands like
>> python3 -m pip install numpy
>> python3 -m pip install scipy
>> python3 -m pip install matplotlib
'''
from scipy.io.wavfile import write
import numpy as np
samplerate = 44100

# initial frequency (pitch)
freq = 220 

duration_seconds = 3
t = np.linspace(0., duration_seconds, duration_seconds * samplerate)
amplitude = np.iinfo(np.int16).max

data = amplitude * np.sin(2. * np.pi * freq * t)

# try changing the values of data, frequency, or duration!
#data = amplitude * np.sin(2. * np.pi * freq * t * t)
#data = amplitude * np.sin(2. * np.pi * freq * t * t) * np.sin(2. * np.pi * freq * t * t)
#freq = 8000; data = amplitude * -np.sin(2. * -np.pi * freq * t * t) * -np.sin(2. * np.pi * freq * t * t)
#data = data * data

write("data/example.wav", samplerate, data.astype(np.int16))
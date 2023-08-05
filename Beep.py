import pyaudio
import wave
import numpy as np
from math import pi

def make_sinewave(frequency, length, sample_rate=44100):
    length = int(length * sample_rate)
    factor = int(frequency) * (pi * 2) / sample_rate
    waveform = np.sin(np.arange(length) * factor)

    return waveform

def save_wave_file(filename, waveform, sample_rate=44100):
    wave_data = (waveform * 32767).astype(np.int16)  # Convert float waveform to int16
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframesraw(wave_data.tobytes())

if __name__ == "__main__":
    p = pyaudio.PyAudio()

    sinewave = make_sinewave(500, 1)

    output_filename = "beep.wav"
    save_wave_file(output_filename, sinewave)

    p.terminate()

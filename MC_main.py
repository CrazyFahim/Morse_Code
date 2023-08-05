import pyaudio
import wave
import time

import numpy as np
from math import pi

p1 = ""

# Define Morse code dictionary for A-Z
morse_code_dict = {
    'A': '.-', 
    'B': '-...', 
    'C': '-.-.', 
    'D': '-..', 
    'E': '.', 
    'F': '..-.',
    'G': '--.',
    'H': '....', 
    'I': '..', 
    'J': '.---', 
    'K': '-.-', 
    'L': '.-..', 
    'M': '--', 
    'N': '-.',
    'O': '---', 
    'P': '.--.', 
    'Q': '--.-', 
    'R': '.-.', 
    'S': '...', 
    'T': '-', 
    'U': '..-',
    'V': '...-', 
    'W': '.--', 
    'X': '-..-', 
    'Y': '-.--', 
    'Z': '--..'
}

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

def morse_code_to_wave(morse_code, frequency=500, unit_duration=0.1, sample_rate=44100):
    # Convert Morse code to sine wave
    waveform = np.array([])

    for symbol in morse_code:
        if symbol == '.':
            wave = make_sinewave(frequency, unit_duration * 1)
        elif symbol == '-':
            wave = make_sinewave(frequency, unit_duration * 5)
        else:  # symbol is a space
            wave = np.zeros(int(sample_rate * unit_duration))

        waveform = np.concatenate([waveform, wave, np.zeros(int(sample_rate * unit_duration))])

    return waveform

if __name__ == "__main__":
    p = pyaudio.PyAudio()

    for letter, morse_code in morse_code_dict.items():
        output_filename = f"{letter}_morse.wav"
        wave_data = morse_code_to_wave(morse_code)
        save_wave_file(output_filename, wave_data)

    p.terminate()


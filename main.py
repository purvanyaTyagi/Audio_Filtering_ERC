import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

sample_rate, modulated = wavfile.read("modulated_noisy_audio.wav")

if modulated.ndim > 1:
    modulated = modulated[:, 0]
print(modulated.shape)

# # Normalize to [-1, 1]
modulated = modulated / np.max(np.abs(modulated))

N = len(modulated)

plt.figure(figsize=(10, 5))
time = np.linspace(0, N / sample_rate, N)
plt.plot(time, modulated)
plt.title("Time Spectrum of Modulated Signal")
plt.xlabel("time (s)")
plt.ylabel("Magnitude")


fft_result = np.fft.fft(modulated) # complex numbers are returned
frequencies = np.fft.fftfreq(N, d=1/sample_rate)
magnitude = np.abs(fft_result)

half = N // 2
frequencies = frequencies[:half]
magnitude = magnitude[:half]

peak_index = np.argmax(magnitude)
carrier_freq = frequencies[peak_index]

print(f"Estimated carrier frequency (Fc): {carrier_freq:.2f} Hz")


plt.figure(figsize=(10, 5))
plt.plot(frequencies, magnitude)
plt.title("Frequency Spectrum of Modulated Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()


carrier = np.cos(2 * np.pi * carrier_freq * (1 / sample_rate) * np.arange(len(modulated)))
demodulated = carrier*modulated

plt.figure(figsize=(10, 5))
time = np.linspace(0, N / sample_rate, N)
plt.plot(time, demodulated)
plt.title("time Spectrum of demodulated Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()

fft_result_demodulated = np.fft.fft(demodulated) # complex numbers are returned
frequencies_demodulated = np.fft.fftfreq(N, d=1/sample_rate)
magnitude_demodulated = np.abs(fft_result_demodulated)

plt.figure(figsize=(10, 5))
plt.plot(frequencies_demodulated, magnitude_demodulated)
plt.title("Frequency Spectrum of demodulated Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()

from scipy.signal import butter, sosfilt
from scipy.signal import butter, filtfilt
from scipy.signal import hilbert


import numpy as np

def bandstop_filter(data, lowcut, highcut, fs, order=5):
    sos = butter(order, [lowcut, highcut], btype='bandstop', fs=fs, output='sos')
    filtered = sosfilt(sos, data)
    return filtered

def butter_lowpass_filter(data, cutoff, sample_rate, order=5):
    nyquist = 0.5 * sample_rate
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered = filtfilt(b, a, data)
    return filtered

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs                  # Nyquist frequency
    low = lowcut / nyq              # Normalize low cutoff
    high = highcut / nyq            # Normalize high cutoff
    b, a = butter(order, [low, high], btype='band')  # Design filter
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order)
    y = filtfilt(b, a, data)  # Apply filter forward and backward
    return y

def frequency_shift(signal, sample_rate, f_shift):
    t = np.arange(len(signal)) / sample_rate
    analytic_signal = hilbert(signal)  # Get analytic version (complex-valued)
    shifted = np.real(analytic_signal * np.exp(2j * np.pi * f_shift * t))  # Multiply by complex exponential
    return shifted





lowcut = 1000.0     # Lower cutoff frequency in Hz
highcut = 1200.0   # Upper cutoff frequency in Hz

clean_signal = bandpass_filter(demodulated, 1000, 1200, sample_rate)
clean_signal = frequency_shift(clean_signal, sample_rate, -500)  # Shift back to baseband

# clean_signal = bandstop_filter(demodulated, lowcut, highcut, sample_rate)
# clean_signal = butter_lowpass_filter(clean_signal, 1200, sample_rate)

fft_result_clean = np.fft.fft(clean_signal) # complex numbers are returned
frequencies_clean = np.fft.fftfreq(N, d=1/sample_rate)
magnitude_clean = np.abs(fft_result_clean)

plt.figure(figsize=(10, 5))
plt.plot(frequencies_clean, magnitude_clean)
plt.title("Frequency Spectrum of Modulated_clean Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()

from scipy.io.wavfile import write
import numpy as np

# Parameters
clean_signal = np.array(clean_signal)  # ensure it's a NumPy array

# If the signal is in float [-1, 1], convert to int16
scaled = np.int16(clean_signal / np.max(np.abs(clean_signal)) * 32767)

# Save to WAV file
write("clean_output_real_real.wav", sample_rate, scaled)





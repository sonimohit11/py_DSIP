import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio, display

# Set audio file path
AUDIO_PATH = r"D:\College\SEM 5\DSIP\OPE4\song.mp3"

# Check file
if not os.path.isfile(AUDIO_PATH):
   raise FileNotFoundError(f"Audio file not found: {AUDIO_PATH}")

# Load audio
y, sr = librosa.load(AUDIO_PATH, sr=None, mono=True)

# Calculate audio information
duration = len(y) / sr

print(f"File: {os.path.basename(AUDIO_PATH)}")
print(f"Sampling rate: {sr} Hz")
print(f"Duration: {duration:.2f} seconds")
print(f"Nyquist frequency: {sr / 2:.0f} Hz")

# Plot original audio waveform
plt.figure(figsize=(12, 3))
time = np.arange(len(y)) / sr

plt.plot(time, y, linewidth=0.5)
plt.title("Original Audio - Time Domain")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()

# Display audio player
display(Audio(y, rate=sr))

# ----------------------------------------------------------------

# Part 2: Low-Pass Filtered Audio Spectrograms

import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import soundfile as sf
from scipy.signal import butter, sosfiltfilt
from IPython.display import Audio, display
import os

# Output folder
output_dir = r"D:\College\SEM 5\DSIP\OPE4"
os.makedirs(output_dir, exist_ok=True)

# Cutoff frequencies
cutoff_frequencies = [500, 1500, 3000]

# Store filtered audio
filtered_signals = {}

for cutoff in cutoff_frequencies:

   # Design Butterworth low-pass filter
   sos = butter(
     6,
     cutoff,

       btype="lowpass",
       fs=sr,
       output="sos"
   )

   # Apply filter
   filtered_audio = sosfiltfilt(sos, y)
   filtered_signals[cutoff] = filtered_audio

   # Plot spectrogram
   D = librosa.amplitude_to_db(
     np.abs(librosa.stft(filtered_audio, n_fft=2048)),
     ref=np.max
   )

   plt.figure(figsize=(12, 4))

   librosa.display.specshow(
      D,
      sr=sr,
      x_axis="time",
      y_axis="hz",
      cmap="magma"
   )

   plt.ylim(0, 10000)
   plt.colorbar(format="%+2.0f dB")
   plt.title(f"Low-Pass Filtered Audio - Cutoff {cutoff} Hz")
   plt.tight_layout()
   plt.show()

   # Save filtered audio
   output_path = os.path.join(
     output_dir, f"lowpass_{cutoff}Hz.wav"
   )

   sf.write(output_path, filtered_audio, sr)
   print("Saved:", output_path)

   # Play filtered audio
   print(f"Audio playback: {cutoff} Hz")
   display(Audio(filtered_audio, rate=sr))

# ----------------------------------------------------------------

# Part 3: Frequency Spectrum Comparison

import numpy as np
import matplotlib.pyplot as plt

# Function to calculate and plot frequency spectrum
def plot_frequency_spectrum(signal, sr, label):

   # Calculate Fourier Transform
   fft_values = np.fft.rfft(signal)
   frequencies = np.fft.rfftfreq(
      len(signal), d=1 / sr
   )

   # Convert magnitude to decibels
   magnitude = np.abs(fft_values)
   magnitude_db = 20 * np.log10(
     magnitude / (np.max(magnitude) + 1e-12) + 1e-12
   )

   # Plot spectrum
   plt.plot(frequencies, magnitude_db, label=label)

# Plot original and filtered spectra
plt.figure(figsize=(12, 5))

plot_frequency_spectrum(y, sr, "Original Audio")

for cutoff, filtered_audio in filtered_signals.items():
  plot_frequency_spectrum(
     filtered_audio,
     sr,
     f"Low-Pass {cutoff} Hz"
  )

plt.title("Frequency Spectrum Comparison")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB, normalized)")
plt.xlim(0, sr / 2)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------------------------------------------------

# Part 4: Band-Pass Filtering (300-3400 Hz)

import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import soundfile as sf
from scipy.signal import butter, sosfiltfilt
from IPython.display import Audio, display
import os

# Set output folder
output_dir = r"D:\College\SEM 5\DSIP\OPE4"
os.makedirs(output_dir, exist_ok=True)

# Design sixth-order Butterworth band-pass filter
low_cutoff = 300
high_cutoff = 3400

sos = butter(
  6,
  [low_cutoff, high_cutoff],
  btype="bandpass",
  fs=sr,
  output="sos"

)

# Apply filter to original audio
bandpass_audio = sosfiltfilt(sos, y)

# Save band-pass output
output_path = os.path.join(
  output_dir, "bandpass_300_3400Hz.wav"
)

sf.write(output_path, bandpass_audio, sr)
print("Saved:", output_path)

# Calculate spectrogram
D = librosa.amplitude_to_db(
  np.abs(librosa.stft(bandpass_audio, n_fft=2048)),
  ref=np.max
)

# Display spectrogram
plt.figure(figsize=(12, 4))

librosa.display.specshow(
   D,
   sr=sr,
   x_axis="time",
   y_axis="hz",
   cmap="magma"
)

plt.ylim(0, 10000)
plt.colorbar(format="%+2.0f dB")
plt.title("Band-Pass Output (300-3400 Hz)")
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency (Hz)")
plt.tight_layout()
plt.show()

# Play filtered audio
display(Audio(bandpass_audio, rate=sr))

# ----------------------------------------------------------------

# Part 5: Residual Background Estimation

import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import soundfile as sf
import os
from IPython.display import Audio, display

# Set output folder
output_dir = r"D:\College\SEM 5\DSIP\OPE4"
os.makedirs(output_dir, exist_ok=True)

# Calculate residual signal
# Original audio minus band-pass-filtered audio
residual_audio = y - bandpass_audio

# Save residual audio
output_path = os.path.join(
  output_dir, "residual_background_estimate.wav"
)

sf.write(output_path, residual_audio, sr)

print("Residual audio saved:", output_path)

# Calculate spectrogram

D = librosa.amplitude_to_db(
  np.abs(librosa.stft(residual_audio, n_fft=2048)),
  ref=np.max
)

# Plot residual spectrogram
plt.figure(figsize=(12, 4))

librosa.display.specshow(
   D,
   sr=sr,
   x_axis="time",
   y_axis="hz",
   cmap="magma"
)

plt.ylim(0, 10000)
plt.colorbar(format="%+2.0f dB")
plt.title("Residual Background Estimate")
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency (Hz)")
plt.tight_layout()
plt.show()

# Play residual audio
display(Audio(residual_audio, rate=sr))

# ----------------------------------------------------------------

# Part 6: Audio Playback and Saved Output Confirmation

import os
import soundfile as sf
from IPython.display import Audio, display

# Folder where output files are saved
output_dir = r"D:\College\SEM 5\DSIP\OPE4"

# List of output audio files
output_files = [
  "lowpass_500Hz.wav",
  "lowpass_1500Hz.wav",
  "lowpass_3000Hz.wav",
  "bandpass_300_3400Hz.wav",
  "residual_background_estimate.wav"
]

print("Saved Audio Files Confirmation")
print("--------------------------------")

for filename in output_files:

   file_path = os.path.join(output_dir, filename)

   if os.path.isfile(file_path):
      info = sf.info(file_path)

       print(f"\nFile: {filename}")
       print(f"Status: Saved successfully")
       print(f"Duration: {info.duration:.2f} seconds")
       print(f"Sampling rate: {info.samplerate} Hz")

       # Load and play audio
       data, sample_rate = sf.read(file_path)

      print("Playing:", filename)
      display(Audio(data.T if data.ndim == 2 else data,
                rate=sample_rate))
   else:
      print(f"\nFile: {filename}")
      print("Status: File not found. Run the corresponding filter cell first.")

print("\nAudio output verification completed.

# ----------------------------------------------------------------

import os
import numpy as np
import pandas as pd
import soundfile as sf
from IPython.display import display

output_dir = r"D:\College\SEM 5\DSIP\OPE4"
audio_files = {
   "Original Audio": os.path.join(output_dir, "song.mp3"),
   "Low-pass 500 Hz": os.path.join(output_dir, "lowpass_500Hz.wav"),
   "Low-pass 1500 Hz": os.path.join(output_dir, "lowpass_1500Hz.wav"),
   "Low-pass 3000 Hz": os.path.join(output_dir, "lowpass_3000Hz.wav"),
   "Band-pass 300–3400 Hz": os.path.join(output_dir, "bandpass_300_3400Hz.wav"),
   "Residual Audio": os.path.join(output_dir, "residual_background_estimate.wav")
}
results = []
for name, path in audio_files.items():
   if not os.path.exists(path):
      print(f"File not found: {path}")
      continue

   audio, sample_rate = sf.read(path)

   if audio.ndim > 1:
      audio = audio.mean(axis=1)

   duration = len(audio) / sample_rate
   peak_amplitude = np.max(np.abs(audio))
   rms_amplitude = np.sqrt(np.mean(audio ** 2))

   results.append({
      "Audio Type": name,
      "Sampling Rate (Hz)": sample_rate,
      "Duration (seconds)": round(duration, 2),
      "Peak Amplitude": round(float(peak_amplitude), 4),
      "RMS Amplitude": round(float(rms_amplitude), 4)
   })

comparison_df = pd.DataFrame(results)
display(comparison_df)

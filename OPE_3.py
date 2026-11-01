import imageio_ffmpeg
from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate

# FFmpeg path
AudioSegment.converter = imageio_ffmpeg.get_ffmpeg_exe()
# Function to load first 60 seconds
def load_audio(filename):
  audio = AudioSegment.from_file(filename)
  # Keep first 60 seconds
  audio = audio[:60000]
  # Convert to mono
  audio = audio.set_channels(1)
  # Reduce sample rate
  audio = audio.set_frame_rate(8000)
  # Convert to numpy array
  samples = np.array(audio.get_array_of_samples(), dtype=np.float32)
  # Normalize
  samples = samples / np.max(np.abs(samples))
  return samples

# Load your files
original = load_audio("Warning.mp3")
karaoke = load_audio("Justin Bieber ka.mp3")
different = load_audio("Justin Bieber o.mp3")


# Equal length
min_len = min(len(original), len(karaoke), len(different))
original = original[:min_len]
karaoke = karaoke[:min_len]
different = different[:min_len]

# Pearson Correlation
corr_ok = np.corrcoef(original, karaoke)[0,1]
corr_od = np.corrcoef(original, different)[0,1]
corr_kd = np.corrcoef(karaoke, different)[0,1]
print("\nCorrelation Results")
print("-----------------------------")
print("Original vs Karaoke :", round(corr_ok,4))
print("Original vs Different :", round(corr_od,4))
print("Karaoke vs Different :", round(corr_kd,4))
# Cross Correlation
cross_ok = correlate(original, karaoke, mode="same")
cross_od = correlate(original, different, mode="same")
cross_kd = correlate(karaoke, different, mode="same")
# Normalize
cross_ok = cross_ok / np.max(np.abs(cross_ok))
cross_od = cross_od / np.max(np.abs(cross_od))
cross_kd = cross_kd / np.max(np.abs(cross_kd))

# Plot
plt.figure(figsize=(12,10))
plt.subplot(3,1,1)
plt.plot(cross_ok)
plt.title("Cross Correlation: Original vs Karaoke")
plt.grid(True)
plt.subplot(3,1,2)
plt.plot(cross_od)
plt.title("Cross Correlation: Original vs Different")
plt.grid(True)
plt.subplot(3,1,3)
plt.plot(cross_kd)
plt.title("Cross Correlation: Karaoke vs Different")
plt.grid(True)
plt.tight_layout()
plt.show()

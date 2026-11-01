from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Load MP3 file
audio = AudioSegment.from_mp3("Hopeless.mp3")

# Convert to mono
audio = audio.set_channels(1)
samples = np.array(audio.get_array_of_samples()).astype(np.float32)

# Normalize original signal
samples_norm = samples / np.max(np.abs(samples))

# Define 5 different kernels
kernels = [
    np.array([1, 0, 1, 0, 1], dtype=np.float32),
    np.array([10, 208, 100, 208, 120], dtype=np.float32),
    np.array([50, 100, 150, 100, 255], dtype=np.float32),
    np.array([124, 210, 146, 80, 200], dtype=np.float32),
    np.array([255, 255, 255, 255, 255], dtype=np.float32)
]

# Apply each kernel
for i, kernel in enumerate(kernels, start=1):
    print(f"\\nApplying Kernel {i}: {kernel}")

    # Perform convolution
    convoluted = convolve(samples, kernel, mode='same')

    # Normalize
    convoluted = convoluted / np.max(np.abs(convoluted))
    convoluted_int16 = (convoluted * 32767).astype(np.int16)

    # Create AudioSegment
    convoluted_audio = AudioSegment(
        convoluted_int16.tobytes(),
        frame_rate=audio.frame_rate,
        sample_width=2,
        channels=1
    )

    # Save WAV file
    output_file = f"output_convoluted_{i}.wav"
    convoluted_audio.export(output_file, format="wav")
    print(f"Saved: {output_file}")

    # Plot
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(samples_norm, color='blue')
    plt.title("Original Audio Signal")
    plt.subplot(2, 1, 2)
    plt.plot(convoluted, color='red')
    plt.title(f"Convoluted Audio Signal\\nKernel {i}: {kernel.tolist()}")
    plt.tight_layout()
    plt.show()

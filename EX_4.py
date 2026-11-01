import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import butter, bilinear, cheby1, lfilter

    # Sampling parameters
    fs = 8000
    N = 1024
    n = np.arange(N)

    # Frequencies in Hz
    f1 = 1000
    f2 = 2000
    f3 = 3000
    f4 = 4000

    # Generate discrete sine waves
    x1 = np.sin(2 * np.pi * f1 * n / fs)
    x2 = np.sin(2 * np.pi * f2 * n / fs)
    x3 = np.sin(2 * np.pi * f3 * n / fs)
    x4 = np.sin(2 * np.pi * f4 * n / fs)

    # Plot first 32 samples of each signal
    n_plot = n[:32]

    plt.figure(figsize=(10, 10))

    plt.subplot(4, 1, 1)
    plt.stem(n_plot, x1[:32])


    plt.title("Discrete Sine Wave - 1 kHz")
    plt.xlabel("Sample n")
    plt.ylabel("Amplitude")
    plt.grid()

    plt.subplot(4, 1, 2)
    plt.stem(n_plot, x2[:32])
    plt.title("Discrete Sine Wave - 2 kHz")
    plt.xlabel("Sample n")
    plt.ylabel("Amplitude")
    plt.grid()

    plt.subplot(4, 1, 3)
    plt.stem(n_plot, x3[:32])
    plt.title("Discrete Sine Wave - 3 kHz")
    plt.xlabel("Sample n")
    plt.ylabel("Amplitude")
    plt.grid()

    plt.subplot(4, 1, 4)
    plt.stem(n_plot, x4[:32])
    plt.title("Discrete Sine Wave - 4 kHz")
    plt.xlabel("Sample n")
    plt.ylabel("Amplitude")
    plt.grid()

    plt.tight_layout()
    plt.show()
# ----------------------------------------------------------------

x = x1 + x2 + x3 + x4
    # Plot combined signal in discrete time domain
    plt.figure(figsize=(10, 5))
    plt.stem(n[:32], x[:32])
    plt.title("Sum of 1 kHz, 2 kHz, 3 kHz and 4 kHz Signals")
    plt.xlabel("Sample n")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.tight_layout()


    plt.show()
    X = np.fft.rfft(x)
    freq = np.fft.rfftfreq(N, d=1/fs)

    magnitude = 2 * np.abs(X) / N
    magnitude[0] /= 2
    plt.figure(figsize=(10, 5))
    plt.stem(freq, magnitude)
    plt.xlim(0, fs/2)
    plt.title("Frequency Domain of Added Signal")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid()
    plt.tight_layout()
    plt.show()

order = 4
    cutoff_butter = 2000 # Cutoff frequency = 2 kHz

    analog_cutoff = 2 * fs * np.tan(
      np.pi * cutoff_butter / fs
    )

    analog_b, analog_a = butter(
       order,
       analog_cutoff,
       analog=True,
       btype='low'
    )
    digital_b, digital_a = bilinear(
       analog_b,
       analog_a,
       fs
    )
    y_butter = lfilter(
       digital_b,
       digital_a,
       x
    )
    plt.figure(figsize=(10, 5))
    plt.stem(n[:32], y_butter[:32])
    plt.title("Butterworth Filter Output - Time Domain")
    plt.xlabel("Sample n")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.tight_layout()
    plt.show()

    start = 200
    butter_signal = y_butter[start:]

    Y_butter = np.fft.rfft(butter_signal)
    freq_butter = np.fft.rfftfreq(
       len(butter_signal),
       d=1/fs
    )


    magnitude_butter = (
      2 * np.abs(Y_butter) / len(butter_signal)
    )
    magnitude_butter[0] /= 2

    # Plot frequency domain
    plt.figure(figsize=(10, 5))
    plt.stem(freq_butter, magnitude_butter)
    plt.xlim(0, fs/2)
    plt.title("Butterworth Filter Output - Frequency Domain")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid()
    plt.tight_layout()
    plt.show()

# ----------------------------------------------------------------

cutoff_cheby = 3000 # Cutoff frequency = 3 kHz
    ripple = 0.5    # Passband ripple in dB

    analog_cutoff = 2 * fs * np.tan(
      np.pi * cutoff_cheby / fs
    )

    analog_b, analog_a = cheby1(
      order,
      ripple,
      analog_cutoff,
      analog=True,
      btype='low'
    )

    digital_b, digital_a = bilinear(
      analog_b,
      analog_a,
      fs
    )

    y_cheby = lfilter(
      digital_b,
      digital_a,
      x
    )

    plt.figure(figsize=(10, 5))
    plt.stem(n[:32], y_cheby[:32])
    plt.title("Chebyshev Filter Output - Time Domain")
    plt.xlabel("Sample n")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.tight_layout()
    plt.show()
    cheby_signal = y_cheby[start:]
    Y_cheby = np.fft.rfft(cheby_signal)
    freq_cheby = np.fft.rfftfreq(
       len(cheby_signal),
       d=1/fs
    )

    magnitude_cheby = (
      2 * np.abs(Y_cheby) / len(cheby_signal)
    )
    magnitude_cheby[0] /= 2

    plt.figure(figsize=(10, 5))
    plt.stem(freq_cheby, magnitude_cheby)
    plt.xlim(0, fs/2)
    plt.title("Chebyshev Filter Output - Frequency Domain")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid()
    plt.tight_layout()
    plt.show()
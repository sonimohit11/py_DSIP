      import numpy as np
     import matplotlib.pyplot as plt
     from scipy.signal import firwin, freqz
     N = 31
     Fs = 10000
     window_type = 'hann'

     # 1. FIR Low-Pass Filter
     b_lpf = firwin(
        numtaps=N,
        cutoff=3000,
        window=window_type,
        pass_zero='lowpass',
        fs=Fs
     )
     # 2. FIR High-Pass Filter
     b_hpf = firwin(
        numtaps=N,
        cutoff=3000,
        window=window_type,
        pass_zero='highpass',
        fs=Fs
     )
     Fs_band = 20000

     # 3. FIR Band-Pass Filter
     b_bpf = firwin(
        numtaps=N,
        cutoff=[3000, 6000],
        window=window_type,
        pass_zero='bandpass',
        fs=Fs_band
     )
     b_bsf = firwin(
        numtaps=N,
        cutoff=[3000, 6000],
        window=window_type,
        pass_zero='bandstop',
        fs=Fs_band
     )
     filters = [
        ("FIR Low-Pass Filter (Fc = 3 kHz)", b_lpf, Fs),
        ("FIR High-Pass Filter (Fc = 3 kHz)", b_hpf, Fs),
        ("FIR Band-Pass Filter (3-6 kHz)", b_bpf, Fs_band),
        ("FIR Band-Stop Filter (3-6 kHz)", b_bsf, Fs_band)
     ]
     plt.figure(figsize=(12, 9))

     for i, (title, b, fs) in enumerate(filters, start=1):
        f, H = freqz(b, worN=2048, fs=fs)

        magnitude_db = 20 * np.log10(
           np.maximum(np.abs(H), 1e-10)
        )
        plt.subplot(2, 2, i)
        plt.plot(f / 1000, magnitude_db)
        plt.title(title)
        plt.xlabel("Frequency (kHz)")
        plt.ylabel("Magnitude (dB)")
        plt.grid(True)

     plt.tight_layout()
     plt.show()

     # Display filter coefficients
     print("LOW-PASS FILTER COEFFICIENTS:")
     print(b_lpf)

     print("\nHIGH-PASS FILTER COEFFICIENTS:")
     print(b_hpf)

     print("\nBAND-PASS FILTER COEFFICIENTS:")
     print(b_bpf)

     print("\nBAND-STOP FILTER COEFFICIENTS:")
     print(b_bsf)
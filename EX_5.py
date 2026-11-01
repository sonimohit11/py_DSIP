#define the discrete-time signal
    signal = np.array([1,2,3,4,5,6,7,8])

    #compute the FFT of the signal
    fft_result = np.fft.fft(signal)

    #compute the magnitude
    magnitude_spectrum = np.abs(fft_result)

    #compute the phase
    phase_spectrum = np.angle(fft_result)

    #compute the IFFT to reconstruct the original signal

    reconstructed_signal = np.fft.ifft(fft_result)

    sample_index = np.arange(len(signal))

    #create plot
    plt.figure(figsize=(12,8))

    #plot the original signal
    plt.subplot(2,2,1)
    plt.stem(sample_index,signal)
    plt.title('Original Signal')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.subplot(2,2,2)
    plt.stem(sample_index,magnitude_spectrum)
    plt.title('Original Signal')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.subplot(2,2,3)
    plt.stem(sample_index,phase_spectrum)
    plt.title('Original Signal')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.subplot(2,2,4)
    plt.stem(sample_index,reconstructed_signal)
    plt.title('Original Signal')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True)

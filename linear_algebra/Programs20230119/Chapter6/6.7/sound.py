from numpy import arange, fft
import scipy.io.wavfile as wav


class Sound:
    def __init__(self, wavfile):
        self.file = wavfile
        self.rate, Data = wav.read(f'{wavfile}.wav')
        dt = 1 / self.rate
        self.len = len(Data)
        self.tmax = self.len / self.rate
        self.time = arange(0, self.tmax, dt)
        self.data = Data.astype('float') / 32768
        self.fft = fft.fft(self.data)

    def power_spectrum(self, rng=None):
        spectrum = abs(self.fft) ** 2
        if rng is None:
            r1, r2 = -self.len / 2, self.len / 2
        else:
            r1, r2 = rng[0] * self.tmax, rng[1] * self.tmax
        R = arange(int(r1), int(r2))
        return R / self.tmax, spectrum[R]

    def lowpass(self, K):
        k = int(K * self.tmax)
        U = self.fft.copy()
        U[range(k + 1, self.len - k)] = 0
        V = fft.ifft(U).real
        Data = (V * 32768).astype('int16')
        wav.write(f'{self.file}{K}.wav', self.rate, Data)
        return V

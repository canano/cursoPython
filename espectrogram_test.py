'''
Created on 02/06/2015

@author: Fernando
'''
#!/usr/bin/env python
#             Script que realiza el espectrograma de una serie temporal
#
#                           Argumento: nombre del fichero de entrada
#
import matplotlib.pyplot as plt
import sys
from numpy import *
from pylab import *

# Comprueba si hay fichero de entrada:

if len(sys.argv) != 2:
    print " falta fichero de entrada \n"
    sys.exit(0)

# leer los datos como float
x =  loadtxt(sys.argv[1], dtype=float )
n = len(x)  # length of the signal

dt = 1.
t = arange(0.0, n, dt)

# FFT of this
Fs = 1 / dt  # sampling rate, Fs = 1/1'
k = arange(n)
T = n / Fs
frq = k / T  # two sides frequency range
frq = frq[range(n / 2)]  # one side frequency range
Y = fft(x) / n  # fft computing and normalization
Y = Y[range(n / 2)] / max(Y[range(n / 2)])

print n

# Graficos de la serie temporal, y el espectrograma:

# Grafico de serie temporal: (comparte el eje x con el espectrograma)
ax1 = subplot(211)

# plotting the data
subplot(2, 1, 1)

plt.plot(t[0:n] , x[0:n], 'r')
title('Filtered sea level - Langosteira')
xlabel('Time (minutes)')
ylabel('Amplitude (mm)')
grid()
#Conseguimos que la longitud de ambos ejes se ajuste al tamano de la senal representada
plt.axis('tight')
# plotting the spectrogram (sharing the abscisas with plot 1):
#Si al segundo diagrama le quitamos la dependencia con el primero en el eje de las X, tambien ajustamos el espectro a sus valores;
# si no, nos saldra un espacio en blanco  -- subplot(2, 1, 2, sharex = ax1)
subplot(2, 1, 2)

Pxx, freqs, bins, im = specgram(x, NFFT=256, detrend=mlab.detrend_none, Fs=Fs, noverlap=10)
#xlabel('Time (min)')
#ylabel('Freq (1/min)'
#Conseguimos que la longitud de ambos ejes se ajuste al tamano de la senal representada
plt.axis('tight')
plt.savefig('image.png')
plt.show()

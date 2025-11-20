import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# PARÁMETROS
# -------------------------------
N = 8              # número de bits
fs = 1000          # frecuencia de muestreo [Hz]
Tb = 1             # duración de cada bit [s]
t = np.arange(0, N*Tb, 1/fs)  # vector de tiempo total

# Frecuencias de cada bit
f1 = 5   # frecuencia para bit 1
f2 = 2   # frecuencia para bit 0

# -------------------------------
# SECUENCIA DE BITS
# -------------------------------
bits = np.random.randint(0, 2, N)
print("Bits transmitidos:", bits)

# -------------------------------
# GENERACIÓN DE LA SEÑAL 2FSK
# -------------------------------
fsk_signal = np.zeros_like(t)

for i, bit in enumerate(bits):
    # intervalo temporal del bit actual
    t_bit = np.arange(i*Tb, (i+1)*Tb, 1/fs)
    if bit == 1:
        fsk_signal[i*fs*Tb:(i+1)*fs*Tb] = np.cos(2*np.pi*f1*t_bit)
    else:
        fsk_signal[i*fs*Tb:(i+1)*fs*Tb] = np.cos(2*np.pi*f2*t_bit)

# -------------------------------
# GRÁFICA
# -------------------------------
plt.figure(figsize=(10,6))

plt.subplot(2,1,1)
plt.step(np.arange(N), bits, where='post')
plt.ylim(-0.5, 1.5)
plt.title("Bits transmitidos")
plt.ylabel("Bit")
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(t, fsk_signal)
plt.title("Señal 2-FSK modulada (BFSK)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)

plt.tight_layout()
plt.show()
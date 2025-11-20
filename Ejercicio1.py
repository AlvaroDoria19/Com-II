import numpy as np
import matplotlib.pyplot as plt

def calcular_snr_pcm(n, Pe):
    """
    Calcula la SNR en dB para un sistema PCM considerando
    ruido de cuantización y errores de bit.
    Formula: SNR = 2^(2n) / (1 + 4 * Pe * 2^(2n))
    """
    numerador = 2**(2*n)
    denominador = 1 + 4 * Pe * (2**(2*n))
    snr_lineal = numerador / denominador
    
    snr_db = 10 * np.log10(snr_lineal)
    return snr_db
pe = np.logspace(-7, -1, 200)
n_valores = [8]
plt.figure(figsize=(10, 6))
for n in n_valores:
    snr = calcular_snr_pcm(n, pe)
    plt.semilogx(pe, snr, label=f'PCM de {n} bits', linewidth=2)
plt.title(r'Relación Señal a Ruido (SNR) vs Probabilidad de Error ($P_e$)', fontsize=14)
plt.xlabel(r'Probabilidad de Error de Bit ($P_e$)', fontsize=12)
plt.ylabel('SNR Promedio (dB)', fontsize=12)
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.legend()
plt.annotate('Dominio de Ruido de Cuantización\n(SNR Constante)', 
             xy=(1e-6, 45), xytext=(1e-6, 30),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.annotate('Dominio de Errores de Canal\n(Caída de SNR)', 
             xy=(1e-2, 10), xytext=(1e-3, 5),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()
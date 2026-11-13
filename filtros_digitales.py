
1. Crear la señal de entrada
fs = 500
t = np.arange(0, 2, 1/fs)
senal = (
np.sin(2*np.pi*5*t) +
np.sin(2*np.pi*50*t) +np.sin(2*np.pi*120*t)


Agregar ruido blanco
np.random.seed(42)
ruido = np.random.normal(0, 0.5, len(t))
senal_ruidosa = senal + ruido

Diseñar los filtros Butterworth
Filtro pasa bajos: 20 Hz
pasa_bajos = butter(4, 20, btype='lowpass',
                    fs=fs, output='sos')
Filtro pasa altos: 80 Hz
pasa_altos = butter(4, 80, btype='highpass',
                    fs=fs, output='sos')
Filtro pasa bandas: 40 a 60 Hz
pasa_bandas = butter(4, [40, 60], btype='bandpass',
                     fs=fs, output='sos')
Aplicar los filtros
resultado_bajos = sosfiltfilt(pasa_bajos, senal_ruidosa)
resultado_altos = sosfiltfilt(pasa_altos, senal_ruidosa)
resultado_bandas = sosfiltfilt(pasa_bandas, senal_ruidosa)
Graficar las señales
plt.figure(figsize=(12, 10))

graficas = [
    (senal_ruidosa, "Señal original con ruido"),
    (resultado_bajos, "Filtro pasa bajos"),
    (resultado_altos, "Filtro pasa altos"),
    (resultado_bandas, "Filtro pasa bandas")
for i, (datos, titulo) in enumerate(graficas, 1):
    plt.subplot(4, 1, i)
    plt.plot(t, datos)
    plt.title(titulo)
    plt.xlabel("Tiempo (segundos)")
    plt.ylabel("Amplitud")
    plt.grid()
plt.tight_layout()
plt.show()Mostrar las respuestas en frecuencia
filtros = [
    (pasa_bajos, "Respuesta del filtro pasa bajos"),
    (pasa_altos, "Respuesta del filtro pasa altos"),
    (pasa_bandas, "Respuesta del filtro pasa bandas")
plt.figure(figsize=(10, 8))
for i, (fltro, titulo) in enumerate(filtros, 1):
    frecuencias, respuesta = sosfreqz(
        filtro, worN=2048, fs=fs    )
    magnitud = 20 * np.log10
        np.maximum(np.abs(respuesta), 1e-10)    plt.subplot(3, 1, i)
    plt.plot(frecuencias, magnitud)
    plt.title(titulo)
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud (dB)")
    plt.grid()
    plt.ylim(-80, 5)

plt.tight_layout()
plt.show()

print("Simulación finalizada correctamente.")


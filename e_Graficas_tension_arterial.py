"""
Programa de Visualización de Presión Arterial

Este programa grafica las presiones sistólica y diastólica utilizando la librería matplotlib.
La secuencia de datos muestra una evolución de la presión arterial de un estado normal a ligera
hipertensión, seguido de una disminución a valores ligeramente bajos y luego una recuperación a
niveles normales. Este ejemplo sirve para demostrar cómo los cambios en la presión arterial pueden
ser visualizados de manera efectiva usando gráficas de líneas.
"""

import matplotlib.pyplot as plt  # Importación del módulo para graficar

# Datos de presiones arteriales ajustados para mostrar una progresión realista
presiones_sistolica = [120, 125, 130, 135, 140, 135, 130, 125, 120, 115]
presiones_diastolica = [80, 82, 85, 88, 90, 85, 80, 78, 75, 73]

# Inicialización de la figura para la gráfica, especificando el tamaño de la misma
plt.figure(figsize=(10, 5))

# Creación de la línea para la presión sistólica, con puntos ('o') conectados por líneas ('-'), en color rojo ('r')
plt.plot(presiones_sistolica, 'r-o', label='Sistólica')

# Creación de la línea para la presión diastólica, similar a la sistólica pero en color azul ('b')
plt.plot(presiones_diastolica, 'b-o', label='Diastólica')

# Añadiendo un título a la gráfica
plt.title('Registro de Presión Arterial')

# Etiquetando el eje X
plt.xlabel('Número de Medición')

# Etiquetando el eje Y
plt.ylabel('Presión Arterial (mmHg)')

# Añadiendo una leyenda para identificar cada línea de manera clara
plt.legend()

# Activando la cuadrícula para facilitar la lectura de las mediciones
plt.grid(True)

# Mostrando la gráfica
plt.show()

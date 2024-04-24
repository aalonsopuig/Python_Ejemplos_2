"""
Programa de Registro de Presión Arterial
Este programa permite al usuario introducir las presiones arteriales sistólica y diastólica de un paciente de manera separada.
Los valores se almacenan en un archivo y, tras la recolección de datos, se pueden visualizar en una gráfica usando Matplotlib.
Esto facilita el seguimiento y la visualización de las tendencias en la presión arterial a lo largo del tiempo.
"""

import matplotlib.pyplot as plt # Se importa módulo para graficar
import os  # Se importa el módulo os para verificar la existencia del archivo

# Nombre del archivo donde se almacenarán las presiones
nombre_archivo = 'presiones_arteriales.txt'

# Verificar si el archivo ya existe
if os.path.exists(nombre_archivo):
    modo_apertura = 'a' 
else:
    modo_apertura = 'w' 

# Añadimos las presiones arteriales al archivo según se introducen por teclado
try:
    # Abrimos el archivo en el modo adecuado para almacenar los elementos
    archivo = open(nombre_archivo, modo_apertura, encoding='utf-8')
   
    while True:
        # Pedir al usuario que introduzca la presión sistólica o termine el proceso
        presion_sistolica = int(input("Introduce la presión arterial sistólica del paciente o escribe '0' para terminar: "))
        if presion_sistolica == 0:
            break
        # Pedir al usuario que introduzca la presión diastólica
        presion_diastolica = int(input("Introduce la presión arterial diastólica del paciente: "))
        # Añadir una nueva presión arterial al archivo
        archivo.write(f"{presion_sistolica}/{presion_diastolica}\n")
except IOError:
    print("Se produjo un error al introducir datos o escribir en el archivo.")
finally:
    archivo.close()


# Leer las presiones desde el archivo
presiones_sistolica = []
presiones_diastolica = []
try:
    # Abrimos el archivo en modo de lectura para obtener los elementos
    archivo = open(nombre_archivo, 'r')

    for linea in archivo:
        # Eliminamos espacios en blanco al principio y al final con strip()
        linea_limpia = linea.strip()
        # Dividimos la línea en partes por el separador '/'
        partes = linea_limpia.split('/')
        # Convertimos la primera parte a entero y la añadimos a la lista de presiones sistólicas
        presiones_sistolica.append(int(partes[0]))
        # Convertimos la segunda parte a entero y la añadimos a la lista de presiones diastólicas
        presiones_diastolica.append(int(partes[1]))

except IOError:
    print("Se produjo un error al leer el archivo.")
finally:
    archivo.close()


# Hacer gráfica de presiones
if presiones_sistolica and presiones_diastolica:
    plt.figure(figsize=(10, 5))
    plt.plot(presiones_sistolica, 'r-o', label='Sistólica')
    plt.plot(presiones_diastolica, 'b-o', label='Diastólica')
    plt.title('Registro de Presión Arterial')
    plt.xlabel('Número de Medición')
    plt.ylabel('Presión Arterial (mmHg)')
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("No hay datos para mostrar.")


'''
Programa: Escritura y lectura básica de fichero
El programa escribe tres líneas en un fichero en disco y luego las lee 
y muestra en pantalla. 
Incluye control de excepciones.
'''
# Nombre del archivo a utilizar
nombre_archivo = 'mi_archivo.txt'

# Intentamos abrir el archivo y escribir en él
try:
    # Abrimos el archivo en modo de escritura ('w' para escritura)
    archivo = open(nombre_archivo, 'w')
    # Escribimos tres líneas en el archivo
    archivo.write('Primera línea\n')
    archivo.write('Segunda línea\n')
    archivo.write('Tercera línea\n')
except IOError:
    print("Se produjo un error al escribir en el archivo.")
finally:
    # Asegurarse de cerrar el archivo
    archivo.close()

# Intentamos abrir el archivo y leer de él
try:
    # Abrimos el archivo en modo de lectura ('r' para lectura)
    archivo = open(nombre_archivo, 'r')
    # Leemos las líneas del archivo
    lineas = archivo.readlines()
except IOError:
    # Manejo de la excepción si ocurre algún error al leer el archivo
    print("Se produjo un error al leer el archivo")
finally:
    # Asegurarse de cerrar el archivo
    archivo.close()

# Imprimir las líneas leídas del archivo
print("Contenido del archivo:")
for linea in lineas:
    print(linea, end='')  # La función print añade por defecto un salto de línea, por eso usamos end='' para evitar líneas extra.

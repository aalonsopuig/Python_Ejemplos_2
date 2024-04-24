# Programa de Lista de Compras con almacenamiento aditivo en Archivo 
# Este programa permite al usuario añadir artículos a una lista de la compra de manera interactiva.
# Los artículos son almacenados en un archivo de texto. Una vez que el usuario termina de añadir artículos,
# el programa lee el archivo y muestra todos los artículos almacenados.
# En caso de que el archivo ya tenga artículos, los añadirá

import os  # Se importa el módulo os para verificar la existencia del archivo

# Nombre del archivo donde se almacenará la lista de la compra
nombre_archivo = 'lista_de_compras.txt'

# Verificar si el archivo ya existe
if os.path.exists(nombre_archivo):
    modo_apertura = 'a' 
else:
    modo_apertura = 'w' 

# Solicitamos al usuario que introduzca elementos en la lista de la compra
try:
    # Abrimos el archivo en el modo adecuado para almacenar los elementos
    archivo = open(nombre_archivo, modo_apertura, encoding='utf-8')
    
    while True:
        elemento = input("Introduce un artículo a la lista de la compra o '0' para terminar: ")
        if elemento == '0':
            break
        archivo.write(elemento + '\n')
        print(f"'{elemento}' ha sido agregado a la lista.")
except IOError:
    print("Se produjo un error al escribir en el archivo.")
finally:
    archivo.close()

# Leemos la lista de la compra desde el archivo y la mostramos
try:
    # Abrimos el archivo en modo de lectura para obtener los elementos
    archivo = open(nombre_archivo, 'r', encoding='utf-8')
    print("\nLista de la compra:")
    for elemento in archivo:
        print(elemento.strip())  # strip() elimina el salto de línea al final de cada elemento
except IOError:
    print("Se produjo un error al leer el archivo.")
finally:
    archivo.close()

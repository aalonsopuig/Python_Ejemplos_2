# Programa de almacenamiento en Archivo
# Este programa permite al usuario añadir artículos a un archivo de manera interactiva.
# Los artículos son almacenados en un archivo de texto. Una vez que el usuario termina de añadir artículos,
# el programa lee el archivo y muestra todos los artículos almacenados.

# Nombre del archivo 
nombre_archivo =input("Nombre fichero: ")

# Solicitamos al usuario que introduzca elementos 
try:
    # Abrimos el archivo en modo de append para almacenar los elementos.
    # Si el archivo no existe, lo crea. Si existe, añade los datos al final de este.
    archivo = open(nombre_archivo, 'a', encoding='utf-8')
    
    while True:
        elemento = input("Introduce un elemento a añadir o '0' para terminar: ")
        if elemento == '0':
            break
        archivo.write(elemento + '\n')
        print(f"'{elemento}' ha sido agregado.")
except IOError:
    print("Se produjo un error al escribir en el archivo.")
finally:
    archivo.close()

# Leemos la lista de la compra desde el archivo y la mostramos
try:
    # Abrimos el archivo en modo de lectura para obtener los elementos
    archivo = open(nombre_archivo, 'r', encoding='utf-8')
    print("\nElementos:")
    for elemento in archivo:
        print(elemento.strip())  # strip() elimina el salto de línea al final de cada elemento
except IOError:
    print("Se produjo un error al leer el archivo.")
finally:
    archivo.close()

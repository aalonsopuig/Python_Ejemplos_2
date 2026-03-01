# Programa de Biblioteca de Libros
# Este programa permite al usuario añadir títulos de libros a un archivo de manera interactiva.
# Los títulos son almacenados en un archivo de texto. Una vez que el usuario termina de añadir títulos,
# el programa lee el archivo y muestra todos los títulos almacenados.

# Nombre del archivo
nombre_archivo = input("Nombre del fichero para almacenar los libros: ")

# Solicitamos al usuario que introduzca títulos de libros
try:
    # Abrimos el archivo en modo de append para almacenar los títulos.
    # Si el archivo no existe, lo crea. Si existe, añade los datos al final de este.
    archivo = open(nombre_archivo, 'a', encoding='utf-8')
    
    while True:
        titulo = input("Introduce el título de un libro a añadir o '0' para terminar: ")
        if titulo == '0':
            break
        archivo.write(titulo + '\n')
        print(f"'{titulo}' ha sido agregado a la biblioteca.")
except IOError:
    print("Se produjo un error al escribir en el archivo.")
finally:
    archivo.close()

# Leemos los títulos de los libros desde el archivo y los mostramos
try:
    # Abrimos el archivo en modo de lectura para obtener los títulos
    archivo = open(nombre_archivo, 'r', encoding='utf-8')
    print("\nTítulos en la biblioteca:")
    for titulo in archivo:
        print(titulo.strip())  # strip() elimina el salto de línea al final de cada título
except IOError:
    print("Se produjo un error al leer el archivo.")
finally:
    archivo.close()

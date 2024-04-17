'''
Programa: Escritura básica de fichero
El programa escribe tres líneas en un fichero en disco
'''
ruta_archivo = 'Documentos/mi_archivo.txt'
# Abrir el archivo en modo de escritura ('w' crea un nuevo archivo o sobrescribe si ya existe)
archivo = open(ruta_archivo, 'w')

# Escribir tres líneas en el archivo
archivo.write('Primera línea\n')
archivo.write('Segunda línea\n')
archivo.write('Tercera línea\n')

# Cerrar el archivo manualmente
archivo.close()

print('Tres líneas han sido escritas en el archivo "mi_archivo.txt".')
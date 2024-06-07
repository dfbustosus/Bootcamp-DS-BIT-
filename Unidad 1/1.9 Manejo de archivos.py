# Parte 1: Apertura y Cierre de Archivos

# Para manejar archivos en Python, usamos la función open().
# Podemos especificar diferentes modos al abrir un archivo.

# Abrir un archivo en modo de solo lectura (por defecto)
archivo = open("archivo.txt", "r")
print("Archivo abierto en modo de solo lectura")
archivo.close()

# Es importante cerrar el archivo después de terminar la operación para liberar recursos.
print("Archivo cerrado")

# Parte 2: Lectura de Archivos

# Lectura completa del archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)

# Leer el archivo línea por línea
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(f"Línea: {linea.strip()}")

# Leer líneas como una lista
with open("archivo.txt", "r") as archivo:
    lineas = archivo.readlines()
    print(f"Líneas como lista: {lineas}")

# Parte 3: Escritura en Archivos

# Escribir en un archivo (modo "w" sobrescribe el contenido existente)
with open("archivo_escritura.txt", "w") as archivo:
    archivo.write("Primera línea\n")
    archivo.write("Segunda línea\n")
print("Contenido escrito en archivo_escritura.txt")

# Añadir contenido a un archivo existente (modo "a" de append)
with open("archivo_escritura.txt", "a") as archivo:
    archivo.write("Tercera línea\n")
print("Contenido añadido a archivo_escritura.txt")

# Parte 4: Modos de Archivo

# Modos comunes:
# "r" - Lectura (por defecto)
# "w" - Escritura (sobrescribe el archivo)
# "a" - Añadir (escribe al final del archivo)
# "b" - Modo binario
# "t" - Modo texto (por defecto)

# Leer y escribir en modo binario
with open("archivo_binario.bin", "wb") as archivo:
    archivo.write(b'\x00\x01\x02\x03')
print("Datos binarios escritos en archivo_binario.bin")

with open("archivo_binario.bin", "rb") as archivo:
    datos_binarios = archivo.read()
    print(f"Datos binarios leídos: {datos_binarios}")

# Parte 5: Gestión de Errores

# Manejar excepciones al trabajar con archivos
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("Error: El archivo no existe")

# Consejos avanzados:
# 1. Usar with para asegurar que el archivo se cierre automáticamente.
with open("archivo_consejo.txt", "w") as archivo:
    archivo.write("Usar with para manejar archivos es una buena práctica")

# 2. Leer archivos grandes en bloques para evitar problemas de memoria.
with open("archivo_grande.txt", "r") as archivo:
    while True:
        bloque = archivo.read(1024)  # Leer en bloques de 1KB
        if not bloque:
            break
        print(bloque)

# 3. Uso de las librerías pandas o csv para manejar archivos CSV de manera eficiente.
import csv

with open("archivo.csv", newline='') as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        print(f"Fila CSV: {fila}")

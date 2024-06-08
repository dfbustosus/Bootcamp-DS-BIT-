# Parte 1: Sentencias condicionales (if, elif, else)

# Las sentencias condicionales permiten ejecutar código basado en ciertas condiciones.
x = 10
if x > 5:
    print("x es mayor que 5")
else:
    print("XXXXX")

# Puedes tener múltiples condiciones usando elif.
y = 15
if y > 20:
    print("y es mayor que 20")
elif y > 10:
    print("y es mayor que 10 pero menor o igual a 20")
else:
    print("y es 10 o menor")

# Ejemplo con operadores lógicos
z = 25
if (z > 10) and (z < 30):
    print("z está entre 10 y 30")

# Parte 2: Bucles (for y while)

# Los bucles se usan para repetir un bloque de código varias veces.

# Bucle for
print("Bucle for:")
for i in range(5):
    print(f"Iteración {i}")

# Bucle while
print("Bucle while:")
n = 0
while n < 5:
    print(f"Iteración {n}")
    n += 1
else:
    print('Saliendo')

# Parte 3: Control de bucles (break, continue, pass)

# La instrucción break termina el bucle actual.
print("Uso de break:")
for i in range(10):
    if i == 5:
        break
    print(i)

# La instrucción continue salta a la siguiente iteración del bucle.
print("Uso de continue:")
for i in range(10):
    if i == 5:
        continue
    print(i)

# La instrucción pass no hace nada y se usa como un placeholder.
print("Uso de pass:")
for i in range(5):
    if i == 3:
        pass
    print(i)

# Parte 4: Comprehensions

# Las comprehensions son una forma concisa de crear listas, conjuntos y diccionarios.

# List comprehension
lista_v=[]
for i in range(10):
    lista_v.append(i**2)

cuadrados = [x**2 for x in range(10)]
print(f"List comprehension de cuadrados: {cuadrados}")

# Set comprehension
pares = {x for x in range(10) if x % 2 == 0}
print(f"Set comprehension de pares: {pares}")

# Dictionary comprehension
cuadrados_dict = {x: x**2 for x in range(10)}
print(f"Dictionary comprehension de cuadrados: {cuadrados_dict}")

# Parte 5: Funciones y control de flujo

# Las funciones permiten encapsular código reutilizable.
def es_par(numero):
    return numero % 2 == 0

print(f"10 es par: {es_par(10)}")
print(f"7 es par: {es_par(7)}")

# Funciones con condicionales
def clasificar_edad(edad):
    if edad < 18:
        return "Menor de edad"
    elif edad < 65:
        return "Adulto"
    else:
        return "Adulto mayor"

print(f"Clasificación de edad (15): {clasificar_edad(15)}")
print(f"Clasificación de edad (30): {clasificar_edad(30)}")
print(f"Clasificación de edad (70): {clasificar_edad(70)}")


# Parte 6: Control de excepciones

# Las excepciones permiten manejar errores en tiempo de ejecución.
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")

# Captura de múltiples excepciones
try:
    numero = int("texto")
except ValueError:
    print("Error: No se puede convertir texto a entero")
except Exception as e:
    print(f"Error inesperado: {e}")

# Consejos avanzados:
# 1. Uso de else con bucles
for i in range(5):
    print(i)
else:
    print("Bucle completado sin interrupciones")

# 2. Uso de else con excepciones
try:
    numero = int("10")
except ValueError:
    print("Error: No se puede convertir texto a entero")
else:
    print("Conversión exitosa")

# 3. Uso de finally para limpieza
try:
    archivo = open("archivo.txt", "r")
except FileNotFoundError:
    print("Error: El archivo no existe")
else:
    print("Archivo abierto con éxito")
finally:
    print("Esto se ejecuta sin importar lo que pase")
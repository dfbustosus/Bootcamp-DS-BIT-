# En Python, los números y las cadenas de caracteres (strings) son dos de los tipos de datos más utilizados.
# Empezaremos con los números y luego pasaremos a las cadenas.

# Parte 1: Números en Python

# Python soporta varios tipos de números: enteros, flotantes y complejos.
# Los enteros son números sin parte decimal.
entero = 10
print(f"Entero: {entero}")

# Los números flotantes (float) tienen una parte decimal.
flotante = 10.5
print(f"Flotante: {flotante}")

# Los números complejos tienen una parte real y una imaginaria.
complejo = 2 + 3j
print(f"Complejo: {complejo}")

# Operaciones aritméticas básicas
suma = 5 + 3
resta = 10 - 2
multiplicacion = 4 * 3
division = 20 / 5
division_entera = 20 // 6
modulo = 20 % 6
potencia = 2 ** 3

print(f"Suma: 5 + 3 = {suma}")
print(f"Resta: 10 - 2 = {resta}")
print(f"Multiplicación: 4 * 3 = {multiplicacion}")
print(f"División: 20 / 5 = {division}")
print(f"División entera: 20 // 6 = {division_entera}")
print(f"Módulo: 20 % 6 = {modulo}")
print(f"Potencia: 2 ** 3 = {potencia}")

# Parte 2: Strings en Python

# Los strings son secuencias de caracteres encerrados entre comillas simples o dobles.
cadena_simple = 'Hola, Mundo!'
cadena_doble = "Hola, Mundo!"

print(f"Cadena con comillas simples: {cadena_simple}")
print(f"Cadena con comillas dobles: {cadena_doble}")

# Puedes usar comillas triples para strings multilínea.
cadena_multilinea = """Esta es una cadena
multilínea en Python."""
print(f"Cadena multilínea: {cadena_multilinea}")

# Concatenación de strings
nombre = "Juan"
saludo = "Hola, " + nombre + "!"
print(f"Concatenación: {saludo}")

# Interpolación de strings (f-strings)
edad = 30
mensaje = f"{nombre} tiene {edad} años."
print(f"Interpolación (f-string): {mensaje}")

# Métodos comunes de strings
longitud = len(mensaje)
mayusculas = mensaje.upper()
minusculas = mensaje.lower()
reemplazo = mensaje.replace("Juan", "Pedro")

print(f"Longitud del mensaje: {longitud}")
print(f"Mensaje en mayúsculas: {mayusculas}")
print(f"Mensaje en minúsculas: {minusculas}")
print(f"Reemplazo de 'Juan' por 'Pedro': {reemplazo}")

# Indexación y segmentación (slicing) de strings
primer_caracter = mensaje[0]
ultimo_caracter = mensaje[-1]
subcadena = mensaje[5:10]

print(f"Primer carácter: {primer_caracter}")
print(f"Último carácter: {ultimo_caracter}")
print(f"Subcadena [5:10]: {subcadena}")

# Conversión entre números y strings
numero_str = str(entero)
string_a_numero = int("123")

print(f"Conversión de número a string: {numero_str}")
print(f"Conversión de string a número: {string_a_numero}")

# Consejos avanzados:
# 1. Utiliza try-except para manejar errores de conversión.
try:
    numero_invalido = int("abc")
except ValueError:
    print("Error: No se puede convertir 'abc' a un número.")

# 2. Formatea números con coma como separador de miles.
numero_grande = 1000000
print(f"Número grande formateado: {numero_grande:,}")

# 3. Usa f-strings para formatear números con decimales.
pi = 3.14159
print(f"Pi con dos decimales: {pi:.2f}")

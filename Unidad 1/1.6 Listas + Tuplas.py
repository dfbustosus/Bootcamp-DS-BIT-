# Parte 1: Listas en Python

# Las listas son colecciones ordenadas y mutables que permiten almacenar múltiples elementos.
# Puedes crear una lista utilizando corchetes [].
mi_lista = [1, 2, 3, 4, 5]
print(f"Lista inicial: {mi_lista}")

# Las listas pueden contener elementos de diferentes tipos.
lista_mixta = [1, "dos", 3.0, [4, 5]]
print(f"Lista mixta: {lista_mixta}")

# Acceso a elementos
primer_elemento = mi_lista[0]
ultimo_elemento = mi_lista[-1]
print(f"Primer elemento: {primer_elemento}")
print(f"Último elemento: {ultimo_elemento}")

# Modificación de elementos
mi_lista[0] = 10
print(f"Lista después de modificar el primer elemento: {mi_lista}")

# Métodos comunes de listas
mi_lista.append(6)
print(f"Lista después de añadir 6: {mi_lista}")

mi_lista.insert(1, 15)
print(f"Lista después de insertar 15 en la posición 1: {mi_lista}")

mi_lista.remove(3)
print(f"Lista después de eliminar el primer 3: {mi_lista}")

pop_elemento = mi_lista.pop()
print(f"Elemento eliminado con pop: {pop_elemento}")
print(f"Lista después de pop: {mi_lista}")

# Longitud de la lista
longitud_lista = len(mi_lista)
print(f"Longitud de la lista: {longitud_lista}")

# Slicing (segmentación) de listas
sublista = mi_lista[1:4]
print(f"Sublista [1:4]: {sublista}")

# List comprehension
cuadrados = [x**2 for x in mi_lista]
print(f"Cuadrados de los elementos en la lista: {cuadrados}")

# Parte 2: Tuplas en Python

# Las tuplas son colecciones ordenadas e inmutables que permiten almacenar múltiples elementos.
# Puedes crear una tupla utilizando paréntesis ().
mi_tupla = (1, 2, 3, 4, 5)
print(f"Tupla inicial: {mi_tupla}")

# Las tuplas también pueden contener elementos de diferentes tipos.
tupla_mixta = (1, "dos", 3.0, [4, 5])
print(f"Tupla mixta: {tupla_mixta}")

# Acceso a elementos
primer_elemento_tupla = mi_tupla[0]
ultimo_elemento_tupla = mi_tupla[-1]
print(f"Primer elemento de la tupla: {primer_elemento_tupla}")
print(f"Último elemento de la tupla: {ultimo_elemento_tupla}")

# Las tuplas son inmutables, por lo que no se pueden modificar sus elementos directamente.
# Sin embargo, puedes concatenar tuplas para crear una nueva.
nueva_tupla = mi_tupla + (6, 7)
print(f"Tupla después de concatenar: {nueva_tupla}")

# Longitud de la tupla
longitud_tupla = len(mi_tupla)
print(f"Longitud de la tupla: {longitud_tupla}")

# Slicing (segmentación) de tuplas
subtupla = mi_tupla[1:4]
print(f"Subtupla [1:4]: {subtupla}")

# Conversión entre listas y tuplas
lista_a_tupla = tuple(mi_lista)
tupla_a_lista = list(mi_tupla)

print(f"Conversión de lista a tupla: {lista_a_tupla}")
print(f"Conversión de tupla a lista: {tupla_a_lista}")

# Consejos avanzados:
# 1. Usar tuplas para datos constantes y listas para datos que cambian frecuentemente.
coordenadas = (10.0, 20.0)  # Ejemplo de uso de tupla para coordenadas
print(f"Coordenadas (tupla): {coordenadas}")

# 2. Desempaquetar tuplas y listas en variables individuales.
x, y, z = (1, 2, 3)
print(f"Desempaquetar tupla: x={x}, y={y}, z={z}")

a, b, c = [4, 5, 6]
print(f"Desempaquetar lista: a={a}, b={b}, c={c}")

# 3. Usar * para desempaquetar listas y tuplas en funciones.
def suma(a, b, c):
    return a + b + c

parametros = (1, 2, 3)
resultado = suma(*parametros)
print(f"Suma de parámetros desempaquetados: {resultado}")
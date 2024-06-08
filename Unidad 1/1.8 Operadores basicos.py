# Parte 1: Operadores Aritméticos

# Los operadores aritméticos se usan para realizar operaciones matemáticas comunes.
a = 10
b = 3

# Suma
suma = a + b
print(f"Suma: {a} + {b} = {suma}")

# Resta
resta = a - b
print(f"Resta: {a} - {b} = {resta}")

# Multiplicación
multiplicacion = a * b
print(f"Multiplicación: {a} * {b} = {multiplicacion}")

# División
division = a / b
print(f"División: {a} / {b} = {division}")

# División entera
division_entera = a // b
print(f"División entera: {a} // {b} = {division_entera}")

# Módulo
modulo = a % b
print(f"Módulo: {a} % {b} = {modulo}")

# Potencia
potencia = a ** b
print(f"Potencia: {a} ** {b} = {potencia}")

# Parte 2: Operadores de Comparación

# Los operadores de comparación se usan para comparar dos valores.
x = 5
y = 8

# Igual a
igual = x == y
print(f"{x} == {y} : {igual}")

# Diferente de
diferente = x != y
print(f"{x} != {y} : {diferente}")

# Mayor que
mayor_que = x > y
print(f"{x} > {y} : {mayor_que}")

# Menor que
menor_que = x < y
print(f"{x} < {y} : {menor_que}")

# Mayor o igual que
mayor_o_igual = x >= y
print(f"{x} >= {y} : {mayor_o_igual}")

# Menor o igual que
menor_o_igual = x <= y
print(f"{x} <= {y} : {menor_o_igual}")

# Parte 3: Operadores Lógicos

# Los operadores lógicos se usan para combinar declaraciones condicionales.
verdadero = True
falso = False

# AND lógico
and_logico = verdadero and falso
print(f"{verdadero} AND {falso} : {and_logico}")

# OR lógico
or_logico = verdadero or falso
print(f"{verdadero} OR {falso} : {or_logico}")

# NOT lógico
not_logico = not verdadero
print(f"NOT {verdadero} : {not_logico}")


# Parte 4: Operadores de Asignación

# Los operadores de asignación se usan para asignar valores a las variables.
c = 10

# Asignación simple
c = 5
print(f"Asignación simple: c = {c}")

# Asignación con suma
c += 2  # Equivalente a c = c + 2
print(f"Asignación con suma: c += 2 -> {c}")

# Asignación con resta
c -= 1  # Equivalente a c = c - 1
print(f"Asignación con resta: c -= 1 -> {c}")

# Asignación con multiplicación
c *= 3  # Equivalente a c = c * 3
print(f"Asignación con multiplicación: c *= 3 -> {c}")

# Asignación con división
c /= 2  # Equivalente a c = c / 2
print(f"Asignación con división: c /= 2 -> {c}")

# Asignación con módulo
c %= 4  # Equivalente a c = c % 4
print(f"Asignación con módulo: c %= 4 -> {c}")

# Asignación con potencia
c **= 2  # Equivalente a c = c ** 2
print(f"Asignación con potencia: c **= 2 -> {c}")

# Parte 5: Operadores de Pertenencia

# Los operadores de pertenencia se usan para verificar si un valor o variable se encuentra en una secuencia.
lista = [1, 2, 3, 4, 5]

# in
pertenece = 3 in lista
print(f"3 in {lista} : {pertenece}")

# not in
no_pertenece = 6 not in lista
print(f"6 not in {lista} : {no_pertenece}")

# Consejos avanzados:
# 1. Uso de operadores en comprehensiones de listas.
cuadrados = [x**2 for x in range(10) if x % 2 == 0]
print(f"Cuadrados de números pares usando comprehensiones: {cuadrados}")

# 2. Combinación de operadores lógicos con operadores de comparación.
edad = 25
es_adulto = edad >= 18 and edad < 65
print(f"Es adulto (18 <= edad < 65): {es_adulto}")

# 3. Uso de operadores de asignación con operadores de comparación para contar elementos.
conteo = 0
valores = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
for valor in valores:
    conteo += (valor == 3)
print(f"Conteo de valores iguales a 3 en la lista: {conteo}")
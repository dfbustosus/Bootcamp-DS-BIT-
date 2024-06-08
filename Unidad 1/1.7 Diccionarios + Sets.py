# Parte 1: Diccionarios en Python

# Los diccionarios son colecciones desordenadas de pares clave-valor.
# Puedes crear un diccionario utilizando llaves {}.
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(f"Diccionario inicial: {mi_diccionario}")

# Acceso a valores
nombre = mi_diccionario["nombre"]
print(f"Nombre: {nombre}")

# Añadir o modificar elementos
mi_diccionario["edad"] = 31  # Modificar
mi_diccionario["profesión"] = "Ingeniero"  # Añadir
print(f"Diccionario después de modificar/añadir: {mi_diccionario}")

# Métodos comunes de diccionarios
# Obtener todas las claves
claves = mi_diccionario.keys()
print(f"Claves: {list(claves)}")

# Obtener todos los valores
valores = mi_diccionario.values()
print(f"Valores: {list(valores)}")

# Obtener todos los pares clave-valor
items = mi_diccionario.items()
print(f"Pares clave-valor: {list(items)}")

# Eliminar un elemento
mi_diccionario.pop("ciudad")
print(f"Diccionario después de eliminar 'ciudad': {mi_diccionario}")

# Usar get() para evitar errores si la clave no existe
profesion = mi_diccionario.get("profesión", "No especificado")
a= mi_diccionario.get("AAA","XXXX")
print(f"Profesión: {profesion}")
print(a)

# Parte 2: Sets en Python

# Los sets son colecciones desordenadas de elementos únicos.
# Puedes crear un set utilizando llaves {} o la función set().
mi_set = {1, 2, 3, 4, 5, 5, 5 }
print(f"Set inicial: {mi_set}")

# Los sets eliminan automáticamente los duplicados
set_con_duplicados = {1, 2, 2, 3, 4, 4, 5}
print(f"Set sin duplicados: {set_con_duplicados}")

# Añadir y eliminar elementos
mi_set.add(6)
print(f"Set después de añadir 6: {mi_set}")

mi_set.remove(3)
print(f"Set después de eliminar 3: {mi_set}")

# Operaciones de conjuntos
otro_set = {4, 5, 6, 7, 8}
mi_set = {1, 2, 3, 4, 5, 5, 5 }
# Unión
union = mi_set | otro_set
print(f"Unión de sets: {union}")
# Intersección
interseccion = mi_set & otro_set
print(f"Intersección de sets: {interseccion}")
# Diferencia
diferencia = mi_set - otro_set
print(f"Diferencia de sets: {diferencia}")
# Diferencia simétrica
diferencia_simetrica = mi_set ^ otro_set
print(f"Diferencia simétrica de sets: {diferencia_simetrica}")


# Consejos avanzados:
# 1. Usar sets para eliminar duplicados de una lista.
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
set_sin_duplicados = set(lista_con_duplicados)
print(f"Lista sin duplicados usando set: {list(set_sin_duplicados)}")

# 2. Iterar eficientemente sobre un diccionario.
for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")

# 3. Comprehensiones de diccionarios y sets.
# Crear un diccionario a partir de una lista de tuplas
lista_tuplas = [("nombre", "Ana"), ("edad", 25)]
diccionario_comp = {clave: valor for clave, valor in lista_tuplas}
print(f"Diccionario con comprehensión: {diccionario_comp}")

# Crear un set de cuadrados
set_cuadrados = {x**2 for x in range(10)}
print(f"Set de cuadrados usando comprehensión: {set_cuadrados}")
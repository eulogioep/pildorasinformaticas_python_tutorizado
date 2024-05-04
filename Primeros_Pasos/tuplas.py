# Las tuplas son parecidas a las listas pero con ligeras diferencias.

# Son inmutables, es decir, no se pueden modificar después de su creación.
# Se pueden extraer porciones de la tupla pero el resultado es una tupla nueva.
# No permite búsquedas con index.
# Sí se puede comprobar si un elemento está dentro de la tupla.

# Ventajas frente a las listas:
# Son más rápidas, ocupan menos memoria, formatean Strings y se pueden utilizar
# como claves en un diccionario.

# Se crea: nombre_tupla = (elem1, elem2, elem3, .....)

mi_tupla = ("Pedro", 34, True, "Mario")

# Convertir tupla a lista

mi_tupla_en_lista = list(mi_tupla)

# Comprobar si un elemento se encuentra en una tupla

print("Mario" in mi_tupla) # Devuelve True

# Contabiliza cuántas veces se encuentra un elemento en una tupla

print(mi_tupla.count("Pedro")) # Devuelve 1

# Obtener la longitud de una tupla

print(len(mi_tupla)) # Devuelve 4

# Desempaquetar una tupla
# Es importante asignar cada variable al dato que queremos dar y
# tenemos que dar la cantidad exacta de variables que tenga la tupla.

nombre, edad, casado, nombre_hijo = mi_tupla

print(nombre, edad, casado, nombre_hijo)

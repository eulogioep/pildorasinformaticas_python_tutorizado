# Crea una lista
trabajadores = ["Juan", 6, "Ana", "Pedro", "María", True]
trabajadores2 = ["Pilar", "Amancio"]

# Imprime en consola los elementos de una lista
print(trabajadores)

# Imprime en consola el primer elemento de una lista
print(trabajadores[0]) # Accede por el principio de la lista
print(trabajadores[-1]) # Accede por el final de la lista

# Primer valos es el índice donde empieza a contar. El segundo valor dónde para y siempre
# empezando desde el primer valor.
print(trabajadores[2:4]) # ["Ana", "Pedro"]

# Unir dos listas
print(trabajadores + trabajadores2)

# Agrega un elemento al final de una lista.
# Uso común: Cuando deseas agregar un solo elemento a una lista existente.
trabajadores.append("Luis")
print(trabajadores)

# Agrega varios elementos al final de una lista.
# Uso común: Cuando deseas agregar múltiples elementos desde otra lista o secuencia.
trabajadores.extend([3,5])
print(trabajadores)

# Elimina la primera aparición de un elemento con el valor especificado en una lista.
# Modifica la lista original al eliminar el elemento. Si el elemento aparece más de una vez 
# en la lista, solo se eliminará la primera aparición.
trabajadores.remove("Pedro")

# Eliminar un elemento según el índice dado
del trabajadores[3] # Eliminamos a Pedro

# Imprimir el índice de un elemento
print(trabajadores.index("Ana"))


# Indica el tamaño de una lista
print(len(trabajadores))
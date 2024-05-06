# Los diccionarios son estructuras de datos que nos permite almacenar valores
# de diferente tipo (int,string,bool, etc incl. listas y diccionarios).

# Los datos se almacenan asociados a una clave única. (clave : valor).

# Cómo se crea un diccionario:
capitales = {'España' : 'Madrid',
             'Francia' : 'París',
             'Portugal' : 'Lisboa',
             'Italia' : 'Roma',
             'Reino Unido' : 'Londres'
            }

#print(capitales)

# Agregar nuevos valores o modificar existentes:
capitales['Alemania'] = 'Berlín'

print(capitales)

# Eliminar valores:
del capitales['Reino Unido']

print(capitales)

########### Ejemplo con diferentes tipos de datos ############ 

datos = {'España' : 'Madrid', 
         23 : 'Jordan', 
         'Mosqueteros' : 3
        }

### Trabajar con tuplas en los diccionarios ###

clave_capitales = ('España', 'Reino Unido', 'Colombia', 'Portugal')

capitales_mundo = {clave_capitales[0] : 'Madrid',
                   clave_capitales[1] : 'Londres',
                   clave_capitales[2] : 'Bogotá',
                   clave_capitales[3] : 'Lisboa'
                   }

print(type(capitales_mundo))

# Acceso a valores de un diccionario:
print(capitales_mundo['España'])

# Conocer las claves de un diccionario (keys):
print(capitales_mundo.keys())

# Conocer los valores de un diccionario (values):
print(capitales_mundo.values())

# Conocer la cantidad de elementos que tiene un diccionario (len):
print(len(capitales_mundo))

# Diccionarios anidados:

datos_Jordan = {23 : "Jordan",
                'Nombre' : 'Michael',
                'Equipo' : 'Chicago Bulls',
                'anillos' : {'temporadas' : [1991, 1992, 1993, 1996, 1997, 1998]}
                }


print(datos_Jordan)
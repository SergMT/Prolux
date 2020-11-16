#Crear array con elementos predefinidos
famosos = ['Scarlet', 'Gal Gadot']
#Se accede al segundo nombre
print(famosos[1])

#Obtener el tamaño del array usando len()
tamanoFamosos = len(famosos)
print(tamanoFamosos)

#Array vacío
valoresX = []
#Agregar datos al final del array
valoresX.append(70)
valoresX.append(80)
print(valoresX)

"""
    METODOS DE ARRAYS EN PYTHON!!

    Method	    Description
    append()	Agrega un elemento al final de la lista
    clear()	    Quita todos los elementos de la lista
    copy()	    Retorna una copia de la lista
    count()	    Retorna el numero de elementos con el valor especificado
    extend()	Agrega los elementos de una lista (o cualquier iteracion) 
                al final de la lista actual
    index()	    Retorna el índice del primer elemento con el valor específicado
    insert()	Agrega un elemento en la posición especificada
    pop()	    Elimina el último elemento de la lista o el que se especifique
    remove()	Elimina el primer elemento que encuentre con el valor especificado,
                en caso de no especificar ninguno, dará error.
    reverse()	Invierte el orden de la lista
    sort()  	Reordena la lista. Si son strings las ordena de alfabéticamente.
                Si son números los ordena de menor a mayor.
                Si es una combinacion de cadenas y números, pondrá primero los números.
"""
#Rangos en arrays
famosos = ['Scarlet Johanson', 'Gal Gadot', 'Henry Cavill', 'Crhistian Bale']
#Se eligen rangos con la siguiente sintaxis:
print(famosos[1:3])
#Resultado:
['Gal Gadot', 'Henry Cavill']
""" Cuando se especifica un rango, los índices se vuelven los corchetes y las comas
en este caso los índices serían: 0, 1, 2, 3 y 4, siendo 1 2 y 3 los de Gal Gadot y Henry
"""

#Crear diccionarios. Nótese que es con llaves
contactos = {"nombre" : "Eduardo"}
#Añadir un elemento al diccionario
contactos["apellido"] = "Nolasco"
print(contactos)
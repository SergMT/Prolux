"""CICLO FOR """
arreglo = ["Hola", "Mundo"]
#Ejemplo de ciclo for para los arreglos
for lista in arreglo:
#En este caso la variable lista sirve de contador o índice (AUMENTA DE 1 EN 1)
    print(lista)

"""Especificar un rango con el método range() 
el primer parámetro es el número inicial del contador
el segundo es la cantidad de números que va a contar
en este caso solo contaría 0 y 1  
"""
for indice in range(0,2):
    print(arreglo[indice])

"""Si solo se coloca un parámetro el valor inicial del contador es 0
este codigo hace lo mismo que el anterior:"""
for indice in range(2):
    print(arreglo[indice])

"""Se puede agregar un tercer parámetro que indique el valor del incremento
en este caso aumentara de 3 en 3"""
for x in range(2, 30, 3):
  print(x)

#Se puede iterar cada una de las letras de un string
for x in "banana":
  print(x)

#Ejemplo con break para detener el ciclo
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Ejemplo for anidado
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


"""CICLO WHILE
Ejemplo de ciclo while para un arreglo"""
i = 0
#El método len() obtiene la longitud del arreglo
while i < len(arreglo):
    print(arreglo[i])
    i += 1

#Detener un ciclo usando un if y break
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

#Usando continue se detiene la iteración actual y se continua a la siguiente
i = 0
while i < 6:
  i += 1
  #En este caso no se imprimiŕa el número 3
  if i == 3:
    continue
  print(i)

#Con un else se ejecuta un bloque de código cuando el ciclo termina
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

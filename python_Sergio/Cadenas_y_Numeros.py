print("Hola mundo!!")
print() #Salto de línea
print("Mi primer programa \n en python") #String con salto de linea

#Pedir datos al usuarios
name = input("Escribe tu nombre: ")
lastName = input("Escribe tus apellidos: ")
#Capitalizar primer letra de strings en python: .capitalize()
# print("Hola, " + name.capitalize() + " " + lastName.capitalize())

#Formatear strings
output = f"Hola, {name.capitalize()} {lastName.capitalize()}"
print(output)

""" Mayúsculas: .upper()  
    Minúsculas: .lower()
    Contar caracteres: .count()
"""

"""NUMEROS !!!
    Exponente: **
    (lo demás ya lo saben)
"""

number1 = input("Escribe el primer número ")
number2 = input("Escribe el segundo número ")
#Se debe convertir los numeros a int o float cuando los escribe el usuario
result = float(number1) + float(number2)
print(result)

#Para concatenar números con strings se debe convertir el numero a string
number3 = 28
daysFebruary= str(number3) + " days has February"
print(daysFebruary)

#RANDOM
import random
#Numero aleatorio del 1 al 9
print(random.randrange(1, 10))

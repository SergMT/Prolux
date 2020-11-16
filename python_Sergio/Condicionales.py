precio = input("Ingresa el valor ")

precio = float(precio)
#Condicional if en python:
if precio >= 100.00:
    tarifa = 0.7
else:
    tarifa = 0.3
print("Tarifa: " + str(tarifa))
"""Cualquier linea que no sea tabulada dentro de la condicional, se 
tomará como excluida de la condicional.

COMPARAR CADENAS: """
paisNatal = input("De dónde eres? ")

"""Python ve diferentes las mayusculas y minúsculas, por lo tanto se debe
optar por formatear el string del usuario usando upper(), lower() o capitalize()"""
if paisNatal.lower() == "mexico":
    print("Te deben encantar los tacos!!")
else:
    print("Pues deberías visitarlo")

#Else if:
if paisNatal.lower() == "mexico":
    print("Te deben encantar los tacos!!")
elif paisNatal.lower() == "colombia":
    print("genial!")
else:
    print("cool")

#Como usar OR en los ifs
if paisNatal.lower() == "mexico":
    print("Te deben encantar los tacos!!")
#La manera mśa rápida y limpia es usando la palabra clave IN
elif paisNatal.lower() in("colombia", "honduras"):
    print("genial!")
else:
    print("cool")

#Cómo usar AND en los ifs
if paisNatal.lower() == "mexico":
    print("Te deben encantar los tacos!!")
#Colocar la palabra clave AND 
elif paisNatal.lower() == "colombia" and paisNatal.lower() == "honduras":
    print("genial!")
else:
    print("cool")

#Cómo usar booleanos
if paisNatal.lower() == "mexico":
    paisNatal = True
else:
    paisNatal = False
"""Siempre se debe usar mayúscula en la primer letra de los valores booleanos
Para verificar si una variable es falsa o verdadera se escribe como se muestra:  """
if paisNatal:
    print(paisNatal)

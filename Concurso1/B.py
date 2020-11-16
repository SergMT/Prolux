estaciones = []
cantidadPersonas = int(input(" "))
estacion = int(input(" "))

estaciones.append(estacion)

i = 0
while i < cantidadPersonas-1:
    estacion = input(" ")
    estacion = int(estacion)
    estaciones.append(estacion)
    i += 1

comparador = estaciones
numero = 0
#Puerta trasera
for z in estaciones:
    for x in comparador:
        if z < x:
            estaciones.pop(0)        
        elif z > x:
           pass
        

#Dos puertas
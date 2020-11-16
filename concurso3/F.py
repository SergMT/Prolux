partida = input('')
puntos = []
for i in range(len(partida)):
  if partida[i]=='Q':
    # aqui se hace la operación para sumar los puntos y se vacia el arreglo para nueva operación lo cual no se como hacer JAJAJAJAJA
    print(puntos)
    puntos = []
  else:
    puntos.append(partida[i])

squares = []
squares += [1, 12, 23, 24, 45, 56]
squares += ['s', 'a', 'b', 'c']
print (squares[-3])
print (squares[2])
print (squares[:3])
print (squares[-3:])
print ()

cubes = [1, 8, 27]
cubes.append(64) # append agrega elementos al array
print (cubes)
print (len(cubes))

# borrar un rango 
squares[2:2] = []

# baciar toda la lista
squares[:] = []

# Crear matrices
matriz = [[1,2,3,4],['a','b','c','d']]
# indice      0              1
# indice   0 1 2 3    0   1   2   3
print (matriz[1][2])
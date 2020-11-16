capacidad = int(input(''))
alumnos = int(input(''))
rango = alumnos
cupo = 0
viajes = 0
if capacidad >= alumnos + 1:
    print(1)
elif capacidad < alumnos + 1:
    for i in range(rango):
        if capacidad > cupo + 1 and cupo < alumnos:#c=10 cupo
            cupo += 1
        elif cupo + 1 == capacidad:
            cupo += 1
            # alumnos += 1
            alumnos -= cupo
            viajes += 1
            cupo = 0
            rango += alumnos
            print(viajes)
        elif cupo < capacidad and cupo > 0:
            viajes += 1
            print('v:', viajes)

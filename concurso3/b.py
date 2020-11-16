matriz = [
  #1,2,3,4,5,6,7,8,9,10
  [0,0,0,0,0,0,0,0,0,0], #1
  [0,0,0,0,0,0,0,0,0,0], #2
  [0,0,0,0,0,0,0,0,0,0], #3
  [0,0,0,0,0,0,0,0,0,0], #4
  [0,0,0,0,0,0,0,0,0,0], #5
  [0,0,0,0,0,0,0,0,0,0], #6
  [0,0,0,0,0,0,0,0,0,0], #7
  [0,0,0,0,0,0,0,0,0,0], #8
  [0,0,0,0,0,0,0,0,0,0], #9
  [0,0,0,0,0,0,0,0,0,0], #10
]
res='Y'
numB = input('')
salida = []
barco = []
for index in range(int(numB)):
  barco = input('').split() #0 5 1 1
  x = int(barco[2])-1
  y = int(barco[3])-1
  try:
    if int(barco[0])==0:
      for lengB in range(int(barco[1])):
        if matriz[x][y]==0:
          matriz[x][y] = 1
          salida.append('Y')
        else:
          salida.append('N')
        y += 1
    elif int(barco[0])==1:
      for lengB in range(int(barco[1])):
        if matriz[x][y]==0:
          matriz[x][y] = 1
          salida.append('Y')
        else:
          salida.append('N')
        x += 1
  except IndexError:
    res='N'
if res=='N':
  print(res)
else:
  for i in range(len(salida)):
    if salida[i]== 'N':
      res='N'
  print(res)
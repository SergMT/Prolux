cantidad = input('').split() #2 2

matriz=[]
for i in range(int(cantidad[0])):
  # a = input('').split()
  matriz.append(input('').split())


for i in range(len(matriz)):
  sum=0
  for j in range(int(cantidad[1])):
    sum += int(matriz[i][j])
  print(sum)

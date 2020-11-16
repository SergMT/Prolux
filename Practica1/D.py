cantidad = input('')

matriz=[]
for i in range(int(cantidad)):
  # a = input('').split()
  matriz.append(input('').split())

count=0
sum=0
for i in range(int(cantidad)):
  sum+=int(matriz[i][count])
  count += 1
  
print(sum)

for i in range(int(cantidad)):
  print(' '.join(matriz[i]))
a = input('').split()
numeros = []
for i in range(int(a[1])):
  numeros.append(input('').split())
evaluar = 0
for i in range(len(numeros)):
  
  if numeros[i][0]==evaluar:
    result='N'
  else:
    result='Y'
  evaluar = numeros[i][0]
print(result)
cantidad = int(input(''))
calif=[]
for i in range(cantidad):
  # a = input('').split()
  calif.append(input('').split())

prom = []

for i in range(len(calif)):
  y=int(calif[i][0])
  prom.append(y)
  asteriscos=''
  for y in range(y):
    asteriscos+='*'
  print(asteriscos)

suma=0
for i in range(len(prom)):
  suma += prom[i]

div = suma/len(prom)
expresion=''
if div>=6:
  expresion=":)"
if div<6:
  div = 0
  expresion=":("
print(int(div))
print(expresion)

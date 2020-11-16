cantidad = int(input(''))
if cantidad >= 1 and cantidad <=100:
  matriz = []
  res=0
  for i in range(cantidad):
    ronda=int(input(''))
    res+=ronda
    matriz.append(res)
  max_item = max(matriz, key=int)
  if max_item>0:
    resultado = 100+max_item
  else:
    resultado = 100
  print(resultado)
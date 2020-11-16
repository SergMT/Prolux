a, b= 0, 1
while a<10:
  print (f'Valor de a es: {a}')
  a, b = b, a+b; # Serie de Fibonacci
  # a += 1

# Evitar salto de linea al imprimir
a, b = 0, 1
while a < 1000:
  print(a, end=', ')
  a, b = b, a+b

# For trabaja más como un for each refiriendose a java
words = ['cat', 'window', 'defenestrate']
for w in words:
  print (w, len(w))

# Para hacer un siclo consecutivo se puede utilizar la función range
for i in range(5):
  print(i)

#Para iterar o recorrer una lista en secuencia se puede usar len y range
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
  print(1, a[1]) #Sin embargo con esta funcion se puede usar enumerate() el cual debuelve la lista pero con numeros

# Más sobre la función range
range(5, 10) #Rango del 6 al 10
# Resultado:   5, 6, 7, 8, 9

range(0, 10, 3) #Rango del 0 al 10 de 3 en 3
# Resultado   0, 3, 6, 9

range(-10, -100, -30) #Rando del -10 al -100 de -30 en -30
# Resultado  -10, -40, -70

print(range(10)) #No es una lista y no es iterable
# Resultado   range(0, 10)

sum(range(4))  # 0 + 1 + 2 + 3
# Resultado   6

list(range(4)) # Asigna a la lista todos los valores del rango
# Resultado   [0, 1, 2, 3]

# Break
for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, 'equals', x, '*', n//x)
      break
  else: ##Los siclos úeden tener un else, este se ejecuta al terminar la condicion pero nunca al ejecutar un break
    # loop fell through without finding a factor
    print(n, 'is a prime number')

# Continue
for num in range(2, 10):
  if num % 2 == 0:
    print("Found an even number", num)
    continue
  print("Found an odd number", num)

# El programa se puede poner en modo de espera, y solo dejarlo sin hacer nada, para salir es necesario presionar ctrl + c
pass #No hace nada, solo deja el programa en espera
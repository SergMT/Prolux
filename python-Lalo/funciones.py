# def funcname(parameter_list):
#   """
#   docstring
#   """
#   Conenido de la funcion

# Podemos crear una función que escriba la serie de Fibonacci en un límite arbitrario
def fib(n):    # write Fibonacci series up to n
  """Print a Fibonacci series up to n."""
  a, b = 0, 1
  while a < n:
    print(a, end=' ')
    a, b = b, a+b
  print()
# Now call the function we just defined:
fib(2000)

f = fib
f(100) #  Se puede crear un objeto de una funcion

print(fib(0)) # Si la función no retorna ningun valor, el valor de retorno será None

# Para hacer que una lista debuelva un valor se usa return
def fib2(n):  # return Fibonacci series up to n
  """Return a list containing the Fibonacci series up to n."""
  result = []
  a, b = 0, 1
  while a < n:
    result.append(a)    # see below
    a, b = b, a+b
  return result
f100 = fib2(100)        # call it
print (f100)            # write the result
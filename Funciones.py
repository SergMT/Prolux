from datetime import datetime

"""Para crear funciones se usa la palabra def nombreFuncion():
Ejemplo:"""
def tiempoActual():
    #No existe la palabra return en python
    print(datetime.now())
#Al llamar la función imprime la fecha y hora actual
tiempoActual()

#PARAMETROS EN FUNCIONES
def my_function(firstName):
  print(firstName + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
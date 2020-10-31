name = input('Cuál es tu nombre? ')
last_name  = input('Cuál es tu apellido? ')  # con input se optienen textos de usuario
print ('')
print ('Hola')
print (name)
x = 3
print ('')
# Comentarios con #

print (name+last_name)
print ('Hello, ' + name.capitalize() + ' ' + last_name.capitalize())

#otras formas de concatenar
output0 = 'Hello, {} {}'.format(name, last_name)
output1 = 'Hello, {0} {1}'.format(name, last_name) #el indice {0} o {1} hace referencia a la posicion de la variable en .format
output2 = f'Hello, {name} {last_name}' # Solo para python 3+
print (output0)
print (output1)
print (output2)
print (f'Esto es la salida 1 {output0}, la 2 {output1} y la 3 {output2}')
print ('')

# Funciones para mofigicar Strings
sentence = 'The dog is named Sammy'
print (sentence.upper())       # Coloca todo en mayusculas 
print (sentence.lower())       # Coloca todo el texto en minusculas
print (sentence.capitalize())  # Coloca la primer letra en mayusculas
print (sentence.count('m'))    # cuenta cuantas m existen en el texto

tocapitalize = input('Coloca un texto').capitalize() # se puede aplicar el capitalize desde el input
print(tocapitalize)

length = '12345'
# con len() es posible obtener la longitud de una cadena de texto
print (len(length))

texto = 'Hola como estás'
# como obtener fragmentos de un texto
print (texto[1]) # obtiene la letra en la posicion 2 empezando a contar desde 0
print (texto[3])
print (texto[len(texto)-1]) #obtiene la ultima letra
print (texto[-1]) #Otra forma de obtener la ultima letra
print (texto[2:5]) # obtiene el rango de 2 a 5
print (texto[:3]) # obtiene el rango de 0 a 3
print (texto[-4:]) # obtiene las ultimas 4 letras
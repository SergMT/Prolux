# ###  Operadores y simbolos  ####
#  |----------|-----------------|
#  |  Symbol  |    Operation    |
#  |----------|-----------------|
#  |    +     | Suma            |
#  |    -     | Resta           |
#  |    *     | Multiplicación  |
#  |    /     | Division        |
#  |    **    | Exponente       |
#  |----------|-----------------|
#
# ### Parsear ###
# str()   | a String
# int()   | a Integer
# float() | a Float

first_number  = 6
second_number = 2
print (first_number + second_number)
print (first_number ** second_number)

print ('Hello '+str(first_number)) #si no se coloca el str para parsear la variable el programa colapsa


integerNumbre = '4'
floatNumber   = '5.2'

print (int(integerNumbre))
print (float(floatNumber))
N = int(input(''))
passw = []
if N>=0 and N<=pow(10, 5):
  for i in range(N):
    s = input('')
    passw.append(s)
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
seguridad = 0
seguridadArr = []
for i in range(len(passw)):
  if len(passw[i])>10:
    seguridad = seguridad + 1
  if passw[i].count('.')>0 or passw[i].count('#')>0 or passw[i].count('$')>0 or passw[i].count('%')>0 or passw[i].count('/')>0 or passw[i].count('(')>0 or passw[i].count(')')>0 or passw[i].count('&')>0:
    seguridad = seguridad + 1
  contadorMin = 0
  for j in range(len(abecedario)):
    if passw[i].count(abecedario[j])>0:
      contadorMin = contadorMin+1
  if contadorMin>0:
    seguridad = seguridad + 1
  contadorMin = 0
  for j in range(len(abecedario)):
    if passw[i].count(abecedario[j].capitalize())>0:
      contadorMin = contadorMin+1
  if contadorMin>0:
    seguridad = seguridad + 1

  tempArr = []
  tempstring=passw[i]
  for k in range(len(passw[i])):
    tempArr.append(tempstring[k])
    #if tempstring[k].isnumeric():
  verif = True
  comparacon=tempArr[0]
  for w in range(len(tempArr)+1):
    y=w+1
    if tempArr[y].isnumeric():
      compare2=(int(tempArr[y]))-1
      if compare2==comparacon or verif==False:
        verif=False
      comparacon=tempArr[y]
  if verif==True:
    seguridad = seguridad + 1
  seguridadArr.append(seguridad)
  seguridad = 0
for i in range(len(seguridadArr)):
  if seguridadArr[i]<3:
    print('Assertion number #'+ str(i+1) +': Rejected')
  if seguridadArr[i]==3:
    print('Assertion number #'+ str(i+1) +': Weak')
  if seguridadArr[i]==4:
    print('Assertion number #'+ str(i+1) +': Good')
  if seguridadArr[i]==5:
    print('Assertion number #'+ str(i+1) +': Strong')

    """Los métodos isdigit(), isnumeric() e isdecimal() determinan si todos los caracteres de la cadena son dígitos, números o números decimales.

>>> "1234".isnumeric()
True
>>> "1234".isdecimal()
True
>>> "abc123".isdigit()
False """
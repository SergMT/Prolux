cantidad = int(input(''))
datosArreglo =[]
suma=[]
for datos in range(cantidad):
    datosArreglo.append(input('').split())

for datos in range(cantidad):
    p = float(datosArreglo[datos][0])
    d = float(datosArreglo[datos][1])
    suma.append((.25*d)*(p/100))
res=0
for datos in range(len(suma)):
    res += suma[datos]
print("{0:.2f}".format(res))

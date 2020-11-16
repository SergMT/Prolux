#Se importa la librería datetime, timedelta para hacer operaciones con fechas
from datetime import datetime, timedelta

#Se obtiene la fecha actual con datetime.now()
fechaActual = datetime.now()
#Para concatenar con strings, se convierte la fecha en string
print("La fecha actual es: " + str(fechaActual))

"""Uso de timedelta, para quitar días o semanas a una fecha específica
Para los días se usa days = Numero_De_Dias
Para las semanas es weeks = Numero_De_Semanas"""

unDia = timedelta(days=1)

#Se resta el valor de la variable unDia a la fecha actual
fechaActual = datetime.now() - unDia
print("Fecha de ayer: " + str(fechaActual))

"""OBTENER DATOS ESPECIFICOS
    print("Dia: " + str(fechaActual.day))
    print("Mes: " + str(fechaActual.month))
    print("Año: " + str(fechaActual.year))

    print("Hora: " + str(fechaActual.hour))
    print("Minutos: " + str(fechaActual.minute))
    print("Segundos: " + str(fechaActual.second))
"""

#Pedir fecha de nacimiento al usuario
fechaUsuario = input("Ingresa la fecha de tu cumpleaños dd/mm/yyyy ")
#Se verifica que la fecha se haya recibido en el formato indicado con strptime()
fechaNacimiento = datetime.strptime(fechaUsuario, "%d/%m/%Y")
fechaNacimiento = fechaNacimiento - unDia 
#Se convierte en cadena la fecha de cumpleaños para imprimirlo
print("El día antes de tu cumpleaños es: " + str(fechaNacimiento))
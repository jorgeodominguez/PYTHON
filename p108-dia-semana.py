#Diseña un programa con una función que pida un número entero entre 1 y 7 y devuelva el día de la semana con letra.

def dia(n):
    d=""
    if n==1:
        d="Lunes"
    elif n==2:
        d="Martes"
    elif n==3:
        d="Miercoles"
    elif n==4:
        d="Jueves"
    elif n==5:
        d="Viernes"
    elif n==6:
        d="Sabado"
    elif n==7:
        d="Dominguez"
    else:
        d="Error"
    return d

#Programa principal
n=int(input("Dame el dia de la semana (1-7): "))
print(f"El dia de la semana es {dia(n)}")
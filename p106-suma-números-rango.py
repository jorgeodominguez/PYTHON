# suma numeros en un rango

def sumarango(ini,fin):
    s=0
    for i in range(ini,fin+1):
        s=s+i
    return s


i,f=int(input("Inicio: ")),int(input("Final: "))
suma=sumarango(i,f)

print(f"La suma del Rango es {suma}")
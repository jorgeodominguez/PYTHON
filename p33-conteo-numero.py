#Cuenta numeros, los suma, cuaenta positivos, negativos y ceros, se detiene al introducir 999

cuenta=suma=cp=cn=cc=0

while(True):
    num=int(input("Numero: "))
    if num!=999:
        cuenta=cuenta+1
        suma=suma+num
        if num > 0:
            cp=cp+1
        elif num<0:
            cn=cn+1
        else:
            cc=cc+1
    else:
        break

print(f"Se introdujeron {cuenta} numeros")
print(f"La suma de los numeros es: {suma}")
print("Los positivos son: ",cp)
print("Los negativos son: ",cn)
print("Los ceros son: ",cc)
#Imprime la tabla de multiplicar t desde 1 hasta n

import os

while(True):

    os.system("cls")
    t=int(input("Tabla: "))
    n=int(input("Hasta donde: "))

    c=1
    while c<=n:
        print(f"{t} x {c} = {t*c}")
        c=c+1
    
    res=input("\nDeseas continuar (S/N): ").upper()
    if res=='N':
        break

print("\nProceso terminado... ")
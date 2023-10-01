#Se desea imprimir la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma:

import os

os.system("cls")

n=int(input("Cuantos terminos: "))
suma=0

for i in range(1,n+1):
    if i>1 and i<=n:
        print(f" + 1/{i}!",end="")
    else:
        print(i,end="")
    suma=suma+(1/i)
print(f"\nLa suma es: {suma}")

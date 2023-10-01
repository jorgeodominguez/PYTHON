#Se desea imprimir los pares de 2 a n y su suma

import os

os.system("cls")

n=int(input("Dame un numero: "))
suma=0

for n in range(2,n+1,2):
    suma=n+suma
    print(n, end=" ")

print(f"\nLa suma es: {suma}")
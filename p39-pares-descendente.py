#Se desea imprimir los números pares desde 100 hasta el número que el usuario decida (n), además deberá
#imprimirse la suma de esos números pares. El proceso debe poder repetirse hasta que el usuario lo decida.

import os

while(True):
    os.system("cls")
    print("Imprime los numeros descendentemente comenzando de 100")
    n=int(input("Hasta donde deseas llegar: "))
    c=100
    suma=0
    while c>=n:
     print(c, end=" ")
     suma=suma+c
     c=c-2
    print(f"\nLa suma de los numeros es: {suma}")
    res=input("Deseas continuar (S/N): ").upper()
    if res=='N':
        break
print("\n Proceso terminado ...")
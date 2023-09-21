#Se desea imprimir los números impares de forma ascendente desde 1 hasta el número que el usuario decida (n),
#además deberá imprimirse la suma de esos números impares. El proceso debe poder repetirse hasta que el
#usuario lo decida.
import os

while(True):
    os.system("cls")
    print("Imprime numeros impares ascendentemente hasta donde lo indique")
    n=int(input("Hasta donde deseas llegar: "))
    c=1
    suma=0
    while c<=n:
     print(c, end=" ")
     suma=suma+c
     c=c+2
    print(f"\nLa suma de los numeros es: {suma}")
    res=input("Deseas continuar (S/N): ").upper()
    if res=='N':
        break
print("\n Proceso terminado ...")
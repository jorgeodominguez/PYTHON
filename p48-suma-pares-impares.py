#Imprime los pares y su suma, los impares y su suma, en en rango de 1 a n
import os

while(True):
    os.system("cls")

    n=int(input("Hasta donde deseas pares e impares: "))

    s=0
    print("\n Imprimir numeros pares y su suma")
    for par in range(2,n+1,2):
        print(par, end=" ")
        s=s+par
    print("\nLa suma de los pares es: ",s)

    s=0
    print("\nImprimir los numeros impares y su suma")
    for impar in range(1,n+1,2):
        print(impar,end=" ")
        s=s+impar
    print("\nLa suma de los numeros pares es: ",s)

    res=input("\nDeseas Continuar (S/N)").upper()
    if res=='N':
        break
    
print("\nProceso terminado ....")
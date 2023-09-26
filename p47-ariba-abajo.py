#imprimir los numeros de 1 a n o de 1 a 1, segun el usuario lo decida

import os

while(True):
    os.system('cls')
    print("[ 1 ] Imprimir los numeros de 1 a n")
    print("[ 2 ] Imprimir los numeros de n a 1")
    op=int(input("Elige: "))

    if op==1:
        print(f"Imprimiendo de 1 hasta n\n")
        n=int(input("Dame el valor de n: "))
        for z in range(1,n+1):
            print(z, end=' ')
    elif op==2:
        print("\nImprimiendo desde n hasta 1\n")
        n=int(input("Dame el valor de n: "))
        for w in range(n,0,-1):
            print(w, end=' ')
    else:
        print("\nOpcion invalida")
    res=input("\nDeseas Continuar (S/N)").upper()
    if res=='N':
        break
print("\nProceso terminado ....")

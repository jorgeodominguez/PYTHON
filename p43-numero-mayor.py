#Calcular el número mayor de una serie de números introducidos por el teclado, el proceso se detiene al introducir
#0. El proceso debe poder repetirse hasta que el usuario lo decida.

import os
may=0

while(True):
    os.system("cls")
    print("Numero mayor de una serie de numeros, para parar '0'")
    while(True):
        num=int(input("Numero: "))
        if num!=0:
            if num>may:
                may=num
        else:
            break
        
    print(f"El numero mayor es {may}")
    res=input("\nDeseas continuar (S/N): ").upper()
    if res=='N':
        break
print("\n Proceso terminado ...")
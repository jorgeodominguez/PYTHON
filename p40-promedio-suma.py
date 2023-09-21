#Se desea calcular la suma y el promedio de una serie de números introducidos por el teclado hasta introducir 0,
#además deberá contar cuantos números se introdujeron. El proceso debe poder repetirse hasta que el usuario lo decida.

import os 

while(True):
    os.system("cls")
    print("Introduce numeros, calcula todo cuando introduces 0")
    cuenta=suma=prom=0
    while(True):
        num=int(input("Numero: "))
        if num!=0:
            cuenta=cuenta+1
            suma=suma+num
            prom=suma/cuenta
        else:
            break
    print(f"\nSe introdujeron {cuenta} numeros")
    print(f"La suma de los numeros es: {suma}")
    print(f"El promedio de los numero es: {prom}")
    res=input("\nDeseas continuar (S/N): ").upper()
    if res=='N':
        break
print("\n Proceso terminado ...")
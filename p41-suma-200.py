#Se desea calcular la suma de números introducidos por el usuario hasta que la suma sea >= 200, luego mostrar
#cuantos números fueron introducidos y la suma de estos. El proceso debe poder repetirse hasta que el usuario lo decida.


import os

while(True):
    os.system("cls")
    print("Introduce numeros y se detiene si suma mas de 200")
    cuenta=suma=0
    while(True):
        num=int(input("Numero: "))
        suma=suma+num
        cuenta=cuenta+1
        if suma>=200:
            break
        else:
            print(f"la suma es: {suma}")
    print(f"\nSe introdujeron {cuenta} numeros")
    print(f"La suma de los numeros es: {suma}")
    res=input("\nDeseas continuar (S/N): ").upper()
    if res=='N':
        break
print("\n Proceso terminado ...")
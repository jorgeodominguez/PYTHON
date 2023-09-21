#Se desea calcular la temperatura convertida de grados centígrados a grados farenheit de un rango de valores
#introducidos por el usuario, es decir el usuario introduce la temperatura inicial y la temperatura final en grados
#centígrados y el programa realiza la conversión a farenheit incrementando el valor inicial en 1, hasta llegar al valor
#final. El proceso debe poder repetirse hasta que el usuario lo decida.

import os

#tc=17.13;tcl=21.22

while(True):
    os.system("cls")
    while(True):
        ini=float(input("Valor iniciar: "))
        fin=float(input("Valor final: "))
        if(ini<fin):
            break

    cen=ini
    print("Centigrados\tFarenheit")
    print("-"*25)
    while(cen<=fin):
        far= (cen * 9/5) + 32
        print(f"    {cen}  \t  {far:.2f}")
        cen=cen+1
    print("-"*25)
    res=input("Deseas Continuar (S/N): ").upper()
    if res=='N': break

print("\n Proceso terminado ...")
#Imprime una tabla de conversión de peso a dolar
import os

tc=17.13;tcl=21.22

while(True):
    os.system("cls")
    while(True):
        pi=float(input("Valor iniciar: "))
        pf=float(input("Valor final: "))
        if(pi<pf):
            break

    c=pi
    print("Pesos\tdolar\tLibra")
    print("-"*25)
    while(c<=pf):
        print(f"{c}\t{c/tc:.4f}\t{c/tcl:.4f}")
        c=c+1
    print("-"*25)
    res=input("Deseas Continuar (S/N): ").upper()
    if res=='N': break

print("\n Proceso terminado ...")
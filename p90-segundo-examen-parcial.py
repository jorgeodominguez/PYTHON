#Se desea procesar el pedido de una pizza en base a sus ingredientes, cada ingrediente tiene un precio, de acuerdo con lo siguiente
import os
os.system('cls')

ingredientes={
    'T':1.5,
    'P':3.50,
    'A':0.40,
    'Q':3.74,
    'I':2.10
}

lista=['T','P','A','Q','I']

pizza=input("Ingredientes de tu pizza: ").upper()
lis_pizza=list(pizza)

suma=15
if len(lis_pizza)>0:
    for l in lis_pizza:
        if l in lista:
            if l=="T":
                suma=suma+1.50
            elif l=="P":
                suma=suma+3.50
            elif l=="A":
                suma=suma+0.40
            elif l=="Q":
                suma=suma+3.74
            elif l=="I":
                suma=suma+2.10
        else:
            print("No seleccionaste ingredientes validos")
            suma=15
            break
    if suma==15:
       print("")
    else:        
        print(f"El subtotal es: {suma:.2f}")
        if suma>=30:
            sub=suma-(suma*.05)
            print(f"El total es: {sub:.2f}")
        else:
            print(f"El total es: {suma:.2f}")  
else:
    print(f"Precio base es de 15, compra de más de 20 descuento del 5%")
    for k,v in ingredientes.items():
        print(f'{k:<1} - {v}')


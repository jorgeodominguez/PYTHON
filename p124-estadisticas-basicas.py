import numpy as np

def leer():
    lista=[]
    while True:
        n=int(input("numero: "))
        if n==-1:
            break
        lista.append(n)
    return lista

def menor(lista):
    m=lista[0]
    for n in lista:
        if n<m:
            m=n
    return m

def mayor(lista):
    m=lista[0]
    for n in lista:
        if n>m:
            m=n
    return m

def media(lista):
    s=0
    for n in lista:
        s+=n
    return s/len(lista)

def varianza(lista):
    var=np.var(lista)
    return var

def desviacion(lista):
    des=np.std(lista)
    return des

num=leer()

print(f"\nLa lista de números original es: {num}")
print(f"La media es: {media(num)}")
print(f"El mayor de los numeros: {mayor(num)}")
print(f"El menor de los numeros: {menor(num)}")
print(f"La Varianza es: {varianza(num)}")
print(f"La Desviacion estandar es: {desviacion(num)} \n")
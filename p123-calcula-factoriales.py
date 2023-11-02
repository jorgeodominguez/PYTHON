def leer():
    lista=[]
    while True:
        n=int(input("numero: "))
        if n==-1:
            break
        lista.append(n)
    return lista

def factorial(lista):
    facto=[]
    for n in lista:
        f=1
        for n in range(1,n+1):
            f=f*n
        facto.append(f)
    return facto

num=leer()
fac=factorial(num)
print(f"\nLa lista de números original es: {num}")
print(f"\nLa lista con los factoriales es: {fac}")
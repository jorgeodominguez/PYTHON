def leer():
    lista=[]
    while True:
        n=int(input("numero: "))
        if n==-1:
            break
        lista.append(n)
    return lista

def sumadigitos(lista):
    digitos=[]
    for n in lista:
        suma=0
        while n!=0:
            dig=n%10
            suma=suma+dig
            n=n//10
        digitos.append(suma)
    return digitos    

num=leer()
sum=sumadigitos(num)
print(f"\nLa lista de números original es: {num}")
print(f"\nLa lista con la suma de digitos de los números es: {sum}")

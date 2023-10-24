#Determina al mayor de 3 numeros

def mayor(n1,n2,n3):
    may=0
    if n1>n2 and n1>n3:
        may=n1
    elif n2>n1 and n2>n3:
        may=n2
    else:
        may=n3
    return may

#Programa principal
print("Dame 3 numeros: ")
a,b,c=float(input()),float(input()),float(input())
print(" El mayor de los 3 numero es: ",mayor(a,b,c))

#print(mayor(300,40,100))
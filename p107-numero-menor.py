#Diseña un programa con una función que pida 3 números enteros y devuelva el menor de ellos, usando una función

def menor(n1,n2,n3):
    men=0
    if n1<n2 and n1<n3:
        men=n1
    elif n2<n1 and n2<n3:
        men=n2
    else:
        men=n3
    return men

print("Dame 3 numeros: ")
a,b,c=float(input()),float(input()),float(input())
print(" El menor de los 3 numero es: ",menor(a,b,c))
#Funcion que recive 2 numeros y me regresa la suma

def suma(n1,n2,n3):
    s=n1+n2+n3
    return s

#Programa principal
sum=suma(100,200,50)
print("La suma es ",sum)

print("La suma es ",suma(900,100,500))

print("Dame dos numeros: ")
n1,n2,n3=int(input()),int(input()),int(input())
sum=suma(n1,n2,n3)
print("La suma es ",sum)
#suma los digitos de un numero entero 1971=18

def sumadigitos(n):
    suma=0
    while n!=0:
        dig=n%10
        suma=suma+dig
        n=n//10
    return suma

#Programa principal
año=int(input("Dame tu año de nacimiento y te dire tu numero de la suerte: "))
suerte=sumadigitos(año)
print(f"Tu año de nacimiento es {año} por lo tnato tu numero de la suerte es {suerte}")
#Diseña un programa con una función que reciba tres parámetros: dos números (un rango), una letra P o I y nos regrese la suma de números pares o impares en el rango de números especificados.

def sum_num(ini,fin,l):
    s=0
    if l=="P":
        for par in range(ini,fin+1,1):
            if par%2==0:
                print(par, end=" ")
                s=s+par
        return s
    if l=="I":
        for impar in range(ini,fin+1,1):
            if impar%2!=0:
                print(impar, end=" ")
                s=s+impar
        return s

print("Sumar una serie de numeros: ")
print("[ P ] ar")
print("[ I ] mpares")

op=input("Elije: ").upper()

if op=="P":
    ini=int(input("Dame en inicio: "))
    fin=int(input("Dame el final: "))
    print(f"La suma de los numeros pares es: {sum_num(ini,fin,'P')}")
elif op=="I":
    ini=int(input("Dame en inicio: "))
    fin=int(input("Dame el final: "))
    print(f"La suma de los numero impares es: {sum_num(ini,fin,'I')}")
else:
    print("Opcion incorrecta")
#Imprime la suma y el promedio de n numeros introducidos por el usuario

n=int(input("Cauntos numeros deseas procesar: "))
suma=promedio=0

for c in range(1,n+1):
    num=int(input(f"Numero {c}: "))
    suma=suma+num
    promedio=suma/n

print("\nLa suma es: ",suma)
print("\nEl promedio es: ",promedio)


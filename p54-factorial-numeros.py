#Imprime el factorial de n numeros

n=int(input("de cuantos numeros deseas el factorial: "))

for i in range(1,n+1):
    print(f"{i}! -> ",end="")
    f=1
    for j in range(1,i+1):
        print(f"{j}x ",end="")
        f=f*j
    print(f" = {f}")
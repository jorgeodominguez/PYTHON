#imprime la tabla de multimpicar que el usuario pida hasta donde la pida

def tabla(t,n):
    print(f"Tabla del {t} hasta el {n}")
    for i in range(1,n+1):
        print(f"{t} x {i} = {t*i}")
    print()

#Programa principal
t=int(input("Que tabla quieres: "))
n=int(input("Hasta donde: "))
tabla(t,n)

tabla(5,4)
tabla(4,5)
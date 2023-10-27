#Diseña un programa con dos funciones que convierta: pulgadas a centímetros y metros a pies. Deberá́ mostrar un menú con las opciones correspondientes.

def centimetros(pulgadas):
    return(pulgadas*2.54)

def pies(metros):
    return(metros*3.281)

#Programa principal
print("[ P ] ulgadas")
print("[ M ] etros")

op=input("Elije: ").upper()


if op=="P":
    pulgadas=int(input("Dame las pulgadas: "))
    print(f"Las pulgadas a centimetros son {centimetros(pulgadas)}")
elif op=="M":
    metros=int(input("Dame los metros: "))
    print(f"Los metros a pies son {pies(metros)}")
else:
    print("Opcion incorrecta")
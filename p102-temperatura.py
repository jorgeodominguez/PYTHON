#Convierte de grados centigraos a fareheit y vceversa

def faranheit(temp):
    return(temp*(9/5))+32

def centigrados(temp):
    return(temp-32)*(5/9)

#Programa principal
print("[ F ] arenhei")
print("[ C ] entrigrados")

op=input("Elije: ").upper()


if op=="F":
    temp=int(input("Dame centigrado: "))
    print(f"los Farenheit son {faranheit(temp)}")
elif op=="C":
    temp=int(input("Dame farenheit: "))
    print(f"los centigrados son {centigrados(temp)}")
else:
    print("Opcion incorrecta")

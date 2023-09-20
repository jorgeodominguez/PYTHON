#Dados tres números enteros, verificar si son consecutivos (9,10,11) y mandar mensaje confirmándolo, si no lo son(1,4,6) mandar mensaje de error.

num1=int(input("\nDame el 1er numero: "))
num2=int(input("\nDame el 2do numero: "))
num3=int(input("\nDame el 3er numero: "))

if num1<num2 and num2<num3:
    print(f"los numero son consecutivos {num1} {num2} {num3}")
else:
    print(f"Error los numero NO son consecutivos {num1} {num2} {num3}")
    
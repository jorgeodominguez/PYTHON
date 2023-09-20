#Dados tres números enteros, verificar cual es el mayor.

num1=int(input("\nDame el 1er numero: "))
num2=int(input("\nDame el 2do numero: "))
num3=int(input("\nDame el 3er numero: "))

if num1>=num2 and num1>=num3:
    print(f"El numero {num1} es el mayor")
elif num2>num3:
    print(f"El numero {num2} es el mayor")
else:
    print(f"El numero {num3} es el mayor")
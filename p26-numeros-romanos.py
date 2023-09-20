#Realizar un programa que pida un número entre 1 y 10 y muestre su equivalente en número romano ( I, II, III, IV, V,VI, VII, VIII, IX, X). Si el número no esta en el rango solicitado que mande un mensaje de error.

num=int(input("Dame un numero del 1 al 10: "))

if num>=1 and num<=10:
    if num==1:
        print(f"\nEl numero {num} esta dentro del rango")
        print(f"I")
    elif num==2:
        print(f"\nEl numero {num} esta dentro del rango")
        print(f"II")
    elif num==3:
        print(f"\nEl numero {num} esta dentro del rango")
        print(f"III")
    elif num==4:
        print(f"\nEl numero {num} esta dentro del rango")
        print(f"IV")
    elif num==5:
        print(f"\nEl numero {num} esta dentro del rango")
        print(f"V")
    elif num==6:
        print(f"\nEl numero {num} esta dentro del rango")
        print(f"VI")
    elif num==7:
        print(f"\nEl numero {num} esta dentro del rango")
        print(f"VII")
    elif num==8:
        print(f"\nEl numero {num} esta dentro del rango")
        print(f"VII")
    elif num==9:
        print(f"\nEl numero {num} esta dentro del rango")
        print(f"IX")
    elif num==10:
        print(f"\nEl numero {num} esta dentro del rango")
        print(f"X")
else:
    print(f"\nEl numero {num} no esta dentro del rango solicitado")
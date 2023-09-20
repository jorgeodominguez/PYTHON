#Dado un numero entero entre 1 y 7, se desea mostrar con letra el día de la semana correspondiente, 1 es domingo, 2 es lunes y así hasta 7 es viernes. Si el número no está en el rango especificado, mostrar un mensaje de error.

num=int(input("Dame un numero del 1 al 7: "))

if num>=1 and num<=7:
    if num==1:
        print(f"\nEl numero {num} esta dentro del rango")
        print(f"El dia de la semana es DOMINGO")
    elif num==2:
        print(f"\nEl numero {num} esta dentro del rango")
        print(f"El dia de la semana es LUNES")
    elif num==3:
        print(f"\nEl numero {num} esta dentro del rango")
        print(f"El dia de la semana es MARTES")
    elif num==4:
        print(f"\nEl numero {num} esta dentro del rango")
        print(f"El dia de la semana es MIERCOLES")
    elif num==5:
        print(f"\nEl numero {num} esta dentro del rango")
        print(f"El dia de la semana es JUEVES")
    elif num==6:
        print(f"\nEl numero {num} esta dentro del rango")
        print(f"El dia de la semana es VIERNES")
    elif num==7:
        print(f"\nEl numero {num} esta dentro del rango")
        print(f"El dia de la semana es SABADO")
else:
    print(f"\nEl numero {num} no esta dentro del rango solicitado")
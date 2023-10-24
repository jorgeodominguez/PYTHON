#funcion con varios parametros

def saluda(nombre,edad,telefono,correo):
    print("*"*109)
    print(f"Bienvenido {nombre} tu edad es {edad}, tu telefono es {telefono}, tu correo es {correo}", end="")
    if(edad>=18):
        print(" Eres mayor de edad")
    else:
        print(" Eres menor de edad")
    print("*"*109)


saluda("Jorge Dominguez",30,4921096157,"jorge@gmail.com")
saluda("Carlos Antonio",14,"4921042567","charly@msn.com")
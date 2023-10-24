#funcion que al ser invocada usa el nombre del parametro

def saluda(apaterno,amaterno,nombre):
    print(f"Paterno: {apaterno}, Materno: {amaterno}, Nombre: {nombre}")


saluda("Dominguez","Valdez","Jorge")
saluda(nombre="Jorge",apaterno="Dominguez",amaterno="Valdez")
saluda(amaterno="Bernal",nombre="Rocio",apaterno="Soto",)

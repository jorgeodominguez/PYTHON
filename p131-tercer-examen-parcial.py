import os
class Jugador:
    def __init__(self,nombre,anionac,sexo,becado):
        self.nombre=nombre
        self.anionac=anionac
        self.sexo=sexo
        self.becado=becado
    def __str__(self):
        return f'Nombre: {self.nombre:<20} Año Nacimiento: {self.anionac:<10} Sexo: {self.sexo:<10} Becado: {self.becado:<10}'
    
class Categoria:
    def __init__(self,nombre,rango,costo):
        self.nombre=nombre
        self.rango=rango
        self.costo=costo
        self.jugadores=list()
    def agregarJugador(self,jugador):
        self.jugadores.append(jugador)
    def costoCategoria(self,anionac,becado):
        costo=0
        if anionac>=2006 and anionac<=2008 and becado!="Becado":
            costo=1250
        elif anionac>=2009 and anionac<=2011 and becado!="Becado":
            costo=850
        elif anionac>=2012 and anionac<=2014 and becado!="Becado":
            costo=700
        else:
            costo=0
        return costo
    def __str__(self):
        return f'Nombre: {self.nombre:<15} Rango: {self.rango:<20} Costo: ${self.costo:<10}'

class Academia:
    def __init__(self,nombre,propietario,domicilio):
        self.nombre=nombre
        self.propietario=propietario
        self.domicilio=domicilio
        self.categorias=list()
    def agregarCategoria(self,categoria):
        self.categorias.append(categoria)
    def __str__(self):
        return f'\nNombre: {self.nombre}\nPropietario: {self.propietario}\nDomicilio: {self.domicilio}\n'
    
def main():
    os.system('cls')
    print('REPORTE DEL CLUB DEPORTIVO')
    miacademia=Academia(nombre='Academia Santos Laguna',domicilio='Aguanaval 123, Hidraulica',propietario='Francisco Nava')
    miacademia.agregarCategoria(Categoria(nombre='Junior A',rango='2006/2007/2008',costo=1250))
    miacademia.agregarCategoria(Categoria(nombre='Junior B',rango='2009/2010/2011',costo=850))
    miacademia.agregarCategoria(Categoria(nombre='Pony A',rango='2012/2013/2014',costo=700))
    miacademia.categorias[0].agregarJugador(Jugador(nombre='Alexander Lopez',anionac=2006,sexo='Hombre',becado='Sin Beca'))
    miacademia.categorias[0].agregarJugador(Jugador(nombre='Uriel Puga',anionac=2007,sexo='Hombre',becado='Becado'))
    miacademia.categorias[0].agregarJugador(Jugador(nombre='Alejandra Escalona',anionac=2008,sexo='Mujer',becado='Sin Beca'))
    miacademia.categorias[1].agregarJugador(Jugador(nombre='Armando Santana',anionac=2009,sexo='Hombre',becado='Sin Beca'))
    miacademia.categorias[1].agregarJugador(Jugador(nombre='Daniel Mijares',anionac=2010,sexo='Hombre',becado='Sin Beca'))
    miacademia.categorias[1].agregarJugador(Jugador(nombre='Antonio Hernandez',anionac=2011,sexo='Mujer',becado='Becado'))
    miacademia.categorias[2].agregarJugador(Jugador(nombre='Andrea Solis',anionac=2012,sexo='Mujer',becado='Becado'))
    miacademia.categorias[2].agregarJugador(Jugador(nombre='Marissa Hernandez',anionac=2013,sexo='Mujer',becado='Becado'))
    miacademia.categorias[2].agregarJugador(Jugador(nombre='Diana Soto',anionac=2014,sexo='Mujer',becado='Sin Beca'))

    #Reporte
    print(miacademia)
    print(f'Total de Categorias: {len(miacademia.categorias)}')
    tothom=0
    totmuj=0
    for categoria in miacademia.categorias:
        for jugador in categoria.jugadores:
            if jugador.sexo=="Hombre":
                tothom+=1
            elif jugador.sexo=="Mujer":
                totmuj+=1
    print(f'Total de Hombres: {tothom}')
    print(f'Total de Mujeres: {totmuj}')
    print('\n>> Datos generales de las Categorias')
    print()
    for categoria in miacademia.categorias:
        print(categoria)
    print('\n>> Jugadores por Categoria: ')
    total=0
    for categoria in miacademia.categorias:
        print(f"\n> {categoria.nombre} - {categoria.rango} - ({len(categoria.jugadores)})")
        print()
        subtotal=0
        for jugador in categoria.jugadores:
            print(jugador)
            subtotal=subtotal+categoria.costoCategoria(jugador.anionac,jugador.becado)
        total+=subtotal
        print(f'\n- SubTotal: ${subtotal}')

    print(f'\n->TOTAL: ${total}')
    print()

if __name__ == "__main__":
    main()
    
    
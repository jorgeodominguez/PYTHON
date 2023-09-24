#Primer examen parcial
#Jorge Dominguez

import os

sub=des=por=tot=sub_usu=sub_tip=sum_ven=0

while(True):
    os.system("cls")
    print("Univercidad patito SA de CV")
    print("Sistema de Inscripción de Sistemas")

    print("\n[1]Alumno $100, [2]Trabajador $200, [3]Docente $500")
    usu=int(input("Que tipo de Usuario: "))
    print("\n[1]Solo conferencia $600, [2]Con Eventos Sociales $800, [3]Kit de acceso $900")
    tip=int(input("Que tipo de Paquete: "))
    can=int(input("\nCantidad: "))

    if usu>=1 and usu<=3 and tip>=1 and tip<=3 and can>0:
        if usu==1:
            can_usu=100
            nom_usu="Alumno"
        if usu==2:
            can_usu=200
            nom_usu="Trabajador"
        if usu==3:
            can_usu=500
            nom_usu="Docente"
        if tip==1:
            can_tip=600
            nom_tip="Solo Conferencia"
        if tip==2:
            can_tip=800
            nom_tip="Con eventos sociales"
        if tip==3:
            can_tip=900
            nom_tip="Con kit de acceso"
        
        sub_usu=can*can_usu
        sub_tip=can*can_tip
        sub=sub_usu+sub_tip

        if sub>5000:
            if usu==1:
                por=20
            if usu==2:
                por=10
            if usu==3:
                por=5
        
        des=sub*(por/100)
        tot=sub-des
        sum_ven=tot+sum_ven

        print(f"\nTu pedido fue: {can}, Tipo de usuario: {nom_usu}, Tipo de paquete: {nom_tip}")
        print(f"Subtotal= {sub}")
        print(f"Descuento= {des} ({por}%)")
        print(f"Total= {tot}")
    else:
        print("\nNo Capturo los datos correctos")

    res=input("\nDeseas continuar (S/N): ").upper()
    if res=='N':
        break
print(f"Importe de la venta= {sum_ven}")
print("\n Proceso terminado ...")





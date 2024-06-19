#paquetes
import sys
def validar(dato):
    i = 0
    c = 0
    for nom in dato:
        if nom ==" ":
            i +=1
        else:
            c +=1
    if c >= 4 and i <= 6 and i>= 1:
        return False
    else:
        return True
def sect(sector):
    sector.lower
    if sector == "norte" or sector == "centro" or sector == "sur":
        return False
    else:
        return True
def datospersonas(usuarios):
    for personas in usuarios:
        print("\n")
        for datos in personas:
            print(datos, end=", ")
def texto(usua_sect):
    x = open('registro.txt','x','w', newline="")
    for datos in usua_sect:
        if datos[2].lower == "norte":
            for dato in datos:
                x.write(dato) 
    for datos in usua_sect:    
        if datos[2].lower =="centro":
            for dato in datos:
                x.write(dato)
    for datos in usua_sect:    
        if datos[2].lower == "sur":
            for dato in datos:
                x.write(dato)
datos_personas = []    
while True:
    menu = input("\nBienvenido a PaquExpress\nPor favor ingrese un numero del 1 al 4\n1)Registrar pedidos\n2)Listar todos los pedidos\n3)Imprimir hoja de ruta\n4)Salir del menu")
    if menu == "1":
        x = True
        while x == True:
            nombre = input("Ingrese su nombre y su apellido (con un espacio entre nombre y apellido)")
            x = validar(nombre)
            if x == True:
                print("Ingrese un nombre valido")
        x = True
        while x == True:
            direccion = input("Ingrese su direccion(calle y numero separados por un espacio)")
            x = validar(direccion)
            if x == True:
                print("Ingrese una direccion valida")
        x =True
        while x == True:
            sector = input("Ingrese el sector donde vive(Centro, norte o sur)")
            x = sect(sector)
            if x == True:
                print("Por favor ingrese un sector valido")
        x = True
        while x == True:
            detalle = input("Ingrese el detalle del pedido(paquete grande, mediano o pequeño y la cantidad)")
            detalle.lower
            x = validar(detalle)
            if x == True:
                print("Ingrese datos validos")
        usuario = [nombre,direccion,sector,detalle]
        datos_personas.append(usuario)
    elif menu == "2":
        print("Nombre, direccion, sector, detalle paquete")
        datospersonas(datos_personas)
    elif menu == "3":
        texto(datos_personas)
    elif menu == "4":
        print("Hasta luego que tenga un excelente dia")
        sys.exit




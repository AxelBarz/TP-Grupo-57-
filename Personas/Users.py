import json
from tabulate import tabulate

def agregar_usuario():
    nombre=input("Ingresa nombre de la persona: ")
    apellido=input("Ingresa apellido de la persona: ")
    DNI=input("Ingresa el DNI de la persona: ")
    direccion=input("Ingresa la direccion de la persona: ")
    ciudad=input("Ingresa la ciudad de la persona: ")
    libros=int(input("Ingresa la cantidad de libros prestados y si no tiene libros escribir 0: "))

    nuevo_usuario={
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": DNI,
        "Direccion": direccion,
        "Ciudad": ciudad,
        "Libros": libros
    }

    with open("Personas/Users.json", "r", encoding="utf-8") as usuarios: 
        lista_usuarios=json.load(usuarios)
        lista_usuarios.append(nuevo_usuario)
    with open("Personas/Users.json", "w", encoding="utf-8") as usuarios: 
        json.dump(lista_usuarios, usuarios, indent=4)
        print("USUARIO AGREGADO")

def borrar_usuario():
    DNI=input("Ingresa el DNI del usuario que quieres borrar: ")
    with open("Personas/Users.json", "r", encoding="utf-8") as usuarios: 
        lista_usuarios=json.load(usuarios)
        while True:
            encontrado=False
            for user in lista_usuarios:
                if DNI in user.values():
                    lista_usuarios.remove(user)
                    encontrado=True
                    break
            if encontrado:
                break
            else:
                print("VALOR INCORRECTO!!")
    with open("Personas/Users.json", "w", encoding="utf-8") as usuarios: 
        json.dump(lista_usuarios, usuarios, indent=4)
        print("USUARIO ELIMINADO")

def listar_usuarios():
    menu=" [1] LISTAR TODO \n [2] LISTAR NOMBRE/APELLIDOS \n [3] LISTAR DNIs \n [4] LISTAR DIRECCIONES \n [5] LISTAR CIUDAD \n [6] LISTAR LIBROS DE CADA USUARIO"
    format_table="rounded_grid"
    with open("Personas/Users.json", "r", encoding="utf-8") as usuarios: 
        listar_usuario=json.load(usuarios)
        print(menu)
        opcion=int(input("Ingresa la opcion que quieras listar: "))
        match opcion:
            case 1:
                tabla=tabulate(listar_usuario, headers = "keys", tablefmt = format_table)
                print(tabla)
            case 2:
                nombres=[[user["Nombre"], user["Apellido"] ]for user in listar_usuario]
                tabla=tabulate(nombres, headers = ["Nombre", "Apellido"], tablefmt = format_table)
                print(tabla)
            case 3:
                print(" [1] NOMBRE/DNI \n [2] SOLO DNI ")
                opcion2=int(input("Opcion seleccionada: "))
                match opcion2:
                    case 1:
                        nom_dni=[[user["Nombre"], user["DNI"]]for user in listar_usuario]
                        tabla=tabulate(nom_dni, headers = ["Nombre", "DNI"], tablefmt = format_table)
                        print(tabla)
                    case 2:
                        dni=[[user["DNI"]] for user in listar_usuario]
                        tabla=tabulate(dni, headers = ["DNI"], tablefmt = format_table, stralign="center")
                        print(tabla)
                    case _:
                        print("VALOR INCORRECTO!!")
            case 4:
                print(" [1] NOMBRE/DIRECCION \n [2] DIRECCION")
                opcion3=int(input("Opcion seleccionada: "))
                match opcion3: 
                    case 1:
                        nom_direcc=[[user["Nombre"], user["Apellido"], user["Direccion"]] for user in listar_usuario]
                        tabla=tabulate(nom_direcc, headers = ["Nombre", "Apellido", "Direccion"], tablefmt = format_table)
                        print(tabla)
                    case 2:
                        direccion=[[user["Direccion"]] for user in listar_usuario]
                        tabla=tabulate(direccion, headers=["Direccion"], tablefmt = format_table)
                        print(tabla)
                    case _:
                        print("VALOR INCORRECTO ")
            case 5:
                print(" [1] NOMBRE/CIUDAD \n [2] CIUDAD")
                opcion4=int(input("Opcion seleccionada: "))
                match opcion4:
                    case 1:
                        nom_ciudad=[[user["Nombre"], user["Apellido"], user["Ciudad"]] for user in listar_usuario]
                        tabla=tabulate(nom_ciudad, headers = ["Nombre", "Apellido", "Ciudad"], tablefmt = format_table)
                        print(tabla)
                    case 2:
                        ciudad=[[user["Ciudad"]] for user in listar_usuario]
                        tabla=tabulate(ciudad, headers=["Ciudad"], tablefmt = format_table)
                        print(tabla)
                    case _:
                        print("VALOR INCORRECTO ")
            case 6:
                libros=[[user["Nombre"], user["Apellido"], user["Libros"] ]for user in listar_usuario]
                tabla=tabulate(libros, headers = ["Nombre", "Apellido", "Libros"], tablefmt = format_table)
                print(tabla)
            case _:
                pass

def modificar_usuario():
    with open("Personas/Users.json", "r", encoding="utf-8") as usuarios: 
        lista_usuario=json.load(usuarios)

        buscar=input("Ingresa el DNI del usuario que quieres modificar: ")
        encontrado=False

        for user in lista_usuario:
            if str(user["DNI"]) == buscar:
                print("persona encontrada")
                opcion=int(input("[1] NOMBRE \n [2] APELLIDO \n [3] DNI \n [4] DIRECCION \n [5] CIUDAD \n [6] CANTIDAD LIBROS \n Seleccione una modificacion:  "))
                match opcion:
                    case 1: 
                        user["Nombre"]=input("Ingresa nuevo nombre: ")
                        print("NOMBRE ACTUALIZADO")
                    case 2: 
                        user["Apellido"]=input("Ingresa nuevo apellido: ")
                        print("APELLIDO ACTUALIZADO")
                    case 3: 
                        user["DNI"]=input("Ingresa nuevo DNI: ")
                        print("DNI ACTUALIZADO")
                    case 4: 
                        user["Direccion"]=input("Ingresa nueva direccion: ")
                        print("DIRECCION ACTUALIZADA")
                    case 5: 
                        user["Ciudad"]=input("Ingresa nueva ciudad: ")
                        print("CIUDAD ACTUALIZADA")
                    case 6: 
                        user["Libros"]=int(input("Ingrese cantidad actualizada de libros: "))
                        print("LIBROS ACTUALIZADOS")
                    case _:
                        print("OPCION MAL SELECCIONADA")
                encontrado=True
                break

        if not encontrado:
            print("Persona NO encontrada")
    
    with open("Personas/Users.json", "w", encoding="utf-8") as usuarios:
        json.dump(lista_usuario, usuarios, indent=4, ensure_ascii=False)



def buscar_usuario():
    with open("Personas/Users.json", "r", encoding="utf-8") as usuarios:
        lista_usuario=json.load(usuarios)
        opcion=input("Ingresa dato para buscar: ")
        for user in lista_usuario:
            if user["Nombre"].lower()==opcion.lower() or user["Apellido"].lower()==opcion.lower() or str(user["DNI"])==opcion or user["Direccion"].lower()==opcion.lower() or user["Ciudad"].lower()==opcion.lower():
                tabla=tabulate(user.items(), headers = ["-----", "Usuario"], tablefmt = "rounded_grid")
                print(tabla)



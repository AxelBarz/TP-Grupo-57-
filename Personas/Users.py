import json
from tabulate import tabulate
from colorama import *
from Personas.mini_funciones import limpiar_pantalla, pedir_dato

init(autoreset=True)

def agregar_usuario():
    limpiar_pantalla()
    print(Back.WHITE+Style.BRIGHT+"█████████████████ AGREGAR USUARIO ██████████████████████")
    verde=Fore.LIGHTGREEN_EX

    nombre=pedir_dato(verde+"Ingresa nombre de la persona: ")
    apellido=pedir_dato(verde+"Ingresa apellido de la persona: ")
    dni=pedir_dato(verde+"Ingresa el DNI de la persona: ")
    direccion=pedir_dato(verde+"Ingresa la direccion de la persona: ")
    ciudad=pedir_dato(verde+"Ingresa la ciudad de la persona: ")

    nuevo_usuario={
        "Nombre": nombre,
        "Apellido": apellido,
        "dni": dni,
        "Direccion": direccion,
        "Ciudad": ciudad,
    }

    with open("Personas/Users.json", "r", encoding="utf-8") as usuarios: 
        lista_usuarios=json.load(usuarios)
        lista_usuarios.append(nuevo_usuario)
    with open("Personas/Users.json", "w", encoding="utf-8") as usuarios: 
        json.dump(lista_usuarios, usuarios, indent=4)
        limpiar_pantalla()
        print(Fore.GREEN+Style.BRIGHT+"USUARIO AGREGADO")

def borrar_usuario():
    limpiar_pantalla()
    print(Back.WHITE+Style.BRIGHT+"█████████████████ BORRAR USUARIO ██████████████████████")
    dni=input(Fore.LIGHTRED_EX+"Ingresa el DNI del usuario que quieres borrar: ")
    with open("Personas/Users.json", "r", encoding="utf-8") as usuarios: 
        lista_usuarios=json.load(usuarios)
        while True:
            encontrado=False
            for user in lista_usuarios:
                if dni in user.values():
                    lista_usuarios.remove(user)
                    encontrado=True
                    break
            if encontrado:
                break
            else:
                print(Back.RED+"VALOR INCORRECTO!!")
    with open("Personas/Users.json", "w", encoding="utf-8") as usuarios: 
        json.dump(lista_usuarios, usuarios, indent=4)
        print(Back.LIGHTRED_EX+"USUARIO ELIMINADO")

def listar_usuarios():
    limpiar_pantalla()
    print(Back.WHITE+Style.BRIGHT+"█████████████████ LISTAR USUARIO ██████████████████████")
    menu=Fore.MAGENTA+Style.BRIGHT+" [1] LISTAR TODO \n [2] LISTAR NOMBRE/APELLIDOS \n [3] LISTAR DNIs \n [4] LISTAR DIRECCIONES \n [5] LISTAR CIUDAD"
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
                print(Fore.BLUE+" [1] NOMBRE/DNI \n [2] SOLO DNI ")
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
                        print(Fore.RED+"VALOR INCORRECTO!!")
            case 4:
                print(Fore.BLUE+" [1] NOMBRE/DIRECCION \n [2] DIRECCION")
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
                        print(Fore.RED+"VALOR INCORRECTO ")
            case 5:
                print(Fore.BLUE+" [1] NOMBRE/CIUDAD \n [2] CIUDAD")
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
                        print(Fore.RED+"VALOR INCORRECTO ")
            case _:
                pass

def modificar_usuario():
    limpiar_pantalla()
    print(Back.WHITE+Style.BRIGHT+"█████████████████ MODIFICAR USUARIO ██████████████████████")
    with open("Personas/Users.json", "r", encoding="utf-8") as usuarios: 
        lista_usuario=json.load(usuarios)

        buscar=input("Ingresa el DNI del usuario que quieres modificar: ")
        encontrado=False

        for user in lista_usuario:
            if str(user["dni"]) == buscar:
                print(Back.GREEN+"persona encontrada")
                opcion=int(input(Fore.YELLOW+" [1] NOMBRE \n [2] APELLIDO \n [3] DNI \n [4] DIRECCION \n [5] CIUDAD \n Seleccione una modificacion:  "))
                match opcion:
                    case 1: 
                        user["Nombre"]=input(f"Antiguo nombre: {user['Nombre']} ║║║║ Nuevo nombre: ")
                        print(Fore.GREEN+Style.BRIGHT+"NOMBRE ACTUALIZADO")
                    case 2: 
                        user["Apellido"]=input(f"Antiguo apellido: {user['Apellido']} ║║║║ Nuevo apellido: ")
                        print(Fore.GREEN+Style.BRIGHT+"APELLIDO ACTUALIZADO")
                    case 3: 
                        user["dni"]=input(f"Antiguo DNI: {user['dni']} ║║║║ Nuevo DNI: ")
                        print(Fore.GREEN+Style.BRIGHT+"DNI ACTUALIZADO")
                    case 4: 
                        user["Direccion"]=input(f"Antigua direccion: {user['Direccion']} ║║║║ Nueva direccion: ")
                        print(Fore.GREEN+Style.BRIGHT+"DIRECCION ACTUALIZADA")
                    case 5: 
                        user["Ciudad"]=input(f"Antigua ciudad: {user['Ciudad']} ║║║║ Nueva ciudad: ")
                        print(Fore.GREEN+Style.BRIGHT+"CIUDAD ACTUALIZADA")
                    case _:
                        print(Fore.RED+"OPCION MAL SELECCIONADA")
                encontrado=True
                break

        if not encontrado:
            print(Back.RED+"Persona NO encontrada")
    
    with open("Personas/Users.json", "w", encoding="utf-8") as usuarios:
        json.dump(lista_usuario, usuarios, indent=4, ensure_ascii=False)



def buscar_usuario():
    limpiar_pantalla()
    print(Back.WHITE+Style.BRIGHT+"█████████████████ BUSCAR USUARIO ██████████████████████")
    with open("Personas/Users.json", "r", encoding="utf-8") as usuarios:
        lista_usuario=json.load(usuarios)
        opcion=input("Ingresa dato para buscar: ")
        encontrado=False
        for user in lista_usuario:
            if user["Nombre"].lower()==opcion.lower() or user["Apellido"].lower()==opcion.lower() or str(user["dni"])==opcion or user["Direccion"].lower()==opcion.lower() or user["Ciudad"].lower()==opcion.lower():
                tabla=tabulate(user.items(), headers = ["-----", "Usuario"], tablefmt = "rounded_grid")
                print(tabla)
                encontrado=True
        if not encontrado:
            print(Fore.RED + Style.BRIGHT + "NO EXISTE EL DATO INGRESADO")


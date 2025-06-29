import json
from datetime import date
from tabulate import tabulate

prestamos = []

def cargar_prestamos():
    global prestamos
    try:
        with open("Prestamos/prestamos.json", "r", encoding="utf-8") as archivo:
            prestamos = json.load(archivo)
    except FileNotFoundError:
        print("El archivo no existe, se creará al guardar")
        prestamos = []


def guardar_prestamo():
    with open("Prestamos/prestamos.json", "w", encoding="utf-8") as archivo:
        json.dump(prestamos,archivo)


def agregar_prestamo():
    global prestamos

    print("→ AGREGAR UN NUEVO PRESTAMO ←")
    
    dni = input("Ingrese el DNI del usuario: ")

    if not usuario_registrado(dni):
        print("El DNI ingresado no pertenece a un usuario registrado.")
        return

    usuario = obtener_usuario_por_dni(dni)

    if usuario is None:
        print(f"Error al obtener los datos del usuario.")
        return
    
    nombre = usuario["Nombre"]
    apellido = usuario["Apellido"]

    cantidad = contador_prestamos_por_persona(dni)
    if cantidad >= 3:
        print("El usuario ya posee 3 libros en su haber.")
        print("Debe devolver al menos uno para poder solicitar un nuevo préstamo.")
        return

    titulo = input("Ingrese el título del libro solicitado: ")

    if not stock_libro(titulo):
        print("El libro ingresado no está disponible en la biblioteca.")
        return
    
    dni_prestamo = libro_prestado(titulo)
    if dni_prestamo is not None:
        usuario_prestamo = obtener_usuario_por_dni(dni_prestamo)

        nombre_prestamo = usuario_prestamo["Nombre"]
        apellido_prestamo = usuario_prestamo["Apellido"]

        print(f"Este libro ya se encuentra prestado al usuario {nombre_prestamo} {apellido_prestamo} con DNI: {dni_prestamo}")
        return

    fecha = str(date.today())

    nuevo_prestamo = {"dni": dni, "nombre": nombre, "apellido": apellido, "titulo": titulo, "fecha": fecha}

    prestamos.append(nuevo_prestamo)
    guardar_prestamo()
    
    print("Prestamo registrado correctamente.")



def eliminar_prestamo():
    global prestamos

    if len(prestamos) == 0:
        print("No hay préstamos actualmente.")
    
    else:
        print("")
        print("_-_-_ ELIMINAR PRÉSTAMO _-_-_")

    tabla = []

    for i, prestamo in enumerate(prestamos):
        tabla.append([i+1, prestamo["apellido"], prestamo["nombre"], prestamo["dni"], prestamo["titulo"], prestamo["fecha"]])

    encabezados = ["N°", "Apellido", "Nombre", "DNI", "Libro", "Fecha del préstamo"]

    print("")
    print(tabulate(tabla, headers = encabezados, tablefmt = "grid"))

    while True:
        num_prestamo = input("Ingrese el número del préstamo que desea eliminar (o 'x' para cancelar): ")

        if num_prestamo.lower() == "x":
            print("Eliminación cancelada.")
            break

        try:
            num_prestamo = int(num_prestamo)
            if 1 <= num_prestamo <= len(prestamos):
                eliminado = prestamos.pop(num_prestamo - 1)
                guardar_prestamo()
                print(f"Préstamo eliminado correctamente.")
                print(f"Correspondiente al libro: {eliminado['titulo']} | DNI: {eliminado['dni']}")
                break
            else:
                print("Número fuera de rango. Intente nuevamente.")

        except ValueError:
            print("Entrada inválida. Debe ingresar un número o 'x' para cancelar.")


def contador_prestamos_por_persona(dni):
    contador = 0
    for prestamo in prestamos:
        if prestamo["dni"] == dni:
            contador += 1
    return contador


def usuario_registrado(dni):
    try:
        with open("Personas/Users.json", "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)
            for usuario in usuarios:
                if usuario["dni"] == dni:
                    return True
                
    except FileNotFoundError:
        print("Archivo usuarios no encontrado.")
    return None


def stock_libro(titulo):
    try:
        with open("libros/libros.json", "r", encoding="utf-8") as archivo:
            libros = json.load(archivo)
            for libro in libros:
                if libro["titulo"].lower() == titulo.lower():
                    return True
    
    except FileNotFoundError:
        print("Archivo Libros no encontrado.")
    return False


def libro_prestado(titulo):
    for prestamo in prestamos:
        if prestamo["titulo"].lower() == titulo.lower():
            return prestamo["dni"]
    return None


def obtener_usuario_por_dni(dni):
    try:
        with open("Personas/Users.json", "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)
            for usuario in usuarios:
                if usuario["dni"] == str(dni):
                    return usuario
                
    except FileNotFoundError:
        print("Archivo de Usuarios no encontrado.")
    return "Usuario desconocido."


def modificar_prestamo():
    global prestamos

    if len(prestamos) == 0:
        print("No hay prestamos para modificar")
    
    print("_-_-_ MODIFICAR PRÉSTAMO _-_-_")
    for i, prestamo in enumerate(prestamos):
        print(f"{i+1}. {prestamo["nombre"]} {prestamo["apellido"]} DNI: {prestamo["dni"]}")
        print(f"Libro: {prestamo["titulo"]} Retirado el: {prestamo["fecha"]}")
        print("")

    while True:
        try:
            opcion = int(input("Indique el número correspondiente al préstamo que desea modificar: "))
            if 1 <= opcion <= len(prestamos):
                break #si el número ingresado es válido, sale del bucle
            else:
                print("El número ingresado no corresponde a ninguno de la lista. Intente nuevamente.")
                print("")
        except ValueError:
            print("Por favor ingrese un número.")
            print("")

    indice = opcion - 1
    prestamo = prestamos[indice]

    print(f"Seleccionaste el préstamo de {prestamo["nombre"]} {prestamo["apellido"]}")
    print(f"Correspondiente al libro: {prestamo["titulo"]}")
    print("")

    while True:
        print("---- ¿Qué desea modificar? ----")
        print("1. DNI del usuario")
        print("2. Título del libro")
        
        eleccion = input("Ingrese 1 o 2: ")    

        if eleccion == "1":
            while True:
                nuevo_dni = input("Ingrese el nuevo DNI: ")

                if usuario_registrado(nuevo_dni):
                    break
                else:
                    print(f"El usuario ingresado no está registrado. Ingrese un usuario válido.")

            cantidad = contador_prestamos_por_persona(nuevo_dni)
            if cantidad >= 3:
                print("El usuario ingresado ya cuenta con 3 libros en su haber.")
                return
            
            usuario_nuevo = obtener_usuario_por_dni(nuevo_dni)
            prestamo["dni"] = nuevo_dni
            prestamo["nombre"] = usuario_nuevo["nombre"]
            prestamo["apellido"] = usuario_nuevo["apellido"]

            guardar_prestamo()
            print("Datos de usuario modificados correctamente.")
            return

        elif eleccion == "2":
            while True:
                nuevo_titulo = input("Ingrese el nuevo libro: ")

                if not stock_libro(nuevo_titulo):
                    print("El libro ingresado no se encuentra en la biblioteca.")
                else:
                    dni_prestamo = libro_prestado(nuevo_titulo)

                    if dni_prestamo is not None and dni_prestamo != prestamo["dni"]:
                        usuario_actual = obtener_usuario_por_dni(dni_prestamo)
                        print(f"El libro ingresado ya se encuentra prestado a {usuario_actual["nombre"]} {usuario_actual["apellido"]}")
                        print(f"DNI: {usuario_actual["dni"]}. Intente con otro libro.")
                    else:
                        break #si el libro está disponible

            prestamo["titulo"] = nuevo_titulo
            guardar_prestamo()
            print("Libro modificado correctamente.")
            return

        else:
            print("La opción ingresada no es válida. Intente nuevamente.")


def informe_prestamos():
    global prestamos

    if len(prestamos) == 0:
        print("No hay prestamos actualmente para mostrar.")
        return
    
    else:
        print("Antes de generar el informe, por favor ingrese el orden deseado:")
        print("1. Por fecha")
        print("2. Por apellido")

    while True:
        
        print("")
        opcion = input("Ingrese 1 o 2: ")

        if opcion == "1":
            prestamos_ordenados = sorted(prestamos, key=lambda x: x["fecha"])
            print("")
            print("---- INFORME DE PRÉSTAMOS ORDENADOS POR FECHA ----")
            break

        elif opcion == "2":
            prestamos_ordenados = sorted(prestamos, key=lambda x: x["apellido"])
            print("")
            print("---- INFORME DE PRÉSTAMOS ORDENADOS POR APELLIDO ----")
            break

        else:
            print("Ha ingresado una opción inválida. Por favor intente nuevamente.")

    tabla = []

    for i, prestamo in enumerate(prestamos_ordenados):
        tabla.append([i+1, prestamo["apellido"], prestamo["nombre"], prestamo["dni"], prestamo["titulo"], prestamo["fecha"]])

    encabezados = ["N°", "Apellido", "Nombre", "DNI", "Libro", "Fecha del préstamo"]
    
    print("")
    print(tabulate(tabla, headers = encabezados, tablefmt = "grid"))
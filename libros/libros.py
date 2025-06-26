import json
from tabulate import tabulate

ARCHIVO_JSON = "libros.json"

def cargar_libros():
    try:
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_libros(libros):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(libros, archivo, indent=4, ensure_ascii=False)

def agregar_libro():
    titulo = input("Título: ").upper()
    edicion = input("Edición: ").upper()
    editorial = input("Editorial: ").upper()
    autor = input("Autor: ").upper()
    nuevo = {
        "titulo": titulo,
        "edicion": edicion,
        "editorial": editorial,
        "autor": autor
    }
    libros = cargar_libros()
    libros.append(nuevo)
    guardar_libros(libros)
    print("El libro fue guardado con exito!.")

def mostrar_libros():
    libros = cargar_libros()
    if libros:
        tabla = []
        for i, libro in enumerate(libros, 1):
            tabla.append([
                i,
                libro['titulo'],
                libro['autor'],
                libro['editorial'],
                libro['edicion']
            ])
        print(tabulate(tabla, headers=["N°", "Título", "Autor", "Editorial", "Edición"], tablefmt="fancy_grid"))
    else:
        print("No hay libros cargados.")

def modificar_libro():
    libros = cargar_libros()
    mostrar_libros()
    try:
        indice = int(input("Ingrese el número del libro a modificar: ")) - 1
        if 0 <= indice < len(libros):
            print("Deje en blanco si no desea modificar ese campo.")
            titulo = input(f"Nuevo título ({libros[indice]['titulo']}): ").upper() or libros[indice]['titulo']
            edicion = input(f"Nueva edición ({libros[indice]['edicion']}): ").upper() or libros[indice]['edicion']
            editorial = input(f"Nueva editorial ({libros[indice]['editorial']}): ").upper() or libros[indice]['editorial']
            autor = input(f"Nuevo autor ({libros[indice]['autor']}): ").upper() or libros[indice]['autor']

            libros[indice] = {
                "titulo": titulo,
                "edicion": edicion,
                "editorial": editorial,
                "autor": autor
            }
            guardar_libros(libros)
            print("Libro modificado correctamente.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def eliminar_libro():
    libros = cargar_libros()
    mostrar_libros()
    try:
        indice = int(input("Ingrese el número del libro a eliminar: ")) - 1
        if 0 <= indice < len(libros):
            eliminado = libros.pop(indice)
            guardar_libros(libros)
            print(f"Libro '{eliminado['titulo']}' eliminado.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    while True:
        print("\n BIENVENIDO AL SECTOR DE LIBROS ")
        print("1. Agregar libro")
        print("2. Mostrar libros")
        print("3. Modificar libro")
        print("4. Eliminar libro")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_libro()
        elif opcion == '2':
            mostrar_libros()
        elif opcion == '3':
            modificar_libro()
        elif opcion == '4':
            eliminar_libro()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()

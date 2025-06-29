from Prestamos import prestamos
from Personas import Users
from libros import libros

def menu_principal():
  print("\n📚 Sistema de Gestión de Biblioteca 📚")
  print("\nMenú principal:")
  print("1. Usuarios")
  print("2. Libros")
  print("3. Préstamos")
  print("0. Salir")

# Menus secundarios
def menu_usuarios():
  while True:
    print("\n--- Gestión de Usuarios ---")
    print("1. Crear usuario")
    print("2. Eliminar usuario")
    print("3. Modificar usuario")
    print("4. Buscar usuario")
    print("5. Informe de usuarios")
    print("6. Volver al menú principal")

    opcion = input("Seleccioná una opción: ")
    match opcion:
      case "1":
        Users.agregar_usuario()
        break
      case "2":
        Users.borrar_usuario()
        break
      case "3":
        Users.modificar_usuario()
        break
      case "4":
        Users.buscar_usuario()
        break
      case "5":
        Users.listar_usuarios()
        break
      case "6":
        break
      case _:
        print("❌ Por favor, seleccione una opcion valida:")

def menu_libros():
  while True:
    print("\n--- Gestión de Libros ---")
    print("1. Ingresar libro")
    print("2. Modificar libro")
    print("3. Eliminar libro")
    print("4. Informe de libros")
    print("5. Volver al menú principal")

    opcion = input("Seleccioná una opción: ")
    match opcion:
      case "1":
        libros.agregar_libro()
        break
      case "2":
        libros.modificar_libro()
        break
      case "3":
        libros.eliminar_libro()
        break
      case "4":
        libros.mostrar_libros()
        break
      case "5":
        break
      case _:
        print("❌ Por favor, seleccione una opcion valida:")

def menu_prestamos():
  while True:
    prestamos.cargar_prestamos()
    print("\n--- Gestión de Préstamos ---")
    print("1. Agregar un nuevo préstamo")
    print("2. Eliminar préstamo existente")
    print("3. Modificar un prestamo")
    print("4. Informe de préstamos")
    print("5. Volver al menú principal")

    opcion = input("Seleccioná una opción: ")
    match opcion:
      case "1":
        prestamos.agregar_prestamo()
      case "2":
        prestamos.eliminar_prestamo()
      case "3":
        prestamos.modificar_prestamo()
      case "4":
        prestamos.informe_prestamos()
      case "5":
        break
      case _:
        print("❌ Por favor, seleccione una opcion valida:")


# Menú principal
while True:
  menu_principal()
  opcion = input("Seleccioná una opción: ")
  match opcion:
    case "0":
      print("👋 Saliendo del sistema...")
      break
    case "1":
      menu_usuarios()
    case "2":
      menu_libros()
    case "3":
      menu_prestamos()
    case _:
      print("❌ Por favor, seleccione una opcion valida:")
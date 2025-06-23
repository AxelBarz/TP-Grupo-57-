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
    print("3. Editar usuario")
    print("4. Informe de usuarios")
    print("5. Volver al menú principal")

    opcion = input("Seleccioná una opción: ")
    match opcion:
      case "1":
        print("Crear usuario (función a implementar)")
        break
      case "2":
        print("Eliminar usuario (función a implementar)")
        break
      case "3":
        print("Editar usuario (función a implementar)")
        break
      case "4":
        print("Informe de usuarios (función a implementar)")
        break
      case "5":
        break
      case _:
        print("❌ Por favor, seleccione una opcion valida:")

def menu_libros():
  while True:
    print("\n--- Gestión de Libros ---")
    print("1. Ingresar libro")
    print("2. Editar libro")
    print("3. Eliminar libro")
    print("4. Informe de libros")
    print("5. Volver al menú principal")

    opcion = input("Seleccioná una opción: ")
    match opcion:
      case "1":
        print("Ingresar libro (función a implementar)")
        break
      case "2":
        print("Eliminar libro (función a implementar)")
        break
      case "3":
        print("Editar libro (función a implementar)")
        break
      case "4":
        print("Informe de libros (función a implementar)")
        break
      case "5":
        break
      case _:
        print("❌ Por favor, seleccione una opcion valida:")

def menu_prestamos():
  while True:
    print("\n--- Gestión de Préstamos ---")
    print("1. Agregar préstamo")
    print("2. Eliminar préstamo")
    print("3. Informe de préstamos")
    print("4. Volver al menú principal")

    opcion = input("Seleccioná una opción: ")
    match opcion:
      case "1":
        print("Agregar préstamo (función a implementar)")
      case "2":
        print("Eliminar préstamo (función a implementar)")
      case "3":
        print("Informe de préstamos (función a implementar)")
      case "4":
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
from productos import mostrar_productos, buscar_producto
from pedidos import crear_pedido, ver_pedidos
from inventario import reducir_inventario
from almacenamiento import cargar_productos, guardar_productos, cargar_pedidos, guardar_pedidos

def menu_principal():
    while True:
        print("Menú Principal")
        print("1. Ingresar como Cliente")
        print("2. Ingresar como Administrador")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cliente_menu()
        elif opcion == "2":
            admin_menu()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def cliente_menu():
    while True:
        print("\nMenú Cliente")
        print("1. Ver productos")
        print("2. Crear un pedido")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            crear_pedido()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def admin_menu():
    while True:
        print("\nMenú Administrador")
        print("1. Ver pedidos")
        print("2. Ver productos")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_pedidos()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")


menu_principal()

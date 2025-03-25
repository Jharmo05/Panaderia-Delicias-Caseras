from almacenamiento import cargar_productos, guardar_productos

productos = cargar_productos()

def mostrar_productos():
    print("\nLista de Productos Disponibles:")
    for producto in productos:
        print(f"Codigo: {producto['codigo_producto']}, Nombre: {producto['nombre']}, Categoria: {producto['categoria']}, Precio: {producto['precio_venta']}")

def buscar_producto(codigo):
    for producto in productos:
        if producto["codigo_producto"] == codigo:
            return producto
    return None

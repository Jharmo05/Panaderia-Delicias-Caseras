from productos import buscar_producto
from almacenamiento import cargar_pedidos, guardar_pedidos, cargar_productos
from inventario import reducir_inventario

pedidos = cargar_pedidos()

def crear_pedido():
    codigo_cliente = input("Ingrese su código de cliente: ")
    fecha_pedido = input("Ingrese la fecha del pedido (YYYY-MM-DD): ")
    detalles_pedido = []

    while True:
        codigo_producto = input("Ingrese el código del producto: ")
        producto = buscar_producto(codigo_producto)

        if producto is None:
            print("Producto no encontrado.")
            continue

        cantidad = int(input(f"Ingrese la cantidad de {producto['nombre']} que desea: "))
        if producto["cantidad_en_stock"] < cantidad:
            print(f"No hay suficiente stock de {producto['nombre']}. Solo hay {producto['cantidad_en_stock']} disponibles.")
            continue
        
        precio_unidad = producto["precio_venta"]
        detalles_pedido.append({
            "codigo_producto": codigo_producto,
            "cantidad": cantidad,
            "precio_unidad": precio_unidad,
            "numero_linea": len(detalles_pedido) + 1
        })

        otro_producto = input("¿Desea agregar otro producto? (s/n): ")
        if otro_producto.lower() != "s":
            break

    codigo_pedido = len(pedidos) + 1
    pedidos.append({
        "codigo_pedido": codigo_pedido,
        "codigo_cliente": codigo_cliente,
        "fecha_pedido": fecha_pedido,
        "detalles_pedido": detalles_pedido
    })

    guardar_pedidos(pedidos)
    for detalle in detalles_pedido:
        reducir_inventario(detalle["codigo_producto"], detalle["cantidad"])

    print(f"Pedido {codigo_pedido} creado con éxito.")

def ver_pedidos():
    print("\nLista de Pedidos:")
    for pedido in pedidos:
        print(f"Codigo Pedido: {pedido['codigo_pedido']}, Cliente: {pedido['codigo_cliente']}, Fecha: {pedido['fecha_pedido']}")
        for detalle in pedido["detalles_pedido"]:
            print(f"  Producto: {detalle['codigo_producto']}, Cantidad: {detalle['cantidad']}, Precio: {detalle['precio_unidad']}")

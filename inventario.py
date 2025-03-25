from productos import buscar_producto

def reducir_inventario(codigo_producto, cantidad):
    producto = buscar_producto(codigo_producto)
    if producto:
        producto["cantidad_en_stock"] -= cantidad
        print(f"Inventario actualizado. {producto['nombre']} ahora tiene {producto['cantidad_en_stock']} unidades.")

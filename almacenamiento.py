import json

def cargar_productos():
    try:
        with open('productos.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_productos(productos):
    with open('productos.json', 'w') as f:
        json.dump(productos, f, indent=4)

def cargar_pedidos():
    try:
        with open('pedidos.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_pedidos(pedidos):
    with open('pedidos.json', 'w') as f:
        json.dump(pedidos, f, indent=4)

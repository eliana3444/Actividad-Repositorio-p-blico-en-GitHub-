from tabulate import tabulate

from backend import obtener_todos_los_productos, obtener_producto_por_id
from utils import limpiar


def mostrar_menu():
    """
    Limpia pantalla, muestra el menú principal y retorna la opción ingresada.
    """
    limpiar()
    print("=" * 40)
    print("       SISTEMA DE PRODUCTOS")
    print("=" * 40)
    print("1. Listar productos")
    print("2. Consultar producto por ID")
    print("3. Salir")
    print("=" * 40)
    opcion = input("Seleccione una opción: ")
    return opcion


def mostrar_todos_los_productos():
    """
    Obtiene todos los productos del backend y los muestra en formato tabla.
    """
    productos = obtener_todos_los_productos()
    
    if not productos:
        print("No hay productos registrados.")
    else:
        tabla = [[p["Id"], p["Nombre"], p["Precio"], p["Cantidad"]] for p in productos]
        encabezados = ["Id", "Nombre", "Precio", "Cantidad"]
        print(tabulate(tabla, headers=encabezados, tablefmt="grid"))
    
    input("\nPresione Enter para continuar...")


def mostrar_producto_por_id():
    """
    Solicita un ID al usuario, busca el producto y lo muestra en formato tabla.
    """
    id_ingresado = input("Ingrese el ID del producto: ")
    
    # Intentar convertir a entero si es numérico
    try:
        id_buscado = int(id_ingresado)
    except ValueError:
        id_buscado = id_ingresado
    
    producto = obtener_producto_por_id(id_buscado)
    
    if producto is None:
        print("Producto no encontrado.")
    else:
        tabla = [[producto["Id"], producto["Nombre"], producto["Precio"], producto["Cantidad"]]]
        encabezados = ["Id", "Nombre", "Precio", "Cantidad"]
        print(tabulate(tabla, headers=encabezados, tablefmt="grid"))
    
    input("\nPresione Enter para continuar...")

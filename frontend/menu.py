from tabulate import tabulate

from backend import obtener_todos_los_productos, obtener_producto_por_id
from backend.productos import actualizar_producto, crear_producto, eliminar_producto
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
    print("3. Crear producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")
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


def mostrar_crear_producto():
    """
    Solicita datos de un producto y lo crea en el backend.
    """
    id_ingresado = input("Ingrese el ID del producto: ")

    try:
        id_producto = int(id_ingresado)
    except ValueError:
        id_producto = id_ingresado

    nombre = input("Ingrese el nombre del producto: ")

    precio_ingresado = input("Ingrese el precio del producto: ")
    try:
        precio = float(precio_ingresado)
    except ValueError:
        precio = precio_ingresado

    cantidad_ingresada = input("Ingrese la cantidad del producto: ")
    try:
        cantidad = int(cantidad_ingresada)
    except ValueError:
        cantidad = cantidad_ingresada

    creado = crear_producto(id_producto, nombre, precio, cantidad)

    if creado:
        print("Producto creado correctamente.")
    else:
        print("Ya existe un producto con ese ID.")

    input("\nPresione Enter para continuar...")


def mostrar_actualizar_producto():
    """
    Solicita un ID, muestra el producto y actualiza sus datos.
    """
    id_ingresado = input("Ingrese el ID del producto a actualizar: ")

    try:
        id_buscado = int(id_ingresado)
    except ValueError:
        id_buscado = id_ingresado

    producto = obtener_producto_por_id(id_buscado)

    if producto is None:
        print("Producto no encontrado.")
        input("\nPresione Enter para continuar...")
        return

    tabla = [[producto["Id"], producto["Nombre"], producto["Precio"], producto["Cantidad"]]]
    encabezados = ["Id", "Nombre", "Precio", "Cantidad"]
    print(tabulate(tabla, headers=encabezados, tablefmt="grid"))

    nombre = input("Ingrese el nuevo nombre del producto: ")

    precio_ingresado = input("Ingrese el nuevo precio del producto: ")
    try:
        precio = float(precio_ingresado)
    except ValueError:
        precio = precio_ingresado

    cantidad_ingresada = input("Ingrese la nueva cantidad del producto: ")
    try:
        cantidad = int(cantidad_ingresada)
    except ValueError:
        cantidad = cantidad_ingresada

    actualizado = actualizar_producto(id_buscado, nombre, precio, cantidad)

    if actualizado:
        print("Producto actualizado correctamente.")
    else:
        print("No se pudo actualizar el producto.")

    input("\nPresione Enter para continuar...")


def mostrar_eliminar_producto():
    """
    Solicita un ID, muestra el producto y pide confirmación para eliminarlo.
    """
    id_ingresado = input("Ingrese el ID del producto a eliminar: ")

    try:
        id_buscado = int(id_ingresado)
    except ValueError:
        id_buscado = id_ingresado

    producto = obtener_producto_por_id(id_buscado)

    if producto is None:
        print("Producto no encontrado.")
        input("\nPresione Enter para continuar...")
        return

    tabla = [[producto["Id"], producto["Nombre"], producto["Precio"], producto["Cantidad"]]]
    encabezados = ["Id", "Nombre", "Precio", "Cantidad"]
    print(tabulate(tabla, headers=encabezados, tablefmt="grid"))

    confirmacion = input("¿Desea eliminar este producto? (S/N): ")

    if confirmacion.upper() == "S":
        eliminado = eliminar_producto(id_buscado)
        if eliminado:
            print("Producto eliminado correctamente.")
        else:
            print("No se pudo eliminar el producto.")
    else:
        print("Eliminación cancelada.")

    input("\nPresione Enter para continuar...")

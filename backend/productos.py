from pathlib import Path

from openpyxl import load_workbook

RUTA_EXCEL = Path(__file__).resolve().parent.parent / "productos.xlsx"


def obtener_todos_los_productos():
    """Lee todos los productos del archivo Excel y devuelve una lista de diccionarios."""
    try:
        libro = load_workbook(RUTA_EXCEL)
    except FileNotFoundError:
        return []

    hoja = libro.active
    productos = []

    for fila in hoja.iter_rows(min_row=2, values_only=True):
        if all(valor is None for valor in fila):
            continue

        id_producto, nombre, precio, cantidad = fila[:4]
        productos.append(
            {
                "Id": id_producto,
                "Nombre": nombre,
                "Precio": precio,
                "Cantidad": cantidad,
            }
        )

    libro.close()
    return productos


def obtener_producto_por_id(id_buscado):
    """Busca un producto por Id en el archivo Excel y devuelve su diccionario o None."""
    try:
        libro = load_workbook(RUTA_EXCEL)
    except FileNotFoundError:
        return None

    hoja = libro.active

    for fila in hoja.iter_rows(min_row=2, values_only=True):
        if all(valor is None for valor in fila):
            continue

        id_producto, nombre, precio, cantidad = fila[:4]
        if id_producto == id_buscado:
            libro.close()
            return {
                "Id": id_producto,
                "Nombre": nombre,
                "Precio": precio,
                "Cantidad": cantidad,
            }

    libro.close()
    return None

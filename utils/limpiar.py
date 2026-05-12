import os


def limpiar():
    """Limpia la consola en Windows, Linux y macOS."""
    os.system("cls" if os.name == "nt" else "clear")

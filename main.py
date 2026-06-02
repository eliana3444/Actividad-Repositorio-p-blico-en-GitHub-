from frontend import (
    mostrar_actualizar_producto,
    mostrar_crear_producto,
    mostrar_eliminar_producto,
    mostrar_menu,
    mostrar_producto_por_id,
    mostrar_todos_los_productos,
)


def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            mostrar_todos_los_productos()
        elif opcion == "2":
            mostrar_producto_por_id()
        elif opcion == "3":
            mostrar_crear_producto()
        elif opcion == "4":
            mostrar_actualizar_producto()
        elif opcion == "5":
            mostrar_eliminar_producto()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")
            input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()

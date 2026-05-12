from frontend import mostrar_menu, mostrar_todos_los_productos, mostrar_producto_por_id


def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            mostrar_todos_los_productos()
        elif opcion == "2":
            mostrar_producto_por_id()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")
            input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()

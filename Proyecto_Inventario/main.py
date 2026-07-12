
import os

from crud.listar import ver_inventario

from crud.agregar import agregar_laptop

from crud.actualizar import actualizar_precio

from crud.eliminar import eliminar_laptop

from crud.buscar import buscar_laptop

from utils.exportar import exportar_csv

# Función para limpiar pantalla

def limpiar_pantalla():
    os.system("cls")
    
    
#Menú princippal

while True:
    limpiar_pantalla()
    print("=================================")
    print("   SISTEMA INVENTARIO LAPTOPS")
    print("=================================")
    print("1. Ver inventario")
    print("2. Buscar laptop")
    print("3. Agregar laptop")
    print("4. Actualizar precio")
    print("5. Eliminar laptop")
    print("6. Exportar a CSV")
    print("0. Salir")
    print("=================================")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        limpiar_pantalla()
        ver_inventario()

    elif opcion == "2":
        limpiar_pantalla()
        buscar_laptop()

    elif opcion == "3":
        limpiar_pantalla()
        agregar_laptop()

    elif opcion == "4":
        limpiar_pantalla()
        actualizar_precio()

    elif opcion == "5":
        limpiar_pantalla()
        eliminar_laptop()

    elif opcion == "6":
        limpiar_pantalla()
        exportar_csv()

    elif opcion == "0":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")
        input("Presione Enter para continuar...")    
import listas as listt

ferreteria_stock_copy = listt.ferreteria_stock




def mostrar_cabecera():
    print(f'{"Producto":<5} / {"Cantidad":<5}')


def mostrar_uno(productos:list, pos:int):
    "Muestra un solo producto con su nombre, cantidad y ubicación."
    print(f'{productos[pos][0]} {productos[pos][1]} {productos[pos][2]} {productos[pos][3]}')

def mostrar_todos(productos:list):
    mostrar_cabecera()
    for i in range(len(productos)):
        mostrar_uno(productos, i)  
    print("\n")

def listar_inventario(lista:list):
    print("\nInventario actual:")
    mostrar_todos(lista)



def reponer_mercaderia(lista:list):
    producto = input("Ingrese el nombre del producto a reponer: ")
    cantidad = int(input("ingrese la cantidad que desea reponer: "))
    for fila in lista:
        for item in fila:
            if item[0] == producto:
                item[1] += cantidad
                print(f"Se han repuesto {cantidad} unidades de {producto}. Nuevo stock: {item[1]}")
                return
    print("Producto no encontrado.")


def vender_mercaderia(lista:list):
    listar_inventario(lista)
    producto = input("Ingrese el nombre del producto a vender: ")
    cantidad = int(input("Ingrese la cantidad a vender: "))
    
    for fila in lista:
        for item in fila:
            if item[0] == producto:
                if item[1] >= cantidad:
                    item[1] -= cantidad
                    print(f"Se han vendido {cantidad} unidades de {producto}. Stock restante: {item[1]}")
                else:
                    print(f"Stock insuficiente para vender {cantidad} unidades. Stock disponible: {item[1]}")
                return
    print("Producto no encontrado.")



def menu():

    while True:
        print("\n=========== MENU DE GESTION DE FERRETERO===========")
        print("1. Reponer Mercaderia.")
        print("2. Vender Mercaderia.")
        print("3. Listar Inventario.")
        print("4. Salir")
        print("===================================================")

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            reponer_mercaderia(ferreteria_stock_copy)
        elif opcion == "2":
            vender_mercaderia(ferreteria_stock_copy)
        elif opcion == "3":
            listar_inventario(ferreteria_stock_copy)
        elif opcion == "4":
            print("Saliendo del Programa .....")
            break
        else:
            print("Opcion invalida, igrese una opcion correcta(1/2/3/4)")



        
import listas as lis
productos1 = lis.productos


def mostrar_cabecera():
    'Muestra una cabezera'
    print(f'{"Producto":<12}  {"Cantidad":<10}  Ubicacion')


def mostrar_uno(productos:list, pos:int):
    'Muestra un solo producto con su nombre, cantidad y ubicacion.'
    print(f'{productos[pos][0]:<12}  {productos[pos][1]:<10}    {productos[pos][2]}')

def mostrar_todos(productos:list):
    mostrar_cabecera()
    for i in range(len(productos)):
        mostrar_uno(productos, i)  
    print("\n")

def alta_productos(lista:list):
    'Da de alta un producto, pidiendole nombre, cantidad, ubicacion'
    elemento = input("Ingrese el elemento que desea agregar a la lista: ")
    cantidad = int(input("Ingrese la cantidad que desea agregar: "))
    fila = int(input("ingrese en la fila de la gondola que los piensa ubicar: "))
    columna = int(input("Ingrese en que columna desea ubicarlo: "))
    ubicacion = [fila, columna]
    lista.append([elemento, cantidad, ubicacion])
    print(f'Elemento "{elemento}" agregado a la lista.')

def baja_productos(lista:list):
    'Da de baja un producto, pidiendole al usuaria a travez de un input, el indice del producto que desea eliminar'
    print("Cual de estos productos desea eliminar?")
    mostrar_todos(lista)
    indice = int(input("Ingrese el índice del producto que desea eliminar: "))
    producto_eliminado = lista.pop(indice-1)
    print(f"Producto {producto_eliminado} eliminado exitosamente")

def modificacion_productos(lista:list):
    'Modifica la cantidad y ubicacion de un producto ya existente'
    print("Cual de estos productos desea modificar?")
    mostrar_todos(lista)
    indice = int(input("Indique con el indice el producto a modificar: "))
    nueva_cantidad = int(input(f"Ingrese la nueva cantidad para {lista[indice-1][0]} (Actual: {lista[indice-1][1]}): "))
    lista[indice -1][1] = nueva_cantidad
    fila = int(input("ingrese en la fila de la gondola que los piensa ubicar: "))
    columna = int(input("Ingrese en que columna desea ubicarlo: "))
    ubicacion_nueva = [fila, columna]
    lista[indice -1][2] = ubicacion_nueva
    print(f'Producto "{lista[indice - 1][0]}" modificado exitosamente.')
    


def menu():
    baja_modif = False
    while True:
        print("\n=========== MENU DE GESTION DE GONDOLA ===========")
        print("1. Ver todos los productos")
        print("2. Dar de alta un producto")
        print("3. Eliminar un producto")
        print("4. Modificar un producto")
        print("5. Productos Ordenado por nombres")
        print("6. Salir")
        print("===================================================")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mostrar_todos(productos1)
        elif opcion == "2":
            alta_productos(productos1)
            baja_modif = True
        elif opcion == "3" and baja_modif == True:
            baja_productos(productos1)
        elif opcion == "4" and baja_modif == True:
            modificacion_productos(productos1)
        elif opcion == "5":
            print("En construccion...")
        elif opcion == "6":
            print("Saliendo del programa....")
            break


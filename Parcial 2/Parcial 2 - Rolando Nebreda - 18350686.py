""" Enunciado:
La biblioteca escolar necesita modernizar su forma de administrar el catálogo de libros y el 
stock de ejemplares disponibles. Tu tarea es desarrollar una aplicación de consola en Python 
que permita cargar, consultar y actualizar el inventario de manera sencilla, manteniendo 
registros persistentes en un archivo CSV.
    
    1. Ingresar títulos (multiples)
        permite cargar varios libros de una vez, el usuario indica la cantidad de libros que 
        quiere cargar. Por cada libro, pedir TITULO (no vacío, no duplicado) y CANTIDAD (>= 0).
    2. Ingresar ejemplares
        sumar una cantidad a un título existente. 
    3. Mostrar catálogo
        listar todos los libros con su stock actual. 
    4. Consultar disponibilidad
        buscar un TITULO y mostrar cuántos ejemplares hay disponibles. 
    5. Listar agotados
        mostrar solo los títulos con CANTIDAD == 0.
    6. Agregar título
        alta de un libro individual (validar duplicados) con su cantidad inicial. 
    7. Actualizar ejemplares
            ○ Préstamo: restar 1 solo si CANTIDAD > 0. 
            ○ Devolución: sumar 1. 
    8. Salir
        finalizar la aplicación. """


#Importa librería de funciones utils
import utils

# Menú de opciones
biblioteca_menu= ["1. Ingresar títulos (múltiples)", 
                  "2. Ingresar ejemplares", 
                  "3. Mostrar catálogo", 
                  "4. Consultar disponibilidad",
                  "5. Listar agotados",
                  "6. Agregar título",
                  "7. Actualizar ejemplares (préstamo/devolución)",
                  "8. Salir"]

# lista para catálogo
catalogo=[]

#crea el archivo si no existe
utils.crear_archivo("catalogo.csv")

#lee el contenido del archivo y lo carga en la lista como diccionarios
utils.lineas_diccionario ("catalogo.csv", catalogo)

#bandera para finalización del programa
finalizado= False

#Todo el programa se encuentra dentro de un bucle while que finaliza al elegir
# la opción 8 del menú donde la bandera "finalizado" toma el valor "True" 
while  not finalizado:

    #Muestra el menú en pantalla
    print()
    print("*** Biblioteca ***")
    for opcion in biblioteca_menu:
        print(opcion)
    print()

    #Solicita elegir una opción y valida que la misma sea un dígito 
    # y que se encuentre dentro de los valores de las opciones del menú
    # La funcion utilizada no sale del while hasta que la opción elegida sea correcta
    opcion_elegida = utils.verificar_opcion_menu(input("Seleccione una opción del menú: "))
    print()

    #Utiliza una estructura match-case de acuerdo a la opción ingresada
    match opcion_elegida:

        case "1": #Ingresar títulos (multiples)
            #permite cargar varios libros de una sola vez, con su cantidad inicial de ejemplares.
            #El programa ofrece seguir ingresando títulos hasta elegir una opción distinta de "S" (S = Si)
            
            continuar_ingresando = True # "S = Si"

            while continuar_ingresando:
                
                #Solicita un título y verifica si este ya se encuentra en la lista 
                # o se ingresó un caracter vacío o si la longitud del mismo 
                # supera los 50 caracteres (decision arbitraria para evitar textos excesivamente largos)
                # La función No sale del while hasta que el texto sea correcto y no esté en el catálogo
                utils.agregar_en_lista(catalogo)
                continuar_ingresando=input("Desea agregar más títulos? (S = Si): ").upper().strip() == "S"

            print()
            
            #Imprime la lista modificada y actualiza el archivo
            utils.imprimir_lista(catalogo)
            utils.actualizar("catalogo.csv", catalogo)

        case "2": #Ingresar ejemplares
            # Sumar una cantidad de exemplares a un título existente. .

            #Verifica si hay títulos en la lista
            #Si no tiene datos, muestra un mensaje y vuelve al menú
            if utils.lista_vacia(catalogo):
                continue

            #Si la lista contiene títulos imprime el listado de libros existentes, 
            # precedidos por un número de orden
            utils.imprimir_lista(catalogo)

            #Luego solicita elegir una opción (el número de orden del título deseado)
            #Con una función valida que la opción ingresada sea un dígito
            # y esté dentro de los valores de números de orden del listado
            #La función no sale del while hasta que la opción sea correcta
            titulo_elegido=utils.verificar_opcion_ingresada(input("Ingrese el número del título deseado: "), catalogo)

            #La cantidad agregada más lo existente previamente no debe exceder las 50 unidades (arbitrario)
            #La variable máximo indicará cual es la cantidad que puede ingresar sin exeder el límite
            #Luego la función validar_cantidad verifica que no exceda este máximo
            maximo= 50-utils.extraer_cantidad(titulo_elegido, catalogo)

            #Solicita la cantidad de ejemplares a agregar y valida que sea un dígito y 
            # que no exeda de las 50 unidades máximo (arbitrario para evitar valores excesivamente
            # altos de cantidad de ejemplares)
            #La función no sale del while hasta que la cantidad sea correcta
            ejemplares_a_agregar= utils.validar_cantidad(input(f"Ingrese la cantidad de ejemplares a agregar para \
el título {catalogo[titulo_elegido]["TITULO"]}. (máximo {maximo} unidades): "), maximo)

            #Suma la cantidad ingresada a la cantidad de ejemplares existente para ese título
            catalogo[titulo_elegido]["CANTIDAD"]= str(int(catalogo[titulo_elegido]["CANTIDAD"]) + ejemplares_a_agregar)

            #Informa al usuario que se ha actualizado en la lista la cantidad de ejemplares para el título
            # seleccionado y muestra la cantidad actual disponible.
            print(f"Se ha actualizado la cantidad de ejemplares para el título {catalogo[titulo_elegido]["TITULO"]}")
            if int(catalogo[titulo_elegido]["CANTIDAD"]) > 1:
                print(f"Existen {catalogo[titulo_elegido]["CANTIDAD"]} unidades disponibles")
            else:
                print("Existe solo 1 unidad disponible") 
            print()

            #Imprime la lista modificada y actualiza el archivo
            utils.imprimir_lista(catalogo)
            utils.actualizar("catalogo.csv", catalogo)

        
        case "3": #Mostrar catálogo
            #listar todos los libros con su stock actual. 

            #Verifica si hay títulos en la lista
            #Si no tiene datos, muestra un mensaje y vuelve al menú
            if utils.lista_vacia(catalogo):
                continue

            #Si la lista contiene títulos imprime el listado de libros existentes, 
            # precedidos por un número de orden
            #Luego espera que el usuario accione una tecla para continuar y volver al menú
            utils.imprimir_lista(catalogo)
            input("Presiona una tecla para continuar...")

        
        case "4": #Consultar disponibilidad
            #buscar un TITULO y mostrar cuántos ejemplares hay disponibles. 
            
            #Verifica si hay titulos en la lista
            #Si no tiene datos, muestra un mensaje y vuelve al menú
            if utils.lista_vacia(catalogo):
                continue

            #Solicita un título y lo busca en el catálogo
            #Si no lo encuentra, informa al usuario que ese título no existe en el catálogo.
            #Si lo encuentra muestra cuantos ejemplares disponibles hay de ese título
            titulo_a_consultar= input("Ingrese el título del libro a consultar: ")
            indice = utils.buscar_indice_por_titulo(catalogo, titulo_a_consultar)

            if indice >= 0:

                cantidad = utils.extraer_cantidad(indice, catalogo)
                titulo = utils.extraer_titulo(indice, catalogo)
                print(f"Existen {cantidad} unidades disponibles para el título {titulo}")

            else:
                print("El título buscado no existe en el catálogo.")
            input("Presiona una tecla para continuar...")

        
        case "5": #Listar agotados
            #Muestra los títulos que tienen 0 ejemplares.

            #Verifica si hay titulos en la lista
            #Si no tiene datos, muestra un mensaje y vuelve al menú
            if utils.lista_vacia(catalogo):                
                continue

            #Si la lista tiene títulos agotados, los imprime. Si no tiene muestra un mensaje
            utils.imprimir_agotados(catalogo)
            input("Presiona una tecla para continuar...")

        
        case "6": #Agregar título
            #Alta de un libro individual con su cantidad inicial. 

            #Solicita un título y verifica si este ya se encuentra en la lista 
            # o se ingresó un caracter vacío o si la longitud del mismo 
            # no supera los 50 caracteres (decision arbitraria para evitar textos excesivamente largos)
            # La función no sale del while hasta que el texto sea correcto y no esté en el catálogo
            utils.agregar_en_lista(catalogo)

            #Imprime la lista modificada y actualiza el archivo
            utils.imprimir_lista(catalogo)
            utils.actualizar("catalogo.csv", catalogo)
            input("Presiona una tecla para continuar...")


        case "7": #Actualizar ejemplares (préstamo/devolución)
            #Permite modificar el stock de un título, para registrar préstamos o devoluciones. 
            # - Préstamo -> Disminuye en 1 la cantidad de ejemplares, si hay unidades suficientes. 
            # - Devolución -> Aumenta en 1 la cantidad de ejemplares del libro seleccionado.

            #Verifica si hay titulos en la lista
            #Si no tiene datos, muestra un mensaje y vuelve al menú
            if utils.lista_vacia(catalogo):
                continue
            
            #Si la lista títulos imprime el listado de libros existentes y su cantidad, 
            # precedidos por un número de orden
            utils.imprimir_lista(catalogo)

            #Luego solicita elegir una opción (el número de orden del título deseado)
            #Con una función valida que la opción ingresada sea un dígito
            #  y esté dentro de los valores de números de orden del listado
            #La función no sale del while hasta que la opción sea correcta
            titulo_elegido=utils.verificar_opcion_ingresada(input("Ingrese el número del título deseado: "), catalogo)

            #Solicita al usuario ingresar la acción a realizar (P=Préstamo / D=Devolución)
            #Con un bucle while se valida que la opción ingresada sea "P" o "D" (mayúscula o minúscula)
            #No sale del while hasta que la opción sea correcta
            accion = input("Ingrese la acción deseada (P=Préstamo / D=Devolución): ").upper().strip()
            while not (accion == "P" or accion == "D"):
                print("La opción ingresada no es correcta")
                accion = input("Ingrese la acción deseada (P=Préstamo / D=Devolución): ").upper().strip()

            #Si es "P" (préstamo)
            if accion.upper() == "P":
                #Informa que está intentando realizar un préstamo
                print(f"Intentando préstamo del título {catalogo[titulo_elegido]["TITULO"]}...")
                print()

                #Verifica que existan ejemplares de ese título para prestar
                if int(catalogo[titulo_elegido]["CANTIDAD"]) > 0:
                        
                    #Si hay ejemplares resta 1 e informa que el préstamo fue realizado con éxito
                    catalogo[titulo_elegido]["CANTIDAD"] = str(int(catalogo[titulo_elegido]["CANTIDAD"]) - 1)
                    print("Préstamo realizado con éxito")

                else:
                    #Si no hay ejemplares para prestar informa que la operación no es posible
                    #y vuelve al menú
                    print("El préstamo no es posible. El título se encuentra agotado.")
                    input("Presiona una tecla para continuar...")
                    continue 

            #Si es "D" (devolución)
            elif accion.upper() == "D":
                #Informa que está intentando realizar una devolución
                print(f"Intentando devolución del título {catalogo[titulo_elegido]["TITULO"]}...")
                print()

                #Suma 1 a la cantidad de ejemplares e informa que la devolución fue realizada con éxito
                catalogo[titulo_elegido]["CANTIDAD"] = str(int(catalogo[titulo_elegido]["CANTIDAD"]) + 1)
                print("Devolución realizada con éxito")
            print()
            input("Presiona una tecla para continuar...")
            print()

            #Imprime la lista modificada y actualiza el archivo
            utils.imprimir_lista(catalogo)
            utils.actualizar("catalogo.csv", catalogo)
            input("Presiona una tecla para continuar...")
                
        
        case "8": #Salir
            #Termina la ejecución del programa.

            #Asigna el valor True a la bandera "finalizado" y sale del bucle while
            # informa que está finalizando la ejecución del programa, 
            # actualiza el archivo al salir y muestra un mensaje de salida.
            finalizado= True
            print("Finalizando el programa...")
            utils.actualizar("catalogo.csv", catalogo)
            print("Hasta luego!!")
            print()

        
        case _:
            #Por defecto, si se ingresa una opción no válida vuelve al menú
            print("La opción ingresada no es correcta")
            print()
            continue


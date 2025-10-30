"""  Parcial 2 de Programación 1 - Rolando Nebreda - DNI 18.350.686  """

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


"""***************FUNCIONES DE MANEJO DE ARCHIVOS***************"""

#Crea un archivo con el nombre dado si no existe
def crear_archivo(archivo):
    import os
    if not os.path.exists(archivo):

        #Escribe en la primera línea los encabezados de columna
        with open(archivo, "w") as catalogo:            
            catalogo.write("TITULO,CANTIDAD\n")


#Agrega los elementos del archivo a una lista como dicionarios
def lineas_diccionario (archivo_a_leer,lista):
    with open(archivo_a_leer,"r") as archivo:

        lineas = archivo.readlines()
            
        for linea in lineas:
            partes = linea.strip().split(",")
            lista.append({"TITULO": partes[0],"CANTIDAD":partes[1]})


#Actualiza los elementos en el archivo desde una lista de diccionarios (sobreescribe)
def actualizar(archivo_a_actualizar, lista):

    with open(archivo_a_actualizar, "w") as archivo:

        for elemento in lista:
            archivo.write(f"{elemento["TITULO"]},{elemento["CANTIDAD"]}\n")

    print(f"El archivo {archivo_a_actualizar} se actualizó correctamente")
    print()



"""***************FUNCIONES DE VALIDACION DE DATOS***************"""

#Función que valida que la opción elegida del menú sea un dígito 
# y que se encuentre dentro de los valores de las opciones del menú
# no sale del while hasta que la opción elegida sea correcta
def verificar_opcion_menu(opcion_elegida):
    while not (opcion_elegida.isdigit()) or not (int(opcion_elegida) in range(1, 9) ):
        print("La opción ingresada no es correcta")
        opcion_elegida = input("Seleccione una opción del menú: ")
        print()
    return opcion_elegida


#Función que valida que el título ingresado por el usuario 
# no se encuentre en la lista, no sea vacío o espacio y que no exceda de 50 caracteres (máximo arbitrario)
# no sale del while hasta que el título ingresado sea correcto
#devuelve el título validado y en formato capital (primera letra en mayúscula)
def validar_titulo(lista,titulo):
    titulo.lower().strip()
    while buscar_por_titulo(lista, titulo) or titulo == "" or len(titulo)>50:
        print("El libro ya existe en el catálogo o ingresó un título no válido. Intente nuevamente.")
        print()
        titulo= input("Ingrese el título del libro (máximo 50 caracteres): ").lower().strip()
        print()
    return titulo.capitalize()


#Función que valida la cantidad ingresada como texto (str)
# sea numérica entera, mayor a cero y menor que 50 (máximo arbitrario)
# no sale del while hasta que la cantidad ingresada sea correcta
# El parámetro "maximo" indica la cantidad máxima de ejemplares que puede agregar
# sin pasarse de los 50 ejemplares luego de agregarlos.
#devuelve la cantidad como entero (int)
def validar_cantidad(cantidad, maximo):
    cantidad.split()
    while not (cantidad.isdigit()) or not (int(cantidad) in range(1, maximo+1)):
        print("La opción ingresada no es correcta")
        cantidad= input(f"Ingrese la cantidad de ejemplares a agregar (máximo {maximo} unidades): ")
    print()
    return int(cantidad)


#Función que valida que la opción elegida del listado de títulos sea un entero positivo 
# y que se encuentre dentro de los valores de las opciones del listado de títulos
# no sale del while hasta que la opción elegida sea correcta (devuelve la opción como entero)
def verificar_opcion_ingresada(opcion_elegida, catalogo):
        
        opcion_elegida.strip()

        while not (opcion_elegida.isdigit()) or not (int(opcion_elegida) in range(1, len(catalogo)) ):
            print("La opción ingresada no es correcta")
            opcion_elegida = input("Ingrese el número del título deseado: ")
            print()
        
        return int(opcion_elegida)



"""********************FUNCIONES DE LISTAS********************"""

#Busca un elemento en una lista de diccionarios por la clave "TITULO"
#Devuelve un booleano
def buscar_por_titulo(lista, titulo):

    for elemento in lista:

        #Si lo encuentra devuelve True
        if elemento["TITULO"].lower().strip() == titulo.lower().strip():
            return True
        
    #Si no lo encuentra devuelve False
    return False


#Agrega un elemento nuevo a la lista (sin actualizar en el archivo)
def agregar_en_lista(lista):
            
    titulo= validar_titulo(lista, input("Ingrese el título del libro (máximo 50 caracteres): "))
    cantidad= validar_cantidad(input("Ingrese la cantidad a agregar (máximo 50 unidades): "), 50)

    lista.append({"TITULO": titulo,"CANTIDAD": cantidad})
    print(f"Se ha agregado {titulo} a la lista")
    print()


#Imprime todos los elementos de la lista (título y cantidad) 
# agregando un número de orden igual a su índice
def imprimir_lista (catalogo):
    print("*** Títulos disponibles ***")

    for i in range(len(catalogo)):
        if i == 0:
            print("***TITULO*** ***CANTIDAD***")

        else:
            if i < 10:
                print(" ", end="")

            print(f"{i}. {catalogo[i]["TITULO"]}, {catalogo[i]["CANTIDAD"]}")
    print()


#Si la lista está vacía retorna True. Si tiene elemento retorna False
def lista_vacia(lista):

    if len(lista)<=1:
        print("No hay títulos en el catálogo. Ingrese el título al catálogo primero (Opción 1 del menú)")
        print()

    return len(lista) <= 1


#Verifica si existen títulos agotados en una lista de diccionarios por la clave "CANTIDAD" (Cantidad == 0)
def buscar_agotados(lista):

    for elemento in lista:

        #Si encuentra títulos con cantidad = 0 devuelve True
        if elemento["CANTIDAD"] == "0":
            return True
        
    #Si no lo encuentra devuelve False
    return False


#Imprime los títulos agotados de la lista
def imprimir_agotados(catalogo):

    #Primero verifica si existen títulos agotados. Si encuentra los imprime.
    if buscar_agotados(catalogo):

        print("*** Títulos agotados ***")

        for i in range(len(catalogo)):
            if i == 0:
                print("***TITULO*** ***CANTIDAD***")

            elif catalogo[i]["CANTIDAD"] == "0":
                if i < 10:
                    print(" ", end="")

                print(f"{i}. {catalogo[i]["TITULO"]}, {catalogo[i]["CANTIDAD"]}")
    else:

        #Si no encuentra muestra un mensaje
        print("No hay títulos agotados en el calálogo")
        
    print()



"""********************FUNCIONES DE DICCIONARIOS********************"""

#Retorna el valor de "CANTIDAD" de un diccionario de la lista accediendo por su índice
#Devuelve la cantidad como entero
def extraer_cantidad(posicion, catalogo):
    return int(catalogo[posicion]["CANTIDAD"])


#Retorna el valor de "TITULO" de un diccionario de la lista accediendo por su índice
def extraer_titulo (posicion, catalogo):
    return catalogo[posicion]["TITULO"]


#Busca un elemento en una lista de diccionarios por la clave "TITULO" 
# devuelve el índice del diccionario en la lista
def buscar_indice_por_titulo(lista, titulo):

    for elemento in lista:

        #Si lo encuentra devuelve el índice del elemento
        if elemento["TITULO"].lower().strip() == titulo.lower().strip():
            return lista.index(elemento)
        
    #Si no lo encuentra devuelve -1
    return -1



"""********************PROGRAMA PRINCIPAL********************"""

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
crear_archivo("catalogo.csv")

#lee el contenido del archivo y lo carga en la lista como diccionarios
lineas_diccionario ("catalogo.csv", catalogo)

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
    opcion_elegida = verificar_opcion_menu(input("Seleccione una opción del menú: "))
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
                agregar_en_lista(catalogo)
                continuar_ingresando=input("Desea agregar más títulos? (S = Si): ").upper().strip() == "S"

            print()
            
            #Imprime la lista modificada y actualiza el archivo
            imprimir_lista(catalogo)
            actualizar("catalogo.csv", catalogo)
            input("Presiona una tecla para continuar...")
            print()


        case "2": #Ingresar ejemplares
            # Sumar una cantidad de exemplares a un título existente. .

            #Verifica si hay títulos en la lista
            #Si no tiene datos, muestra un mensaje y vuelve al menú
            if lista_vacia(catalogo):
                continue

            #Si la lista contiene títulos imprime el listado de libros existentes, 
            # precedidos por un número de orden
            imprimir_lista(catalogo)

            #Luego solicita elegir una opción (el número de orden del título deseado)
            #Con una función valida que la opción ingresada sea un dígito
            # y esté dentro de los valores de números de orden del listado
            #La función no sale del while hasta que la opción sea correcta
            titulo_elegido=verificar_opcion_ingresada(input("Ingrese el número del título deseado: "), catalogo)

            #La cantidad agregada más lo existente previamente no debe exceder las 50 unidades (arbitrario)
            #La variable máximo indicará cual es la cantidad que puede ingresar sin exeder el límite
            #Luego la función validar_cantidad verifica que no exceda este máximo
            maximo= 50-extraer_cantidad(titulo_elegido, catalogo)

            #Si maximo == 0 (ya posee 50 ejemplares), muestra un mensaje y vuelve al menú sin agregar ejemplares.
            if maximo == 0:
                print(f"No es posible agregar ejemplares. El título {catalogo[titulo_elegido]["TITULO"]} ya \
posee el máximo de 50 unidades")
                input("Presiona una tecla para continuar...")
                print()
                continue

            #Solicita la cantidad de ejemplares a agregar y valida que sea un dígito y 
            # que no exeda de las 50 unidades máximo (arbitrario para evitar valores excesivamente
            # altos de cantidad de ejemplares)
            #La función no sale del while hasta que la cantidad sea correcta
            ejemplares_a_agregar= validar_cantidad(input(f"Ingrese la cantidad de ejemplares a agregar para \
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

            #Actualiza el archivo
            actualizar("catalogo.csv", catalogo)
            input("Presiona una tecla para continuar...")
            print()

        
        case "3": #Mostrar catálogo
            #listar todos los libros con su stock actual. 

            #Verifica si hay títulos en la lista
            #Si no tiene datos, muestra un mensaje y vuelve al menú
            if lista_vacia(catalogo):
                continue

            #Si la lista contiene títulos imprime el listado de libros existentes, 
            # precedidos por un número de orden
            #Luego espera que el usuario accione una tecla para continuar y volver al menú
            imprimir_lista(catalogo)
            input("Presiona una tecla para continuar...")


        
        case "4": #Consultar disponibilidad
            #buscar un TITULO y mostrar cuántos ejemplares hay disponibles. 
            
            #Verifica si hay titulos en la lista
            #Si no tiene datos, muestra un mensaje y vuelve al menú
            if lista_vacia(catalogo):
                continue

            #Solicita un título y lo busca en el catálogo
            #Si no lo encuentra, informa al usuario que ese título no existe en el catálogo.
            #Si lo encuentra muestra cuantos ejemplares disponibles hay de ese título
            titulo_a_consultar= input("Ingrese el título del libro a consultar: ")
            indice = buscar_indice_por_titulo(catalogo, titulo_a_consultar)

            if indice >= 0:

                cantidad = extraer_cantidad(indice, catalogo)
                titulo = extraer_titulo(indice, catalogo)
                print(f"Existen {cantidad} unidades disponibles para el título {titulo}")

            else:
                print("El título buscado no existe en el catálogo.")
            input("Presiona una tecla para continuar...")


        
        case "5": #Listar agotados
            #Muestra los títulos que tienen 0 ejemplares.

            #Verifica si hay titulos en la lista
            #Si no tiene datos, muestra un mensaje y vuelve al menú
            if lista_vacia(catalogo):                
                continue

            #Si la lista tiene títulos agotados, los imprime. Si no tiene muestra un mensaje
            imprimir_agotados(catalogo)
            input("Presiona una tecla para continuar...")


        
        case "6": #Agregar título
            #Alta de un libro individual con su cantidad inicial. 

            #Solicita un título y verifica si este ya se encuentra en la lista 
            # o se ingresó un caracter vacío o si la longitud del mismo 
            # no supera los 50 caracteres (decision arbitraria para evitar textos excesivamente largos)
            # La función no sale del while hasta que el texto sea correcto y no esté en el catálogo
            agregar_en_lista(catalogo)

            #Imprime la lista modificada y actualiza el archivo
            imprimir_lista(catalogo)
            actualizar("catalogo.csv", catalogo)
            input("Presiona una tecla para continuar...")



        case "7": #Actualizar ejemplares (préstamo/devolución)
            #Permite modificar el stock de un título, para registrar préstamos o devoluciones. 
            # - Préstamo -> Disminuye en 1 la cantidad de ejemplares, si hay unidades suficientes. 
            # - Devolución -> Aumenta en 1 la cantidad de ejemplares del libro seleccionado.

            #Verifica si hay titulos en la lista
            #Si no tiene datos, muestra un mensaje y vuelve al menú
            if lista_vacia(catalogo):
                continue
            
            #Si la lista títulos imprime el listado de libros existentes y su cantidad, 
            # precedidos por un número de orden
            imprimir_lista(catalogo)

            #Luego solicita elegir una opción (el número de orden del título deseado)
            #Con una función valida que la opción ingresada sea un dígito
            #  y esté dentro de los valores de números de orden del listado
            #La función no sale del while hasta que la opción sea correcta
            titulo_elegido=verificar_opcion_ingresada(input("Ingrese el número del título deseado: "), catalogo)

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
            imprimir_lista(catalogo)
            actualizar("catalogo.csv", catalogo)
            input("Presiona una tecla para continuar...")

                
        
        case "8": #Salir
            #Termina la ejecución del programa.

            #Asigna el valor True a la bandera "finalizado" y sale del bucle while
            # informa que está finalizando la ejecución del programa, 
            # actualiza el archivo al salir y muestra un mensaje de salida.
            finalizado= True
            print("Finalizando el programa...")
            actualizar("catalogo.csv", catalogo)
            print("Hasta luego!!")
            print()

        
        case _:
            #Por defecto, si se ingresa una opción no válida vuelve al menú
            print("La opción ingresada no es correcta")
            print()
            continue


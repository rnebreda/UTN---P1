""" Enunciado:
La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las
copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que
utilice listas paralelas (una para titulos[] y otra para ejemplares[]). Cada título debe estar
vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas.
Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario
elija salir.
    
    1. Ingresar títulos → Para agregar los títulos iniciales de los libros, el usuario indica la
    cantidad inicial.
    2. Ingresar ejemplares → Para agregar una cantidad de copias para cada título.
    3. Mostrar catálogo → Muestra todos los libros y su stock actual.
    4. Consultar disponibilidad → Busca un título específico y muestra cuántos ejemplares
    hay.
    5. Listar agotados → Muestra los títulos que tienen 0 ejemplares.
    6. Agregar título → Permite añadir un nuevo libro y sus ejemplares disponibles al
    catálogo, respetando la sincronía de los índices en las listas.
    7. Actualizar ejemplares (préstamo/devolución) → Permite modificar el stock de un
    libro, elegido por el usuario, para registrar préstamos o devoluciones.
    - Préstamo -> Disminuye en 1 la cantidad de ejemplares del libro seleccionado,
    si hay unidades suficientes.
    - Devolución -> Aumenta en 1 la cantidad de ejemplares del libro seleccionado.
    8. Salir → Termina la ejecución del programa. """

# Menú de opciones
biblioteca_menu= ["1. Ingresar títulos (sin ejemplares)", 
                  "2. Ingresar ejemplares", 
                  "3. Mostrar catálogo", 
                  "4. Consultar disponibilidad",
                  "5. Listar agotados",
                  "6. Agregar título (con ejemplares)",
                  "7. Actualizar ejemplares (préstamo/devolución)",
                  "8. Salir"]

# listas paralelas
titulos=[]
ejemplares=[]

#bandera para finalización del programa
finalizado= False

#Todo el programa se encuentra dentro de un bucle while que finaliza al elegir
#  la opción 8 del menú donde la bandera "finalizado" toma el valor "True" 
while  not finalizado:

    #Muestra el menú en pantalla
    print()
    print("*** Biblioteca ***")
    for opcion in biblioteca_menu:
        print(opcion)
    print()

    #Solicita elegir una opción y valida que la misma sea un dígito 
    # y que se encuentre dentro de los valores de las opciones del menú
    # no sale del while hasta que la opción elegida sea correcta
    opcion_elegida = input("Seleccione una opción del menú: ")
    while not (opcion_elegida.isdigit()) or not (int(opcion_elegida) in range(1, 9) ):
        print("La opción ingresada no es correcta")
        opcion_elegida = input("Seleccione una opción del menú: ")
    print()

    #Utiliza una estructura match-case de acuerdo a la opción ingresada (pasada a tipo int)
    match int(opcion_elegida):

        case 1:
            # Ingresar títulos → Para agregar los títulos iniciales de los libros,
            # cantidad inicial 0 ejemplares.

            #Solicita un título y verifica si este ya se encuentra en la lista 
            # o se ingresó un caracter vacío o si la longitud del mismo 
            # no supera los 50 caracteres (decision arbitraria para evitar textos excesivamente largos)
            # No sale del while hasta que el texto es correcto y no está en el catálogo
            titulo= input("Ingrese el título del libro (máximo 50 caracteres): ")
            while titulo in titulos or titulo == "" or len(titulo)>50:
                print("El libro ya existe en el catálogo o ingresó un título no válido. Intente nuevamente.")
                print()
                titulo= input("Ingrese el título del libro (máximo 50 caracteres): ")
            print()

            #Una vez validado se agrega al catálogo (lista titulo) y usando la función index, 
            #tambien se agrega en la lista ejemplares la cantidad inicial de ejemplares 
            # en la misma posición (valor inicial de cantidad de ejemplares = 0)
            titulos.append(titulo)
            posicion= titulos.index(titulo)
            ejemplares.insert(posicion,0)
            print("El título ha sido agregado al catálogo")


        case 2:
            # Ingresar ejemplares → Para agregar una cantidad de copias para cada título.

            #Verifica si hay ejemplares en la lista titulos
            if len(titulos)==0:
                print("No hay títulos en el catálogo. Ingrese el título primero (Opción 1 del menú)")
                print()
                continue
            else:
                #Si la lista títulos no está vacía imprime el listado de libros existentes, 
                # precedidos por un número de orden
                print("*** Títulos disponibles ***")
                for i in range(1, len(titulos)+1):
                    print(f"{i}. {titulos[i-1]}")
                print()

                #Luego solicita elegir una opción (el número de orden del título deseado)
                #Con un bucle while se valida que la opción ingresada sea un dígito
                #  y dentro de los valores de números de orden del listado
                #No sale del while hasta que la opción es correcta
                titulo_elegido=input("Ingrese el número del título deseado: ")
                while not (titulo_elegido.isdigit()) or not (int(titulo_elegido) in range(1, len(titulos)+1) ):
                    print("La opción ingresada no es correcta")
                    titulo_elegido = input("Ingrese el número del título deseado: ")
                print()

                #Asigna a la variable posición el valor ingresado restando 1, 
                # para que se corresponda con el índice del titulo en la lista titulos
                posicion= int(titulo_elegido) - 1

                #Solicita la cantidad de ejemplares a agregar y valida que sea un dígito y 
                # que no exeda de las 50 unidades (arbitrario para evitar valores excesivamente
                # altos de cantidad de ejemplares)
                #No sale del while hasta que la cantidad es correcta
                ejemplares_a_agregar= input(f"Ingrese la cantidad de ejemplares a agregar para \
el título {titulos[posicion]}. (máximo 50 unidades): ")
                while not (ejemplares_a_agregar.isdigit()) or not (int(ejemplares_a_agregar) in range(1, 51)):
                    print("La opción ingresada no es correcta")
                    ejemplares_a_agregar= input(f"Ingrese la cantidad de ejemplares a agregar para \
el título {titulos[posicion]}. (máximo 50 unidades): ")
                    
                #Suma la cantidad ingresada a la cantidad de ejemplares existente para ese título
                ejemplares[posicion] += int(ejemplares_a_agregar)
                
                #Informa al usuario que se ha actualizado la cantidad de ejemplares para el título
                # seleccionado y muestra la cantidad actual disponible.
                print(f"Se ha actualizado la cantidad de ejemplares para el título {titulos[posicion]}")
                if ejemplares[posicion] > 1:
                    print(f"Existen {ejemplares[posicion]} unidades disponibles")
                else:
                    print("Existe solo 1 unidad disponible")   

        
        case 3:
            # Mostrar catálogo → Muestra todos los libros y su stock actual.

            #Verifica si hay ejemplares en la lista titulos
            if len(titulos)==0:
                print("No hay títulos en el catálogo.")
                print()
                continue
            else:
                #Si la lista títulos no está vacía imprime el listado de libros existentes, 
                # más la cantidad de ejemplares, separado por una sucesión de guiones dependentes
                # de la longitud del nombre del título (arbitrario para visualizar las cantidades encolumnadas)
                print("******************* Títulos disponibles *******************")
                for i in range(1, len(titulos)+1):
                    print(f"{i}. {titulos[i-1]}", end=" ")

                    for j in range(len(titulos[i-1]), 52):
                        #Al haber definido largo máximo del título en 50 caracteres
                        # siempre va a ser la longitud del título 
                        # menor a 52 y existir al menos 1 guion
                        print("_", end="")

                    if ejemplares[i-1] < 10:
                        #si son menos de 10 ejemplares agrega un espacio adelante 
                        # para que visualmente queden los ejemplares encolumnados
                        print(" ", end="")

                    print(f" {ejemplares[i-1]}")
                print()

        
        case 4:
            #Consultar disponibilidad → Busca un título específico y muestra cuántos ejemplares hay.

            #Verifica si hay ejemplares en la lista titulos
            if len(titulos)==0:
                print("No hay títulos en el catálogo.")
                print()
                continue

            #Solicita un título y lo busca dentro de titulos
            #Si lo encuentra, toma el índice del título en la lista
            #  y con el mismo muestra la cantidad de ejemplares de igual índice en la lista ejemplares
            #Si no lo encuentra, informa al usuario que ese título no existe en el catálogo.
            titulo_a_consultar= input("Ingrese el título del libro a consultar: ")
            if (titulo_a_consultar in titulos):
                posicion= titulos.index(titulo_a_consultar)
                print(f"Existen {ejemplares[posicion]} unidades disponibles para el título {titulos[posicion]}")
            else:
                print("El libro no existe en el catálogo.")
            print()

        
        case 5:
            #Listar agotados → Muestra los títulos que tienen 0 ejemplares.

            #Verifica si hay ejemplares en la lista titulos
            if len(titulos)==0:
                print("No hay títulos en el catálogo.")
                print()
                continue
            else:
                #Si la lista no está vacía, recorre la misma y muestra solo los que tienen valor = 0
                #  en la lista ejemplares utilizando la misma posición en ambas listas.
                print("*** Títulos agotados ***")
                for i in range(len(titulos)):
                    if ejemplares[i] == 0:
                        print(f"{titulos[i]}")
                print()

        
        case 6:
            #Agregar título → Permite añadir un nuevo libro y sus ejemplares disponibles al 
            # catálogo, respetando la sincronía de los índices en las listas.

            #Solicita un título y verifica si este ya se encuentra en la lista 
            # o se ingresó un caracter vacío o si la longitud del mismo 
            # no supera los 50 caracteres (decision arbitraria para evitar textos excesivamente largos)
            # No sale del while hasta que el texto es correcto y no está en el catálogo
            titulo= input("Ingrese el título del libro (máximo 50 caracteres): ")
            while titulo in titulos or titulo == "" or len(titulo)>50:
                print("El libro ya existe en el catálogo o ingresó un título no válido. Intente nuevamente.")
                print()
                titulo= input("Ingrese el título del libro (máximo 50 caracteres): ")
            print()

            #Solicita la cantidad de ejemplares a agregar y valida que sea un dígito y 
            # que no exeda de las 50 unidades (arbitrario para evitar valores excesivamente
            # altos de cantidad de ejemplares)
            #No sale del while hasta que la cantidad es correcta
            ejemplares_a_agregar= input(f"Ingrese la cantidad de ejemplares a agregar para \
el título {titulo}. (máximo 50 unidades): ")
            while not (ejemplares_a_agregar.isdigit()) or not (int(ejemplares_a_agregar) in range(1, 51)):
                print("La opción ingresada no es correcta")
                ejemplares_a_agregar= input(f"Ingrese la cantidad de ejemplares a agregar para \
el título {titulo}. (máximo 50 unidades): ")
            
            #Finalmente agrega el título a la lista títulos y usando el mismo índice, 
            # agrega la cantidad de ejemplares (como entero)
            titulos.append(titulo)
            posicion= titulos.index(titulo)
            ejemplares.insert(posicion,int(ejemplares_a_agregar))
            print("El título ha sido agregado al catálogo")

        
        case 7:
            # Actualizar ejemplares (préstamo/devolución) → Permite modificar el stock de un 
            # libro, elegido por el usuario, para registrar préstamos o devoluciones. 
            # - Préstamo -> Disminuye en 1 la cantidad de ejemplares del libro seleccionado, 
            #               si hay unidades suficientes. 
            # - Devolución -> Aumenta en 1 la cantidad de ejemplares del libro seleccionado.

            #Verifica si hay ejemplares en la lista titulos
            if len(titulos)==0:
                print("No hay títulos en el catálogo")
                print()
                continue
            else:
                #Si la lista títulos no está vacía imprime el listado de libros existentes, 
                # precedidos por un número de orden
                print("*** Títulos disponibles ***")
                for i in range(1, len(titulos)+1):
                    print(f"{i}. {titulos[i-1]}")
                print()

                #Luego solicita elegir una opción (el número de orden del título deseado)
                #Con un bucle while se valida que la opción ingresada sea un dígito
                #  y dentro de los valores de números de orden del listado
                #No sale del while hasta que la opción es correcta
                titulo_elegido=input("Ingrese el número del título deseado: ")
                while not (titulo_elegido.isdigit()) or not (int(titulo_elegido) in range(1, len(titulos)+1) ):
                    print("La opción ingresada no es correcta")
                    titulo_elegido = input("Ingrese el número del título deseado: ")
                print()

                #Asigna a la variable posición el valor ingresado restando 1, 
                # para que se corresponda con el índice del titulo en la lista titulos
                posicion= int(titulo_elegido) - 1

                #Solicita al usuario ingresar la acción a realizar (P=Préstamo / D=Devolución)
                #Con un bucle while se valida que la opción ingresada sea "P" o "D" (mayúscula o minúscula)
                #No sale del while hasta que la opción es correcta
                accion = input("Ingrese la acción deseada (P=Préstamo / D=Devolución): ")
                while not (accion.upper() == "P" or accion.upper() == "D"):
                    print("La opción ingresada no es correcta")
                    accion = input("Ingrese la acción deseada (P=Préstamo / D=Devolución): ")

                #Si es "P" (préstamo)
                if accion.upper() == "P":
                    #Informa que está intentando realizar un préstamo
                    print(f"Intentando préstamo del título {titulos[posicion]}...")
                    #Verifica que existan ejemplares de ese título para prestar
                    if ejemplares[posicion]>0:
                        #Si hay ejemplares resta 1 e informa que el préstamo fue realizado
                        ejemplares[posicion] -= 1
                        print("Préstamo realizado con éxito")
                    else:
                        #Si no hay ejemplares para prestar informa que la operación no es posible
                        print("El préstamo no es posible. El título se encuentra agotado.")

                #Si es "D" (devolución)
                elif accion.upper() == "D":
                    #Informa que está intentando realizar una devolución
                    print(f"Intentando devolución del título {titulos[posicion]}...")
                    #Suma 1 a la cantidad de ejemplares e informa que la devolución fue realizada
                    ejemplares[posicion] += 1
                    print("Devolución realizada con éxito")
                print()
                
        
        case 8:
            #Salir → Termina la ejecución del programa.

            #asigna el valor True a la bandera "finalizado" y sale del bucle while
            #  finalizando la ejecución del programa, y mostrando un mensaje de salida.
            finalizado= True
            print("Finalizando el programa...")
            print("Hasta luego!!")
            print()

        
        case _:
            #Por defecto, si se ingresa una opción no válida del menú
            #mostrará un mensaje y volverá al menú
            #Esto no debería suceder de acuerdo a la validación de la opción elegida, 
            # antes de ingresar a la estructura match-case
            print("La opción ingresada no es correcta")
            print()
            continue


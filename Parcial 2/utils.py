"""  Biblioteca de funciones para Parcial 2 de Programación 1 - Rolando Nebreda - DNI 18.350.686  """

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
#devuelve la cantidad como entero (int)
def validar_cantidad(cantidad, previos):
    cantidad.split()
    while not (cantidad.isdigit()) or not (int(cantidad) in range(1, previos+1)):
        print("La opción ingresada no es correcta")
        cantidad= input(f"Ingrese la cantidad de ejemplares a agregar (máximo {previos} unidades): ")
    print()
    return int(cantidad)


#Función que valida que la opción elegida del listado de títulos sea un entero positivo 
# y que se encuentre dentro de los valores de las opciones del listado de títulos
# no sale del while hasta que la opción elegida sea correcta
def verificar_opcion_ingresada(opcion_elegida, catalogo):
        
        opcion_elegida.strip()

        while not (opcion_elegida.isdigit()) or not (int(opcion_elegida) in range(1, len(catalogo)) ):
            print("La opción ingresada no es correcta")
            opcion_elegida = input("Ingrese el número del título deseado: ")
            print()
        
        return int(opcion_elegida)


"""********************FUNCIONES DE LISTAS********************"""

#Busca un elemento en una lista de diccionarios por la clave "TITULO"
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

"""*************************FIN*************************"""
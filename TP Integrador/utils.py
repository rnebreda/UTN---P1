"""  Biblioteca de funciones para Trabajo Práctico Integrador de Programación 1  """

"""***************FUNCIONES DE MANEJO DE ARCHIVOS***************"""

#Crea un archivo con el nombre dado si no existe
def crear_archivo(archivo):
    import os
    if not os.path.exists(archivo):

        #Escribe en la primera línea los encabezados de columna
        with open(archivo, "w") as paises:            
            paises.write("NOMBRE,POBLACION,SUPERFICIE,CONTINENTE\n")


""" #Agrega los elementos del archivo a una lista como dicionarios de paises
def paises_diccionarios (archivo_a_leer,lista):
    with open(archivo_a_leer,"r") as archivo:

        lineas = archivo.readlines()
            
        for linea in lineas:
            partes = linea.strip().split(",")
            lista.append({"NOMBRE": partes[0],"POBLACION":partes[1]},{"SUPERFICIE": partes[2],"CONTINENTE":partes[3]})
 """

#Agrega los elementos del archivo a una lista como dicionarios de paises
def paises_diccionarios (archivo_a_leer,lista):
    #importa múdulo CSV para utilizar función DictRider
    import csv
    with open(archivo_a_leer,"r") as archivo:

        #Esta función interpreta la primera fila como los nombres de las claves de los diccionarios.
        # y genera un diccionario por cada renglón del archivo csv. 
        lector = csv.DictReader(archivo)      

        #Agrega cada diccionario en lector a la lista pasada como parámetro   
        for diccionario in lector:            
            lista.append(diccionario)


""" #Actualiza los elementos en el archivo desde una lista de diccionarios (sobreescribe)
def actualizar(archivo_a_actualizar, lista):

    with open(archivo_a_actualizar, "w") as paises:

        paises.write("NOMBRE,POBLACION,SUPERFICIE,CONTINENTE\n")

        for pais in lista:
            paises.write(f"{pais["NOMBRE"]},{pais["POBLACION"]},{pais["SUPERFICIE"]},{pais["CONTINENTE"]}\n")

    print(f"El archivo {archivo_a_actualizar} se actualizó correctamente")
    print() """


#Actualiza los elementos en el archivo desde una lista de diccionarios (sobreescribe)
def actualizar(archivo_a_actualizar, lista):
    #importa múdulo CSV para utilizar función DictWriter
    import csv

    #El parámetro newline="", indica que el módulo csv se hará cargo de la creación
    #  de nuevas lineas en el archivo
    with open(archivo_a_actualizar, "w", newline= "") as paises:

        #Se genera una lista con los nombres de los campos en el encabezado de columnas del archivo
        encabezado=["NOMBRE","POBLACION","SUPERFICIE","CONTINENTE"]

        #Esta función vuelca al archivo, los diccionarios de una lista de diccionarios
        #El parámetro fieldnames, indica que los nombres de los campos lo tomará de la lista "encabezado"
        escritor = csv.DictWriter(paises, fieldnames=encabezado)
        #Escribe la fila con el encabezado en el archivo
        escritor.writeheader()
        #Luego escribe cada diccionario de la lista de diccionarios en el archivo en una línea diferente
        escritor.writerows(lista)

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


#Función que valida que el nombre del pais ingresado por el usuario 
# no se encuentre en la lista, no sea vacío o espacio y que no exceda de 50 caracteres (máximo arbitrario)
# no sale del while hasta que el nombre del pais ingresado sea correcto
#devuelve el nombre validado y en formato capital (primera letra en mayúscula)
def validar_nombre(lista,nombre):
    nombre.lower().strip()
    while buscar_por_nombre_pais(lista, nombre) or nombre == "" or len(nombre)>50:
        print("El país ya existe en el listado o ingresó un nombre de país no válido. Intente nuevamente.")
        print()
        titulo= input("Ingrese el nombre del país (máximo 50 caracteres): ").lower().strip()
        print()
    return titulo.capitalize()


#Función que valida la cantidad ingresada como texto (str)
# sea numérica entera, mayor a cero
# no sale del while hasta que la cantidad ingresada sea correcta
# devuelve la cantidad como entero (int)
# se utiliza para validar el ingreso de población o el de superficie de acuerdo al argumento "tipo"
def validar_cantidad(cantidad, tipo):
    cantidad.split()
    while not (cantidad.isdigit()):
        if tipo == "poblacion":
            print("Ingrese la población (cantiad entera): ")

        elif tipo == "superficie":
            print("Ingrese la superficie (en km2): ")
    print()
    return int(cantidad)


#Función que permite elegir un continente de una lista de continentes
# valida que la opcion elegida sea numérica entera y dentro del rango de opciones
# no sale del while hasta que la opcion ingresada sea correcta
# devuelve el nombre del continente elegido como string 
# al elegir el continente de una lista el dato es validado.
def validar_continente():

    #Lista de continentes
    continentes= ["África", "América", "Asia", "Europa", "Oceanía"]
    
    #Muestra el menú de continentes en pantalla agregando un número de orden
    print()
    print("*** CONTINENTES ***")
    for i in range(len(continentes)):
        print(f"   {i+1}. {continentes[i]}")
    print()
    opcion_elegida = input("Seleccione el número de un continente del listado: ")
    print()

    #valida que la opción ingresada sea un número y esté dentro del rango de opciones del menu
    while not (opcion_elegida.isdigit()) or not (int(opcion_elegida) in range(len(continentes)+1) ):
        print("La opción ingresada no es correcta")
        opcion_elegida = input("Seleccione el número de un continente del listado: ")
        print()

    #Devuelve el continente elegido (string)
    return continentes[int(opcion_elegida)-1]


#Función que valida que la opción elegida del listado de paises sea un entero positivo 
# y que se encuentre dentro de los valores de las opciones del listado de paises
# no sale del while hasta que la opción elegida sea correcta
def verificar_opcion_ingresada(opcion_elegida, paises):
        
        opcion_elegida.strip()

        while not (opcion_elegida.isdigit()) or not (int(opcion_elegida) in range(1, len(paises)) ):
            print("La opción ingresada no es correcta")
            opcion_elegida = input("Ingrese el nombre del pais deseado: ")
            print()
        
        return int(opcion_elegida)



"""********************FUNCIONES DE LISTAS********************"""

#Busca un elemento en una lista de diccionarios por la clave "TITULO"
def buscar_por_nombre_pais(lista, nombre):

    for pais in lista:

        #Si lo encuentra devuelve True
        if pais["NOMBRE"].lower().strip() == nombre.lower().strip():
            return True
        
    #Si no lo encuentra devuelve False
    return False


#Agrega un elemento nuevo a la lista (sin actualizar en el archivo)
def agregar_en_lista(lista):
            
    nombre= validar_nombre(lista, input("Ingrese el nombre del pais (máximo 50 caracteres): "))
    poblacion= validar_cantidad(input("Ingrese la población (cantiad entera): "),"poblacion")
    superficie= validar_cantidad(input("Ingrese la superficie (en km2): "), "superficie")
    continente= validar_continente()

    lista.append({"NOMBRE": nombre,"POBLACION": poblacion, "SUPERFICIE": superficie,"CONTINENTE": continente})
    print(f"Se ha agregado {nombre} a la lista")
    print()


#Imprime todos los paises de la lista
# agregando un número de orden igual a su índice
def imprimir_lista_paises (paises):

    encabezado=["NOMBRE","POBLACION","SUPERFICIE","CONTINENTE"]

    print("*** LISTADO DE PAISES ***")

    for i in range(len(paises)):
        if i == 0:
            print(" N°", end="")
            for j in range(len(encabezado)):
                print(f" ***{encabezado[j]}***", end= "")
            print()    

        else:
            if i < 10:
                print(" ", end="")

            print(f"{i}. {paises[i]["NOMBRE"]}, {paises[i]["POBLACION"]}, {paises[i]["SUPERFICIE"]}, {paises[i]["CONTINENTE"]}")
    print()


#Si la lista está vacía retorna True. Si tiene elemento retorna False
def lista_vacia(lista):

    if len(lista)<=1:
        print("No hay elementos en la lista de paises. Agregue el país a la lista primero (Opción 1 del menú)")
        print()

    return len(lista) <= 1



"""********************FUNCIONES DE DICCIONARIOS********************"""

#Retorna el valor de "NOMBRE" de un diccionario de la lista accediendo por su índice
def extraer_nombre(posicion, lista):
    return int(lista[posicion]["NOMBRE"])


#Retorna el valor de "POBLACION" de un diccionario de la lista accediendo por su índice
def extraer_poblacion(posicion, lista):
    return int(lista[posicion]["POBLACION"])


#Retorna el valor de "SUPERFICIE" de un diccionario de la lista accediendo por su índice
def extraer_superficie(posicion, lista):
    return int(lista[posicion]["SUPERFICIE"])


#Retorna el valor de "CONTINENTE" de un diccionario de la lista accediendo por su índice
def extraer_continente(posicion, lista):
    return int(lista[posicion]["CONTINENTE"])


#Busca un elemento en una lista de diccionarios por la clave "NOMBRE" 
# devuelve el índice del diccionario en la lista
def buscar_indice_por_nombre_pais(lista, nombre):

    for elemento in lista:

        #Si lo encuentra devuelve el índice del elemento
        if elemento["NOMBRE"].lower().strip() == nombre.lower().strip():
            return lista.index(elemento)
        
    #Si no lo encuentra devuelve -1
    return -1



"""**********FUNCIONES DE ORDENAMIENTO DE LISTA DE DICCIONARIOS**********"""

def ordenar_por_nombre_ascendente(lista):
    from operator import itemgetter

    # Usar itemgetter("NOMBRE") como la clave de ordenación
    nombre_ascendente = sorted(lista, key=itemgetter("NOMBRE"))

    return nombre_ascendente

def ordenar_por_nombre_descendente(lista):
    from operator import itemgetter

    # Usar itemgetter("NOMBRE") como la clave de ordenación
    nombre_descendente = sorted(lista, key=itemgetter("NOMBRE"), reverse=True)

    return nombre_descendente


def ordenar_por_poblacion_ascendente(lista):
    from operator import itemgetter

    # Usar itemgetter("POBLACION") como la clave de ordenación
    poblacion_ascendente = sorted(lista, key=itemgetter("POBLACION"))

    return poblacion_ascendente


def ordenar_por_poblacion_descendente(lista):
    from operator import itemgetter

    # Usar itemgetter("POBLACION") como la clave de ordenación
    poblacion_descendente = sorted(lista, key=itemgetter("POBLACION"), reverse=True)

    return poblacion_descendente

def ordenar_por_superficie_ascendente(lista):
    from operator import itemgetter

    # Usar itemgetter("POBLACION") como la clave de ordenación
    poblacion_ascendente = sorted(lista, key=itemgetter("SUPERFICIE"))

    return poblacion_ascendente


def ordenar_por_superficie_descendente(lista):
    from operator import itemgetter

    # Usar itemgetter("POBLACION") como la clave de ordenación
    superficie_descendente = sorted(lista, key=itemgetter("SUPERFICIE"), reverse=True)

    return superficie_descendente



"""*************************FALTAN*************************"""

#Funcion reporte_por_continente()

#Funcion reporte_por_poblacion()

#Funcion reporte_por_superficie()

#Funcion mayor_poblacion()

#Funcion menor_poblacion()

#Funcion calcular_promedio_poblacion()

#Funcion calcular_promedio_superficie()

#Función contar_paises_por_continente



"""*************************FIN*************************"""
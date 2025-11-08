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
    with open(archivo_a_leer,"r", encoding="utf-8-sig") as archivo:

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
    with open(archivo_a_actualizar, "w", newline= "", encoding="utf-8-sig") as paises:

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
    while buscar_por_nombre_pais(lista, nombre) or nombre == "" or len(nombre)>25:
        print("El país ya existe en el listado o ingresó un nombre de país no válido. Intente nuevamente.")
        print()
        nombre= input("Ingrese el nombre del país (máximo 25 caracteres): ").lower().strip()
    print()
    return nombre.capitalize()


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
    while not (opcion_elegida.isdigit()) or not (int(opcion_elegida) in range(1, len(continentes)+1) ):
        print("La opción ingresada no es correcta")
        opcion_elegida = input("Seleccione el número de un continente del listado: ")
        print()

    #Devuelve el continente elegido (string)
    return continentes[int(opcion_elegida)-1]

def validar_rango_poblacion():

    #Lista de rangos de población (6 rangos)
    rangos_poblacion= ["Mayor a 100 millones", "Entre 50 y 100 millones", "Entre 10 y 50 millones", "Entre 5 y 10 millones", "Entre 1 y 5 millones", "Menor a 1 millón"]
    
    #Muestra el menú de rangos de población en pantalla agregando un número de orden
    print()
    print("*** RANGOS DE POBLACION ***")
    for i in range(len(rangos_poblacion)):
        print(f"   {i+1}. {rangos_poblacion[i]}")
    print()
    opcion_elegida = input("Seleccione un rango de población del listado: ")
    print()

    #valida que la opción ingresada sea un número y esté dentro del rango de opciones del menu
    while not (opcion_elegida.isdigit()) or not (int(opcion_elegida) in range(1, len(rangos_poblacion)+1) ):
        print("La opción ingresada no es correcta")
        opcion_elegida = input("Seleccione el número de rango de población del listado: ")
        print()

    #Devuelve el número del rango de población elegido ( 1 a 6 como string)
    return opcion_elegida


def validar_rango_superficie():

    #Lista de rangos de superficie (6 rangos)
    rangos_superficie= ["Mayor a 5 millones", "Entre 1 y 5 millones", "Entre 500 mil y 1 millón", "Entre 100 y 500 mil", "Entre 50 y 100 mil", "Menor a 50 mil"]
    
    #Muestra el menú de rangos de superficie en pantalla agregando un número de orden
    print()
    print("*** RANGOS DE SUPURFICIE (en Km2) ***")
    for i in range(len(rangos_superficie)):
        print(f"   {i+1}. {rangos_superficie[i]}")
    print()
    opcion_elegida = input("Seleccione un rango de superficie del listado: ")
    print()

    #valida que la opción ingresada sea un número y esté dentro del rango de opciones del menu
    while not (opcion_elegida.isdigit()) or not (int(opcion_elegida) in range(1, len(rangos_superficie)+1) ):
        print("La opción ingresada no es correcta")
        opcion_elegida = input("Seleccione el número de rango de superficie del listado: ")
        print()

    #Devuelve el número del rango de superficie elegido ( 1 a 6 como string)
    return opcion_elegida


#Función que valida que la opción elegida del listado de paises sea un entero positivo 
# y que se encuentre dentro de los valores de las opciones del listado de paises
# no sale del while hasta que la opción elegida sea correcta
def verificar_opcion_ingresada(opcion_elegida, paises):
        
        opcion_elegida.strip()

        while not (opcion_elegida.isdigit()) or not (int(opcion_elegida) in range(1, len(paises)+1) ):
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
            
    nombre= validar_nombre(lista, input("Ingrese el nombre del pais (máximo 25 caracteres): "))
    poblacion= validar_cantidad(input("Ingrese la población (cantiad entera): "),"poblacion")
    superficie= validar_cantidad(input("Ingrese la superficie (en km2): "), "superficie")
    continente= validar_continente()

    lista.append({"NOMBRE": nombre,"POBLACION": poblacion, "SUPERFICIE": superficie,"CONTINENTE": continente})
    print(f"Se ha agregado {nombre} a la lista")
    print()


#Imprime todos los paises de la lista
# agregando un número de orden igual a su índice
def imprimir_lista_paises(paises):

    encabezado=["NOMBRE","POBLACION","SUPERFICIE","CONTINENTE"]

    print("*************** LISTADO DE PAISES ***************")
    print(" N°", end="")
    for j in range(len(encabezado)):
        print(f" ** {encabezado[j]}", end= "")
    print() 

    for i in range(len(paises)):

            if i < 10:
                print(" ", end="")

            print(f"{i+1}. {paises[i]["NOMBRE"]}, {paises[i]["POBLACION"]}, {paises[i]["SUPERFICIE"]}, {paises[i]["CONTINENTE"]}")
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
    return lista[posicion]["NOMBRE"]


#Retorna el valor de "POBLACION" de un diccionario de la lista accediendo por su índice
def extraer_poblacion(posicion, lista):
    return int(lista[posicion]["POBLACION"])


#Retorna el valor de "SUPERFICIE" de un diccionario de la lista accediendo por su índice
def extraer_superficie(posicion, lista):
    return int(lista[posicion]["SUPERFICIE"])


#Retorna el valor de "CONTINENTE" de un diccionario de la lista accediendo por su índice
def extraer_continente(posicion, lista):
    return lista[posicion]["CONTINENTE"]


#Busca un elemento en una lista de diccionarios por la clave "NOMBRE" 
# devuelve el índice del diccionario en la lista
def buscar_indice_por_nombre_pais(lista, nombre):

    for elemento in lista:

        #Si lo encuentra devuelve el índice del elemento
        if elemento["NOMBRE"].lower().strip() == nombre.lower().strip():
            return lista.index(elemento)
        
    #Si no lo encuentra devuelve -1
    return -1


#Busca un elemento en una lista de diccionarios por la clave "NOMBRE" con coincidencia parcial
# devuelve una lista con las coincidencias
def buscar_nombre_coincidencia_parcial(lista, nombre):

    coincidencias=[]

    encontrado=False

    for elemento in lista:

        #Si lo encuentra almacena el nombre y el índice del elemento
        if elemento["NOMBRE"].lower().strip().find(nombre.lower().strip())>= 0:
            coincidencias.append({"NOMBRE":elemento["NOMBRE"], "INDICE":lista.index(elemento)})
            encontrado=True

    if len(coincidencias)>1:

        print("*************** COINCIDENCIAS ENCONTRADAS ***************")

        for i in range(len(coincidencias)):  

            print(f"{i+1}. {coincidencias[i]["NOMBRE"]}")

        opcion_elegida=input("Elija una opción: ").strip()

        while not (opcion_elegida.isdigit()) or not (int(opcion_elegida) in range(1, len(coincidencias)+1)):
            print("La opción ingresada no es correcta")
            opcion_elegida = input("Elija una opción: ")
            print()
        
        return int(coincidencias[int(opcion_elegida)-1]["INDICE"])

    elif len(coincidencias)==1:
            return  int(coincidencias[0]["INDICE"])
    print()  
        
    #Si no lo encuentra devuelve -1
    if not encontrado:
        return -1


#Modifica un diccionario de la lista (sin actualizar en el archivo)
# Se pasa como parámetro la lista y el indice de la posición del diccionario en la lista
# permite cambiar la población y superficie
def modificar_pais(lista, posicion):

    modifica= input(f"Usted va a modificar el pais {lista[posicion]["NOMBRE"]}. Desea continuar? (S=si)").upper().strip() == "S"

    if modifica:

        print("La población actual es:", lista[posicion]["POBLACION"])
        modifica_poblacion= input("Desea modificar? (S=si)").upper().strip() == "S"
        if modifica_poblacion:
            poblacion= validar_cantidad(input("Ingrese la población (cantiad entera): "),"poblacion")
            lista[posicion]["POBLACION"]=poblacion

        print("La superficie actual es:", lista[posicion]["SUPERFICIE"])
        modifica_superficie= input("Desea modificar? (S=si)").upper().strip() == "S"
        if modifica_superficie:
            superficie= validar_cantidad(input("Ingrese la superficie (en km2): "), "superficie")
            lista[posicion]["SUPERFICIE"]=superficie

        print(f"Se ha modificado el país {lista[posicion]["NOMBRE"]}")
        print()



"""**********FUNCIONES DE ORDENAMIENTO DE LISTA DE DICCIONARIOS**********"""


#Funcion para ordenar una lista de diccionarios en forma ascendente 
# de acuerdo a uno de los campos (criterio) del diccionario.
# Utiliza un algoritmo de burbuja para ordenar
#Devuelve una lista ordenada sin modificar la original
def ordenar_ascendente(lista, criterio):

    #Crea una nueva lista vacía
    ordenada=[]

    #Se cargan todos los diccionarios de la lista original en la nueva lista
    for diccionario in lista:
        ordenada.append(diccionario)

        #Recorre la lista comparando los elementos de a pares n-1 veces (pasos), 
        # siendo n la cantidad de elementos de la lista
        for paso in range (len(ordenada) - 1):

            #Utiliza la bandera "intercambio" que indicará si en algun paso antes de n-1 
            # no se realizaron intercambios. Esto indicaría que la lista ya está ordenada 
            # y no es necesario continuar con los restantes pasos.
            intercambio =False

            #En cada paso es necesaria una comparación menos, 
            # por lo cual se resta el n° de paso en el siguiente ciclo for
            for i in range (len(ordenada) -1 - paso):

                #Realiza la comparación de cada elemento con el siguiente
                #En este caso como es un ordenamiento descendente utiliza el signo mayor (>)

                #Si es numérico ordena por número
                if ordenada[i][criterio].isdigit():

                    if int(ordenada[i][criterio]) > int(ordenada[i + 1][criterio]):

                    #Si el elemento es mayor que el siguiente, realiza el entercambio, 
                    # y cambia el valor de la bandera "intercambio" a True
                        ordenada[i], ordenada[i + 1] = ordenada[i + 1], ordenada[i]
                        intercambio=True
                
                #Si no es numérico ordena alfabéticamente
                else:

                    if (ordenada[i][criterio]) > (ordenada[i + 1][criterio]):

                    #Si el elemento es menor que el siguiente, realiza el entercambio, 
                    # y cambia el valor de la bandera "intercambio" a True
                        ordenada[i], ordenada[i + 1] = ordenada[i + 1], ordenada[i]
                        intercambio=True

            #Si no hubo intercambios en el paso, finaliza ya que la lista quedó ordenada
            if not intercambio:
                break
    
    #Devuelve la lista ordenada
    return ordenada


#Funcion para ordenar una lista de diccionarios en forma descendente 
# de acuerdo a uno de los campos (criterio) del diccionario.
# Utiliza un algoritmo de burbuja para ordenar
#Devuelve una lista ordenada sin modificar la original
def ordenar_descendente(lista, criterio):

    #Crea una nueva lista vacía
    ordenada=[]

    #Se cargan todos los diccionarios de la lista original en la nueva lista
    for diccionario in lista:
        ordenada.append(diccionario)

        #Recorre la lista comparando los elementos de a pares n-1 veces (pasos), 
        # siendo n la cantidad de elementos de la lista
        for paso in range (len(ordenada) - 1):

            #Utiliza la bandera "intercambio" que indicará si en algun paso antes de n-1 
            # no se realizaron intercambios. Esto indicaría que la lista ya está ordenada 
            # y no es necesario continuar con los restantes pasos.
            intercambio =False

            #En cada paso es necesaria una comparación menos, 
            # por lo cual se resta el n° de paso en el siguiente ciclo for
            for i in range (len(ordenada) -1 - paso):

                #Realiza la comparación de cada elemento con el siguiente
                #En este caso como es un ordenamiento descendente utiliza el signo menor (<)

                #Si es numérico ordena por número
                if ordenada[i][criterio].isdigit():

                    if int(ordenada[i][criterio]) < int(ordenada[i + 1][criterio]):

                    #Si el elemento es menor que el siguiente, realiza el entercambio, 
                    # y cambia el valor de la bandera "intercambio" a True
                        ordenada[i], ordenada[i + 1] = ordenada[i + 1], ordenada[i]
                        intercambio=True
                
                #Si no es numérico ordena alfabéticamente
                else:

                    if (ordenada[i][criterio]) < (ordenada[i + 1][criterio]):

                    #Si el elemento es menor que el siguiente, realiza el entercambio, 
                    # y cambia el valor de la bandera "intercambio" a True
                        ordenada[i], ordenada[i + 1] = ordenada[i + 1], ordenada[i]
                        intercambio=True

            #Si no hubo intercambios en el paso, finaliza ya que la lista quedó ordenada
            if not intercambio:
                break
    
    #Devuelve la lista ordenada
    return ordenada


def ordenamiento_lista (lista):

    #Lista de opciones de ordenamiento
    ordenamientos= ["Nombre ascendente", "Nombre descendente", "Población ascendente", "Población descendente", "Superficie Ascendente", "Superficie Descendente"]
    
    #Muestra el menú de opciones de ordenamiento en pantalla agregando un número de orden
    print()
    print("*** OPCIONES DE ORDENAMIENTO ***")
    for i in range(len(ordenamientos)):
        print(f"   {i+1}. {ordenamientos[i]}")
    print()
    opcion_elegida = input("Seleccione el número de ordenamiento deseado para el reporte: ")
    print()

    #valida que la opción ingresada sea un número y esté dentro del rango de opciones del menu
    while not (opcion_elegida.isdigit()) or not (int(opcion_elegida) in range(1, len(ordenamientos)+1) ):
        print("La opción ingresada no es correcta")
        opcion_elegida = input("Seleccione el número de ordenamiento deseado para el reporte: ")
        print()

    #Devuelve la lista ordenada
    match opcion_elegida:
        case "1":
            return ordenar_ascendente(lista, "NOMBRE")
        case "2":
            return ordenar_descendente(lista, "NOMBRE")
        case "3":
            return ordenar_ascendente(lista, "POBLACION")
        case "4":
            return ordenar_descendente(lista, "POBLACION")
        case "5":
            return ordenar_ascendente(lista, "SUPERFICIE")
        case "6":
            return ordenar_descendente(lista, "SUPERFICIE")
        case _:
            return lista



"""*****************FUNCIONES DE REPORTES*****************"""


def reporte_por_continente(lista):
    
    continente=validar_continente()

    lista_filtrada=[]

    for pais in lista:

        if pais["CONTINENTE"]== continente:
            lista_filtrada.append(pais)

    

    if len(lista_filtrada) > 0:

        lista_filtrada= ordenamiento_lista(lista_filtrada)

        print(f"Continente: {continente}")
        imprimir_lista_paises(lista_filtrada)

    else:
        print(f"No hay paises del continente {continente} en el listado")



def reporte_por_poblacion(lista):

    #Lista de rangos de población (6 rangos)
    rangos_poblacion= ["Mayor a 100 millones", "Entre 50 y 100 millones", "Entre 10 y 50 millones", "Entre 5 y 10 millones", "Entre 1 y 5 millones", "Menor a 1 millón"]
        
    rango=validar_rango_poblacion()
    
    lista_filtrada=[]
    
    minimo=0
    maximo=999999999999

    #Establece el mínimo y el máximo del rango para filtrar la lista
    match rango:
        case "1": #Mayor a 100 millones
            minimo=100000000
            maximo=999999999999
        case "2": #Entre 50 y 100 millones
            minimo=50000000
            maximo=100000000
        case "3": #Entre 10 y 50 millones
            minimo=10000000
            maximo=50000000
        case "4": #Entre 5 y 10 millones
            minimo=5000000
            maximo=10000000
        case "5": #Entre 1 y 5 millones
            minimo=1000000
            maximo=5000000
        case "6": #Menor a 1 millón
            minimo=0
            maximo=1000000
        case _: #Sin filtrar
            pass


    for pais in lista:

        if minimo <= int(pais["POBLACION"]) < maximo:
            lista_filtrada.append(pais)

    

    if len(lista_filtrada) > 0:

        lista_filtrada= ordenamiento_lista(lista_filtrada)

        print(f"Rango de población: {rangos_poblacion[int(rango)-1]}")
        imprimir_lista_paises(lista_filtrada)

    else:
        print(f"No hay paises del Rango de población {rangos_poblacion[int(rango)-1]} en el listado")



def reporte_por_superficie(lista):
    
    #Lista de rangos de superficie (6 rangos)
    rangos_superficie= ["Mayor a 5 millones", "Entre 1 y 5 millones", "Entre 500 mil y 1 millón", "Entre 100 y 500 mil", "Entre 50 y 100 mil", "Menor a 50 mil"]

    rango=validar_rango_superficie()
    
    lista_filtrada=[]
    
    minimo=0
    maximo=999999999999

    #Establece el mínimo y el máximo del rango para filtrar la lista
    match rango:
        case "1": #Mayor a 5 millones
            minimo=5000000
            maximo=999999999999
        case "2": #Entre 1 y 5 millones
            minimo=1000000
            maximo=5000000
        case "3": #Entre 500 mil y 1 millón
            minimo=500000
            maximo=1000000
        case "4": #Entre 100 y 500 mil
            minimo=100000
            maximo=500000
        case "5": #Entre 50 y 100 mil
            minimo=50000
            maximo=100000
        case "6": #Menor a 50 mil
            minimo=0
            maximo=50000
        case _: #Sin filtrar
            pass


    for pais in lista:

        if minimo <= int(pais["SUPERFICIE"]) < maximo:
            lista_filtrada.append(pais)

    

    if len(lista_filtrada) > 0:

        lista_filtrada= ordenamiento_lista(lista_filtrada)

        print(f"Rango de superficio: {rangos_superficie[int(rango)-1]}")
        imprimir_lista_paises(lista_filtrada)

    else:
        print(f"No hay paises del Rango de superficie {rangos_superficie[int(rango)-1]} en el listado")



"""*************************FALTAN*************************"""


#Funcion mayor_poblacion()

#Funcion menor_poblacion()

#Funcion calcular_promedio_poblacion()

#Funcion calcular_promedio_superficie()

#Función contar_paises_por_continente




"""*************************FIN*************************"""
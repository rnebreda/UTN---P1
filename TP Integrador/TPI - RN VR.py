""" Objetivo  
Desarrollar una aplicación en Python que permita gestionar información sobre países, 
aplicando listas, diccionarios, funciones, estructuras condicionales y repetitivas, 
ordenamientos y estadísticas. El sistema debe ser capaz de leer datos desde un archivo CSV, 
realizar consultas y generar indicadores clave a partir del dataset.

Dominio (dataset de países)  
Cada país estará representado con los siguientes datos:  
• Nombre (string)  
• Población (int)  
• Superficie en km² (int)  
• Continente (string)  

Funcionalidades mínimas del sistema  
El programa debe ofrecer un menú de opciones en consola que permita: 
• Agregar un país con todos los datos necesarios para almacenarse (No se 
permiten campos vacios). 
• Actualizar los datos de Población y Superfice de un Pais. 
• Buscar un país por nombre (coincidencia parcial o exacta).  
• Filtrar países por: 
    o Continente 
    o Rango de población 
    o Rango de superficie  
• Ordenar países por:  
    o Nombre  
    o Población  
    o Superficie (ascendente o descendente)  
• Mostrar estadísticas:  
    o País con mayor y menor población 
    o Promedio de población 
    o Promedio de superficie 
    o Cantidad de países por continente  

Validaciones  
• Controlar errores de formato en el CSV.  
• Evitar fallos al ingresar filtros inválidos o búsquedas sin resultados.  
• Mensajes claros de éxito/error.  


    1. Agregar paises (uno o multiples)
        el usuario decide cuándo dejar de agregar paises al dataset
    2. Modificar
        primero realiza una busqueda de un país por nombre (coincidencia parcial o exacta)
        y ofrece modificar población y/o superficie
    3. Buscar por nombre
        realiza una búsqueda de un país por su nombre (coincidencia parcial o exacta)
    4. Reportes por continente
        paises filtrados por continente y elegir el ordenamiento por nombre (por defecto), 
        superficie (ascendente o descendente) o población (ascendente o descendente)
    5. Reportes por población
        paises filtrados por rangos de población con ordenamiento por población (ascendente o descendente)
    6. Reportes por superficie
        paises filtrados por rangos de superficie con ordenamiento por superficie (ascendente o descendente)
    7. Estadísticas
            o País con mayor y menor población 
            o Promedio de población 
            o Promedio de superficie 
            o Cantidad de países por continente
    8. Salir
        finalizar la aplicación. """


#Importa librería de funciones utils
import utils

# Menú de opciones
paises_menu= ["1. Agregar paises", 
              "2. Modificar", 
              "3. Buscar por nombre", 
              "4. Reportes por continente",
              "5. Reportes por población",
              "6. Reportes por superficie",
              "7. Estadísticas",
              "8. Salir"]

# lista para paises
paises=[]

#crea el archivo si no existe
utils.crear_archivo("paises.csv")

#lee el contenido del archivo y lo carga en la lista como diccionarios
utils.paises_diccionarios("paises.csv", paises)

#bandera para finalización del programa
finalizado= False

#Todo el programa se encuentra dentro de un bucle while que finaliza al elegir
# la opción 8 del menú donde la bandera "finalizado" toma el valor "True" 

# print(paises)

while  not finalizado:

    #Muestra el menú en pantalla
    print()
    print("*** GESTION DE DATOS DE PAISES ***")
    for opcion in paises_menu:
        print(opcion)
    print()

    #Solicita elegir una opción y valida que la misma sea un dígito 
    # y que se encuentre dentro de los valores de las opciones del menú
    # La funcion utilizada no sale del while hasta que la opción elegida sea correcta
    opcion_elegida = utils.verificar_opcion_menu(input("Seleccione una opción del menú: "))
    print()

    #Utiliza una estructura match-case de acuerdo a la opción ingresada
    match opcion_elegida:

        case "1": #Agregar paises
            #permite cargar uno o varios paises de una sola vez, 
            # con su población, superficie y continente al que pertenece.
            #El programa ofrece seguir ingresando paises hasta elegir una opción distinta de "S" (S = Si)
            
            continuar_ingresando = True # "S = Si"

            while continuar_ingresando:
                

                utils.agregar_en_lista(paises)
                continuar_ingresando=input("Desea agregar más paises? (S = Si): ").upper().strip() == "S"

            print()
            
            #Muestra la lista modificada y actualiza el archivo
            utils.imprimir_lista_paises(paises)
            utils.actualizar("paises.csv", paises)

        case "2": #Modificar
            #primero realiza una busqueda de un país por nombre (coincidencia parcial o exacta)
            #luego ofrece modificar población y/o superficie

            #Verifica si hay paises en la lista
            #Si no tiene datos, muestra un mensaje y vuelve al menú
            if utils.lista_vacia(paises):
                continue

            #Si la lista contiene paises imprime el listado de paises existentes, 
            # precedidos por un número de orden
            utils.imprimir_lista_paises(paises)

            #Luego solicita elegir una opción (el número de orden del pais deseado)
            #Con una función valida que la opción ingresada sea un dígito
            # y esté dentro de los valores de números de orden del listado de paises
            #La función no sale del while hasta que la opción sea correcta
            pais_elegido=utils.verificar_opcion_ingresada(input("Ingrese el número del pais deseado: "), paises)

            #Permite modificar población y superficie del país elegido
            utils.modificar_pais(paises, pais_elegido-1)

            #Imprime la lista modificada y actualiza el archivo
            utils.imprimir_lista_paises(paises)
            utils.actualizar("paises.csv", paises)

        
        case "3": #Buscar por nombre
            #realiza una búsqueda de un país por su nombre (coincidencia parcial o exacta)

            #Verifica si hay paises en la lista
            #Si no tiene datos, muestra un mensaje y vuelve al menú
            if utils.lista_vacia(paises):
                continue

            #Solicita un nombre de pais y lo busca en la lista
            # Si se ingresa solo una letra o parte del nombre, devuelve listado de las coincidencias
            # ordenada alfabéticamente con un número de orden.
            #Luego solicita ingresar el número que pertenece al pais buscado 
            # o salir si este no está entre las coincidencias en la lista.
            #Si no hay coincidencias, informa al usuario que ese pais no existe en el listado.
            #Si lo encuentra muestra nombre, población, superficie y continente al que pertenece.
            pais_a_consultar= input("Ingrese el nombre del pais a consultar: ")
            
            #indice = utils.buscar_indice_por_nombre_pais(paises, pais_a_consultar)
            indice = utils.buscar_nombre_coincidencia_parcial(paises, pais_a_consultar)

            if indice >= 0:

                nombre = utils.extraer_nombre(indice, paises)
                poblacion = utils.extraer_poblacion(indice, paises)
                superficie = utils.extraer_superficie(indice, paises)
                continente = utils.extraer_continente(indice, paises)
                print(f"Pais:       {nombre}")
                print(f"Población:  {poblacion}")
                print(f"Superficie: {superficie}")
                print(f"Continente: {continente}")
                print()

            else:
                print("El pais buscado no existe en el listado.")
            input("Presiona una tecla para continuar...")

        
        case "4": #Reportes por Continente
            # El usuario elige el continente de un menú y el ordenamiento deseado en un submenú
            # muestra listado de paises filtrados por continente y 
            # permite elegir el ordenamiento por nombre (por defecto), 
            # superficie (ascendente o descendente) o población (ascendente o descendente)
            
            #Verifica si hay paises en la lista
            #Si no tiene datos, muestra un mensaje y vuelve al menú
            if utils.lista_vacia(paises):
                continue


            pass

            #Funcion reporte_por_continente()

        
        case "5": #Reportes por Población
            # El usuario elige el rango de valores de población de un menú 
            # y el ordenamiento deseado en un submenú
            # muestra listado de paises filtrados por rango de población y 
            # permite elegir el ordenamiento por nombre (por defecto), 
            # o población (ascendente o descendente) dentro del rango
            
            #Verifica si hay paises en la lista
            #Si no tiene datos, muestra un mensaje y vuelve al menú
            if utils.lista_vacia(paises):
                continue


            pass

            #Funcion reporte_por_poblacion()

        
        case "6": #Reportes por Superficie
            # El usuario elige el rango de valores de superficie de un menú 
            # y el ordenamiento deseado en un submenú
            # muestra listado de paises filtrados por rango de superficie y 
            # permite elegir el ordenamiento por nombre (por defecto), 
            # o superficie (ascendente o descendente) dentro del rango
            
            #Verifica si hay paises en la lista
            #Si no tiene datos, muestra un mensaje y vuelve al menú
            if utils.lista_vacia(paises):
                continue


            pass

            #Funcion reporte_por_superficie()


        case "7": #Estadísticas
            #Muestra las estadísticas solicitadas

            # País con mayor población
                #Funcion mayor_poblacion()

            # País con menor población
                #Funcion menor_poblacion()

            # Promedio de población (de todos los paises de la lista)
                #Funcion calcular_promedio_poblacion()

            # Promedio de superficie (de todos los paises de la lista)
                #Funcion calcular_promedio_superficie()

            # Cantidad de países por continente
                #Función contar_paises_por_continente


            pass


        case "8": #Salir
            #Termina la ejecución del programa.

            #Asigna el valor True a la bandera "finalizado" y sale del bucle while
            # informa que está finalizando la ejecución del programa, 
            # actualiza el archivo al salir y muestra un mensaje de salida.
            finalizado= True
            print("Finalizando el programa...")
            utils.actualizar("paises.csv", paises)
            print("Hasta luego!!")
            print()

        
        case _:
            #Por defecto, si se ingresa una opción no válida vuelve al menú
            print("La opción ingresada no es correcta")
            print()
            continue


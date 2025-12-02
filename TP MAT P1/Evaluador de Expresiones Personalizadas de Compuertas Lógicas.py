""" Simulador de Compuertas Lógicas con Evaluación de Expresiones Personalizadas

    Este programa permite al usuario ingresar expresiones lógicas personalizadas
    utilizando las compuertas lógicas básicas (AND, OR, NOT, XOR) y evalúa dichas
    expresiones para todas las combinaciones posibles de las variables involucradas.
    Expresa como resultado la tabla de verdad correspondiente.
    Puede evaluar expresiones de 2, 3 y 4 variables"""

# Definición de las compuertas lógicas básicas (simulación)
def NOT(a):
    return not a
def AND(a, b):
    return a and b
def OR(a, b):
    return a or b
def XOR(a, b):
    return (a or b) and not (a and b)


def simular_expresion_usuario_2_vars():
    """Permite al usuario ingresar una expresión lógica personalizada
     de 2 variables (A, B) y la evalúa."""

    print("\n--- Evaluación de Expresión Personalizada ---")
    print("Variables disponibles: A, B (se prueban todas las combinaciones)")
    print("Funciones/Compuertas disponibles: AND(A, B), OR(A, B), NOT(A), XOR(A, B)")
    print("Ejemplo de entrada: AND(A, OR(NOT(A), B))")
    
    # Solicitar la expresión lógica al usuario y la pasa a mayúsculas por compatibilidad
    expresion_str = input("\nIngrese su expresión lógica: ").upper()

    print(f"\nGenerando tabla de verdad para: {expresion_str}")
    print("| A | B | f(x)|")
    print("|---|---|-----|")

    # Preparamos el entorno seguro para la función eval()
    # Definimos qué funciones y variables puede usar eval()
    # El diccionario 'scope' contiene las funciones y variables permitidas
    scope = {
        'AND': AND,
        'OR': OR,
        'NOT': NOT,
        'XOR': XOR,
        'True': True,
        'False': False
    }
    
    # Iteramos sobre todas las combinaciones posibles de A y B
    for A in [False, True]:
        for B in [False, True]:
            # Añadimos A y B al scope local para cada iteración
            scope['A'] = A
            scope['B'] = B
            
            try:
                # Usamos eval() de forma controlada ya que solo las 
                # funciones y variables en 'scope' son accesibles
                # "__builtins__": None inhabilita completamente el acceso a todas las
                # funciones integradas de Python dentro de la ejecución de eval()
                resultado = eval(expresion_str, {"__builtins__": None}, scope)

                # Convertimos el resultado a 0/1 de forma segura
                #Si es booleano (True o False) lo convierte a entero 1 o 0
                if isinstance(resultado, bool):
                    resultado_int = int(resultado)

                #Si es entero (1 o 0) lo deja igual 
                elif isinstance(resultado, int) and resultado in (0, 1):
                    resultado_int = resultado

                else:
                    # Para otros tipos (None, objetos, etc.) usamos su truthiness 
                    # (valor de verdad implícito según Python)
                    resultado_int = int(bool(resultado))

                # Imprimimos la fila de la tabla
                print(f"| {int(A)} | {int(B)} |  {resultado_int}  |")

            except Exception as e:
                print(f"Error al evaluar la expresión con A={A}, B={B}: {e}")
                return # Salimos de la función si hay un error de sintaxis


def simular_expresion_usuario_3_vars():
    """
    Permite al usuario ingresar una expresión lógica personalizada y la evalúa 
    para 3 variables (A, B, C).
    """
    print("\n--- Evaluación de Expresión Personalizada (3 Variables) ---")
    print("Variables disponibles: A, B, C (se prueban todas las 8 combinaciones)")
    print("Funciones/Compuertas disponibles: AND(A, B), OR(A, B), NOT(A), XOR(A, B)")
    print("Ejemplo de entrada: AND(A, OR(B, AND(NOT(A), C)))")
    
    # Solicitar la expresión lógica al usuario y la pasa a mayúsculas por compatibilidad
    expresion_str = input("\nIngrese su expresión lógica: ").upper()

    print(f"\nGenerando tabla de verdad para: {expresion_str}")
    # Formato de cabecera para 3 variables
    print("| A | B | C | f(x)|")
    print("|---|---|---|-----|")

    # Preparamos el entorno seguro para eval(), idem al caso de 2 variables
    scope = {
        'AND': AND,
        'OR': OR,
        'NOT': NOT,
        'XOR': XOR,
        'True': True,
        'False': False,
        'A': False, 'B': False, 'C': False # Inicializamos variables en el scope
    }
    
    # Iteramos sobre todas las 8 combinaciones posibles de A, B, C
    for A in [False, True]:
        for B in [False, True]:
            for C in [False, True]:
                
                # Actualizamos las variables en el scope local para esta iteración
                scope['A'] = A
                scope['B'] = B
                scope['C'] = C
                    
                try:
                    # Usamos eval() de forma controlada, idem al caso de 2 variables
                    resultado = eval(expresion_str, {"__builtins__": None}, scope)
                        
                    # Convertimos el resultado a 0/1 de forma segura, idem al caso de 2 variables
                    if isinstance(resultado, bool):
                        resultado_int = int(resultado)

                    elif isinstance(resultado, int) and resultado in (0, 1):
                        resultado_int = resultado

                    else:
                        resultado_int = int(bool(resultado))

                    # Imprimimos la fila de la tabla
                    print(f"| {int(A)} | {int(B)} | {int(C)} |  {resultado_int}  |")                    
                    
                except Exception as e:
                    print(f"Error al evaluar la expresión para esta combinación: {e}")
                    print("Por favor, verifique su sintaxis y que use solo las variables A, B, C.")


def simular_expresion_usuario_4_vars():
    """
    Permite al usuario ingresar una expresión lógica personalizada y la evalúa 
    para 4 variables (A, B, C, D).
    """
    print("\n--- Evaluación de Expresión Personalizada (4 Variables) ---")
    print("Variables disponibles: A, B, C, D (se prueban todas las 16 combinaciones)")
    print("Funciones/Compuertas disponibles: AND(A, B), OR(A, B), NOT(A), XOR(A, B)")
    print("Ejemplo de entrada: AND(A, OR(B, AND(C, D)))")
    
    # Solicitar la expresión lógica al usuario y la pasa a mayúsculas por compatibilidad
    expresion_str = input("\nIngrese su expresión lógica: ").upper()

    print(f"\nGenerando tabla de verdad para: {expresion_str}")
    # Formato de cabecera para 4 variables
    print("| A | B | C | D | f(x)|")
    print("|---|---|---|---|-----|")

    # Preparamos el entorno seguro para eval(), idem al caso de 2 variables
    scope = {
        'AND': AND,
        'OR': OR,
        'NOT': NOT,
        'XOR': XOR,
        'True': True,
        'False': False,
        'A': False, 'B': False, 'C': False, 'D': False # Inicializamos variables en el scope
    }
    
    # Iteramos sobre todas las 16 combinaciones posibles de A, B, C, D
    for A in [False, True]:
        for B in [False, True]:
            for C in [False, True]:
                for D in [False, True]:
                    # Actualizamos las variables en el scope local para esta iteración
                    scope['A'] = A
                    scope['B'] = B
                    scope['C'] = C
                    scope['D'] = D
                    
                    try:
                        # Usamos eval() de forma controlada, idem al caso de 2 variables
                        resultado = eval(expresion_str, {"__builtins__": None}, scope)
                        
                        # Convertimos el resultado a 0/1 de forma segura, idem al caso de 2 variables
                        if isinstance(resultado, bool):
                            resultado_int = int(resultado)

                        elif isinstance(resultado, int) and resultado in (0, 1):
                            resultado_int = resultado

                        else:
                            resultado_int = int(bool(resultado))

                        # Imprimimos la fila de la tabla
                        print(f"| {int(A)} | {int(B)} | {int(C)} | {int(D)} |  {resultado_int}  |")                    
                    
                    except Exception as e:
                        print(f"Error al evaluar la expresión para esta combinación: {e}")
                        print("Por favor, verifique su sintaxis y que use solo las variables A, B, C, D.")

# --- Función Principal con Menú ---

def menu_principal():
    while True:
        
        print("\n=====================================")
        print("  Simulador de Compuertas Lógicas")
        print("=====================================")
        print("Seleccione una opción:")
        print("1. Evaluar Expresión Personalizada (2 Variables A, B)")
        print("2. Evaluar Expresión Personalizada (3 Variables A, B, C)")
        print("3. Evaluar Expresión Personalizada (4 Variables A, B, C, D)")        
        print()
        print("0. Salir")
        print("-------------------------------------")

        opcion = input("Ingrese el número de su opción: ")
        

        if opcion == '1':
            simular_expresion_usuario_2_vars()
        
        elif opcion == '2':
            simular_expresion_usuario_3_vars()

        elif opcion == '3':
            simular_expresion_usuario_4_vars()

        elif opcion == '0':
            print("Saliendo del programa. Hasta pronto!!!")
            print()
            input()
            break
        else:
            # ... (manejo de errores de opción) ...
            pass

# --- Ejecución del programa ---
if __name__ == "__main__":
    menu_principal()



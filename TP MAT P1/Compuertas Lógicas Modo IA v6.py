# Definición de las compuertas lógicas básicas (simulación)
def NOT_gate(entrada):
    return not entrada
def AND_gate(entrada_a, entrada_b):
    return entrada_a and entrada_b
def OR_gate(entrada_a, entrada_b):
    return entrada_a or entrada_b
def XOR_gate(entrada_a, entrada_b):
    return (entrada_a or entrada_b) and not (entrada_a and entrada_b)

# ... (Otras funciones omitidas para brevedad) ...

# --- FUNCIÓN ACTUALIZADA PARA 4 VARIABLES Y EXPRESIÓN DE USUARIO ---

def simular_expresion_usuario_4_vars():
    """
    Permite al usuario ingresar una expresión lógica personalizada y la evalúa 
    para 4 variables (A, B, C, D).
    """
    print("\n--- Evaluación de Expresión Personalizada (4 Variables) ---")
    print("Variables disponibles: A, B, C, D (se prueban todas las 16 combinaciones)")
    print("Funciones/Compuertas disponibles: AND_gate(), OR_gate(), NOT_gate(), XOR_gate()")
    print("Ejemplo de entrada: AND_gate(A, OR_gate(B, AND_gate(C, D)))")
    
    expresion_str = input("\nIngrese su expresión lógica: ")

    print(f"\nGenerando tabla de verdad para: {expresion_str}")
    # Formato de cabecera para 4 variables
    print("| A     | B     | C     | D     | Resultado|")
    print("|-------|-------|-------|-------|----------|")

    # Preparamos el entorno seguro para eval()
    scope = {
        'AND_gate': AND_gate,
        'OR_gate': OR_gate,
        'NOT_gate': NOT_gate,
        'XOR_gate': XOR_gate,
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
                        # Usamos eval() de forma controlada
                        resultado = eval(expresion_str, {"__builtins__": None}, scope)
                        # Imprimimos la fila de la tabla
                        print(f"| {str(A):<5} | {str(B):<5} | {str(C):<5} | {str(D):<5} | {str(resultado):<8} |")
                    except Exception as e:
                        print(f"Error al evaluar la expresión para esta combinación: {e}")
                        print("Por favor, verifique su sintaxis y que use solo las variables A, B, C, D.")
                        return # Salimos de la función si hay un error

# --- Función Principal con Menú Interactivo (Actualizado) ---

def menu_principal():
    while True:
        print("\n=====================================")
        print("  Simulador de Compuertas Lógicas")
        print("=====================================")
        print("Opciones:")
        # ... (Opciones individuales 1-4 omitidas) ...
        print("5. Simular Circuito Anidado Clásico (Sumador Medio Bit, 2 vars)")
        print("6. Evaluar Expresión Personalizada (2 Variables A, B)")
        print("7. Evaluar Expresión Personalizada (4 Variables A, B, C, D)") # Nueva Opción
        print("8. Salir")
        print("-------------------------------------")

        opcion = input("Ingrese el número de su opción: ")
        
        if opcion == '7':
            simular_expresion_usuario_4_vars()
        elif opcion == '8':
            print("Saliendo del programa. ¡Adiós!")
            break
        # ... (Resto de opciones if/elif) ...
        elif opcion not in ['1','2','3','4','5','6']:
             print("\nOpción no válida. Por favor, intente de nuevo.")


# --- Ejecución del programa ---
if __name__ == "__main__":
    menu_principal()




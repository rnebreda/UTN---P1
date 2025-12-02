# Definición de las compuertas lógicas básicas (simulación)
def NOT_gate(a):
    return not a
def AND_gate(a, b):
    return a and b
def OR_gate(a, b):
    return a or b
def XOR_gate(a, b):
    return (a or b) and not (a and b)


def simular_expresion_usuario():
    """Permite al usuario ingresar una expresión lógica personalizada y la evalúa."""
    print("\n--- Evaluación de Expresión Personalizada ---")
    print("Variables disponibles: A, B (se prueban todas las combinaciones)")
    print("Funciones/Compuertas disponibles: AND_gate(), OR_gate(), NOT_gate(), XOR_gate()")
    print("Ejemplo de entrada: AND_gate(A, OR_gate(NOT_gate(A), B))")
    
    expresion_str = input("\nIngrese su expresión lógica: ")

    print(f"\nGenerando tabla de verdad para: {expresion_str}")
    print("| A     | B     | Resultado|")
    print("|-------|-------|----------|")

    # Preparamos el entorno seguro para eval()
    # Definimos qué funciones y variables puede usar eval()
    scope = {
        'AND_gate': AND_gate,
        'OR_gate': OR_gate,
        'NOT_gate': NOT_gate,
        'XOR_gate': XOR_gate,
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
                # Usamos eval() de forma controlada
                resultado = eval(expresion_str, {"__builtins__": None}, scope)
                print(f"| {str(A):<5} | {str(B):<5} | {str(resultado):<8} |")
            except Exception as e:
                print(f"Error al evaluar la expresión con A={A}, B={B}: {e}")
                return # Salimos de la función si hay un error de sintaxis

# --- Función Principal con Menú Interactivo (Actualizado) ---

def menu_principal():
    while True:
        # ... (Opciones 1 a 5 omitidas para brevedad) ...
        print("\n=====================================")
        print("  Simulador de Compuertas Lógicas")
        print("=====================================")
        print("Seleccione una opción:")
        print("1. Evaluar Expresión Anidada Personalizada (Usuario)") # Opción clave
        print("2. Evaluar Expresión Anidada Personalizada (Usuario)") # Opción clave 

        print("0. Salir")
        print("-------------------------------------")

        opcion = input("Ingrese el número de su opción: ")
        
        # ... (if/elif para opciones 1-5 y 7 omitidos) ...

        if opcion == '1':
            simular_expresion_usuario()
        
        elif opcion == '2':
            simular_expresion_usuario()

        elif opcion == '0':
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            # ... (manejo de errores de opción) ...
            pass

# --- Ejecución del programa ---
if __name__ == "__main__":
    menu_principal()



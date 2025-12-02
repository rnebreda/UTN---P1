# Definición de las compuertas lógicas básicas (simulación)

def NOT_gate(entrada):
    return not entrada

def AND_gate(entrada_a, entrada_b):
    return entrada_a and entrada_b

def OR_gate(entrada_a, entrada_b):
    return entrada_a or entrada_b

def XOR_gate(entrada_a, entrada_b):
    return (entrada_a or entrada_b) and not (entrada_a and entrada_b)

# --- Funciones de dibujo ASCII ---

def dibujar_NOT_gate_ascii():
    print("\n  +---+")
    print("--|\\  |")
    print("  | >----")
    print("--|/  |")
    print("  +---+")

def dibujar_AND_gate_ascii():
    print("\n  +----_")
    print("--|     \\")
    print("  |      >----")
    print("--|     /")
    print("  +----_")

def dibujar_OR_gate_ascii():
    print("\n    ,--~|`.")
    print("--+  |  |  \\")
    print("  |  |  |   >----")
    print("--+  |  |  /")
    print("    `--~|,'")

def dibujar_XOR_gate_ascii():
    print("\n    ,--~|`.")
    print("--+ ~|  |  \\")
    print("  | ~|  |   >----")
    print("--+ ~|  |  /")
    print("    `--~|,'")

# --- Función Principal con Menú Interactivo ---

def menu_principal():
    """Muestra un menú de opciones para interactuar con las compuertas."""
    while True:
        print("\n=====================================")
        print("  Simulador de Compuertas Lógicas")
        print("=====================================")
        print("Seleccione una opción:")
        print("1. Dibujar compuerta NOT")
        print("2. Dibujar compuerta AND")
        print("3. Dibujar compuerta OR")
        print("4. Dibujar compuerta XOR")
        print("5. Simular un circuito personalizado (Tabla de Verdad)")
        print("6. Salir")
        print("-------------------------------------")

        opcion = input("Ingrese el número de su opción: ")

        if opcion == '1':
            dibujar_NOT_gate_ascii()
        elif opcion == '2':
            dibujar_AND_gate_ascii()
        elif opcion == '3':
            dibujar_OR_gate_ascii()
        elif opcion == '4':
            dibujar_XOR_gate_ascii()
        elif opcion == '5':
            # Llamamos a la función de simulación del ejercicio anterior
            simular_circuito_ejemplo_completo() 
        elif opcion == '6':
            print("Saliendo del programa. ¡Adiós!")
            break # Sale del bucle while y termina el programa
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")

# Función auxiliar para la opción 5 (simulación completa de tabla de verdad)
def simular_circuito_ejemplo_completo():
    print("\n--- Iniciando simulación de circuito: (A AND B) OR (NOT C) ---")
    print("| A     | B     | C     | Salida|")
    print("|-------|-------|-------|-------|")
    for A in [False, True]:
        for B in [False, True]:
            for C in [False, True]:
                # Definición del circuito: (A AND B) OR (NOT C)
                salida_and = AND_gate(A, B)
                salida_not = NOT_gate(C)
                resultado = OR_gate(salida_and, salida_not)
                print(f"| {str(A):<5} | {str(B):<5} | {str(C):<5} | {str(resultado):<5}|")
    print("--- Simulación completada ---")


# --- Ejecución del programa ---
# Llama a la función del menú principal para iniciar la interacción
if __name__ == "__main__":
    menu_principal()


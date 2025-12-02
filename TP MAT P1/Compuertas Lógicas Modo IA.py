# Definición de las compuertas lógicas básicas usando funciones

def NOT_gate(entrada):
    """Implementa la compuerta NOT."""
    return not entrada # El operador 'not' invierte el valor booleano

def AND_gate(entrada_a, entrada_b):
    """Implementa la compuerta AND."""
    return entrada_a and entrada_b # El operador 'and' requiere ambas entradas verdaderas

def OR_gate(entrada_a, entrada_b):
    """Implementa la compuerta OR."""
    return entrada_a or entrada_b # El operador 'or' requiere al menos una entrada verdadera

def XOR_gate(entrada_a, entrada_b):
    """Implementa la compuerta XOR (OR Exclusiva)."""
    # XOR es verdadero si las entradas son diferentes
    return (entrada_a or entrada_b) and not (entrada_a and entrada_b)

# Simulación de un circuito de ejemplo
# Circuito: (A AND B) OR (NOT C)

def circuito_ejemplo(A, B, C):
    """Simula un circuito lógico específico."""
    # Paso 1: Compuerta AND con entradas A y B
    salida_and = AND_gate(A, B)
    
    # Paso 2: Compuerta NOT con entrada C
    salida_not = NOT_gate(C)
    
    # Paso 3: Compuerta OR con las salidas de los pasos 1 y 2
    salida_final = OR_gate(salida_and, salida_not)
    
    return salida_final

# --- Prueba del circuito con diferentes combinaciones de entradas (Tabla de Verdad) ---

print("--- Tabla de Verdad para el circuito: (A AND B) OR (NOT C) ---")
print("| A     | B     | C     | Salida|")
print("|-------|-------|-------|-------|")

# Iteramos sobre todas las posibles combinaciones de True/False
for A in [False, True]:
    for B in [False, True]:
        for C in [False, True]:
            resultado = circuito_ejemplo(A, B, C)
            # Formateamos la salida para que sea legible
            print(f"| {str(A):<5} | {str(B):<5} | {str(C):<5} | {str(resultado):<5}|")

# Definimos las puertas lógicas como funciones simples
def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def XOR(a, b):
    return (a and not b) or (not a and b)

# Función para mostrar resultados de una tabla de verdad
def tabla_verdad():
    valores = [0, 1]  # posibles entradas
    print("A B | AND OR XOR")
    print("----------------")
    for a in valores:
        for b in valores:
            print(f"{a} {b} |  {int(AND(a,b))}   {int(OR(a,b))}   {int(XOR(a,b))}")

# Ejemplo de circuito: (A AND B) OR (NOT A)
def circuito(a, b):
    return OR(AND(a, b), NOT(a))

# Probamos el circuito
def probar_circuito():
    valores = [0, 1]
    print("\nCircuito: (A AND B) OR (NOT A)")
    print("A B | Resultado")
    print("----------------")
    for a in valores:
        for b in valores:
            print(f"{a} {b} |    {int(circuito(a, b))}")

# Ejecutamos las pruebas
tabla_verdad()
probar_circuito()

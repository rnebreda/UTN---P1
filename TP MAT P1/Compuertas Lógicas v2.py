# Definimos las puertas lógicas como funciones simples
def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def XOR(a, b):
    return (a and not b) or (not a and b)

# Función para mostrar menú
def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. AND")
    print("2. OR")
    print("3. NOT")
    print("4. XOR")
    print("5. Salir")

# Función principal
def simulador():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":  # AND
            a = int(input("Valor de A (0 o 1): "))
            b = int(input("Valor de B (0 o 1): "))
            print(f"Resultado AND({a},{b}) = {int(AND(a,b))}")

        elif opcion == "2":  # OR
            a = int(input("Valor de A (0 o 1): "))
            b = int(input("Valor de B (0 o 1): "))
            print(f"Resultado OR({a},{b}) = {int(OR(a,b))}")

        elif opcion == "3":  # NOT
            a = int(input("Valor de A (0 o 1): "))
            print(f"Resultado NOT({a}) = {int(NOT(a))}")

        elif opcion == "4":  # XOR
            a = int(input("Valor de A (0 o 1): "))
            b = int(input("Valor de B (0 o 1): "))
            print(f"Resultado XOR({a},{b}) = {int(XOR(a,b))}")

        elif opcion == "5":  # Salir
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida, intenta de nuevo.")

# Ejecutamos el simulador
simulador()


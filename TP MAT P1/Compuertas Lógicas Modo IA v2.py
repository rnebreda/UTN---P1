def dibujar_NOT_gate_ascii():
    print("  +---+")
    print("--|\\  |")
    print("  | >----")
    print("--|/  |")
    print("  +---+")

def dibujar_AND_gate_ascii():
    print("  +----_")
    print("--|     \\")
    print("  |      >----")
    print("--|     /")
    print("  +----_")

def dibujar_OR_gate_ascii():
    print("    ,--~|`.")
    print("--+  |  |  \\")
    print("  |  |  |   >----")
    print("--+  |  |  /")
    print("    `--~|,'")

# --- Ejemplo de uso ---

print("\nRepresentación gráfica de compuertas (ASCII Art):")

print("\nCompuerta NOT:")
dibujar_NOT_gate_ascii()

print("\nCompuerta AND:")
dibujar_AND_gate_ascii()

print("\nCompuerta OR:")
dibujar_OR_gate_ascii()


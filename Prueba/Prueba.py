edad = int(input("Por favor, ingrese su edad en años: "))

if 65 > edad >= 18:
    print("Debes votar obligatoriamente.")
elif 18 > edad >= 16 or edad >= 65:
    print("Puedes votar, pero no es obligatorio.")
else:
    print("No puedes votar")
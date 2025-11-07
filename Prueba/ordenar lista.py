lista = [{"C": "casa", "A": 1}, {"C": "perro", "A": 5}, {"C": "auto", "A": 9}, {"C": "mate", "A": 6}, {"C": "coro", "A": 3}, {"C": "tero", "A": 9}, {"C": "loro", "A": 2}, {"C": "agua", "A": 1}, {"C": "gas", "A": 4}, {"C": "luz", "A": 8}, {"C": "puerta", "A": 3}, {"C": "casa", "A": 7}]

print("Lista original")
print(lista)
print()

cant_elementos= len(lista)
for paso in range (len(lista) - 1):
    intercambio =False
    for i in range (len(lista) -1 - paso):
        if lista[i]["C"] > lista[i + 1]["C"]:
            lista[i]["C"], lista[i + 1]["C"] = lista[i + 1]["C"], lista[i]["C"]
            intercambio=True
    if not intercambio:
        break

print ("Lista ordenada")
print(lista)

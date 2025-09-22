# Lista
frutas = ["banana", "maçã", "uva"]

print(frutas[0])
print(frutas[1])
print(frutas[2])

print("--- Acessando os elementos a partir do final")
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])

frutas.append("pera")
print(frutas)

frutas.insert(1, "laranja")
print(frutas)

frutas.remove("banana")
print(frutas)

fruta_removida = frutas.pop(2)
print(frutas)
print(fruta_removida)

frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)

# Lista de compreensão
print("\nLista de Compreensão")
numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros if x % 2 == 0]
print(quadrados)


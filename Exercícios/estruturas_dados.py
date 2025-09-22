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


# Tuplas
print("\nTuplas")
ponto = (3, 4)

print(ponto[0])

def get_nome_completo():
    return "Fulano", "de Tal"

primeiro_nome, ultimo_nome = get_nome_completo()
print(primeiro_nome) 
print(ultimo_nome)   

minha_tupla = (1, 2, 3, 2, 4, 2)

busca = input("Qual elemento deseja verificar? ")
print(f"Quantas vezes o elemento {busca} aparece? {minha_tupla.count(int(busca))}")

print(minha_tupla.index(2, 2))
print(minha_tupla.index(2, 2, 4))
print(f"Tamanho da tupla: {len(minha_tupla)}")


# Dicionários
print("\nDicionários")

pessoa = {
    "nome": "Heloisa",
    "idade": 20,
    "cidade": "São Paulo"
}

print(f"Nome: {pessoa.get("nome")}")
print(f"Idade: {pessoa.get("idade")}")
print(pessoa)

pessoa["país"] = "Brasil"
print(pessoa)

pessoa.update({"profissão": "Engenheiro"})
print(pessoa)

print(f"Chaves: {pessoa.keys()}")
print(f"Valores: {pessoa.values()}")
print(f"Itens: {pessoa.items()}")


# Conjuntos (set)
print("\nConjuntos")

frutas = {"maçã", "banana", "laranja"}
frutas.add("pera")
print(frutas)

frutas.remove("banana")
print(frutas)

frutas.discard("uva")
print(frutas)

frutas.clear()
print(frutas)

print("-------- Operações básicas")
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2
print(f"União: {uniao}")

intersecao = conjunto1 & conjunto2 # elemento que tem nos dois conjuntos
print(f"Interseção: {intersecao}")

diferenca = conjunto1 - conjunto2 # só tem no conjunto 1
print(f"Diferença: {diferenca}")

diferenca_simetrica = conjunto1 ^ conjunto2 # tira o que tem nos dois
print(f"Diferença simétrica: {diferenca_simetrica}")
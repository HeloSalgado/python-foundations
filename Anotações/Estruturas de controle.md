# Estruturas de controle

Data: September 4, 2025

As estruturas de controle nos permitem controlar o fluxo de execução de nossos programas. Em Python, as estruturas de controle mais comuns são as estruturas condicionais e os loops. Essas estruturas nos permitem tomar decisões e repetir blocos de código segundo certas condições.

## Estruturas condicionais

Em Python , as estruturas mais utilizadas são if, if-else e if-elif-else.

### IF

A estrutura if é utilizada para executar um bloco de código se uma condição for verdadeira. A sintaxe básica é a seguinte:

```python
idade = 18

if idade >= 18:
   print ("Você é maior de idade.")
```

### IF-ELSE

A estrutura if-else nos permite especificar um bloco de código alternativo que será executado se a condição do if for falsa. A sintaxe básica é a seguinte:

```python
idade = 15

if idade >= 18:
   print ("Você é maior de idade.")

else:
   print ("Você é menor de idade.")
```

### IF-ELIF-ELSE

A estrutura if-elif-else nos permite especificar múltiplas condições e blocos de código alternativos. A sintaxe básica é a seguinte:

```python
nota = 85

if nota >= 90:
   print ("Excelente")

elif nota >= 80:
   print ("Muito bom")

elif nota >= 70:
   print ("Bom")

else:
   print ("Precisa melhorar")
```

## Loops

### For

O loop for é utilizado para iterar sobre uma sequência (como uma lista, uma tupla ou uma string) ou qualquer objeto iterável. A sintaxe básica é a seguinte:

```python
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
		print(fruta)
```

### While

O loop while é utilizado para repetir um bloco de código enquanto uma condição for verdadeira. A sintaxe básica é a seguinte:

```python
contador = 0

while contador < 5:
		print(contador)
		contador += 1
```

### Controle de loops

**Break**

A instrução break é utilizada para sair prematuramente de um loop, independentemente da condição. Quando um break é encontrado, o loop é interrompido e o fluxo de execução continua com a próxima instrução fora do loop.

```python
contador = 0

while true:
		print(contador)
		contador += 1
		
		if contador == 5:
				break
```

**Continue**

A instrução continue é utilizada para pular o restante do bloco de código dentro de um loop e passar para a próxima iteração.

```python
for i in range(10):
		if i % 2 == 0
				continue
		print(i)
```

**Pass**

A instrução pass é uma operação nula que não faz nada. É utilizada como um marcador de posição quando uma instrução é sintaticamente necessária, mas nenhuma ação é desejada.

```python
for i in range(5):
		pass
```

 Isso pode ser útil quando se está desenvolvendo um programa e se deseja reservar um bloco de código para implementá-lo mais tarde.
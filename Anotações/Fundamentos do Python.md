# Fundamentos do Python

Data: September 4, 2025

## Tipos de dados básicos

Em Python, os tipos de dados básicos são as categorias nas quais podemos classificar os valores que utilizamos em nossos programas. Compreender os diferentes tipos de dados é fundamental para trabalhar com variáveis e realizar operações em Python. Os tipos de dados básicos incluem:

### Inteiros (int)

Os números inteiros são aqueles que não têm parte decimal. Em Pyhton, são representados simplesmente escrevendo o número sem aspas nem pontos decimais. Por exemplo:

```python
idade = 25
quantidade = 100
```

### Flutuantes (float)

Os números flutuantes, também conhecidos como números de ponto flutuante, são aqueles que têm uma parte decimal. Em Python, sçao representados utilizando um ponto para separar a parte inteira da parte decimal. Por exemplo:

```python
preco = 9.99
altura = 1.76
```

### Cadeias de texto (strings)

As cadeias de texto, ou simplesmente cadeias, são sequências de caracteres encerradas entre aspas simples (’…’) ou duplas (”…”). São utilizadas para representar texto em Python. Por exemplo:

```python
nome = "Juan"
mensagem = 'Olá mundo!'
```

Você pode incluir caracteres especiais nas cadeias utilizando o caractere de escape \. Por exemplo, para incluir aspas dentro de uma cadeia, você pode usar \' ou \". Também pode utilizar a notação de tripla aspa ('''...''' ou """...""") para criar cadeias de várias linhas.

### Booleanos

Os valores booleanos representam os valores de verdade: True (verdadeiro) e False (falso). São comumente utilizados em expressões condicionais e operações lógicas. Por exemplo:

```python
eh_maior_de_idade = True
tem_desconto = False
```

<aside>

⚠️ Valores booleanos começam com letra maiúscula: True e False

</aside>

## Variáveis

Em Python, não é necessário declarar o tipo de dados de uma variável com antecedência, pois o Python infere o tipo de dados automaticamente com base no valor atribuído.

### Declaração e atribuição de variáveis

As variáveis são contêineres que nos permitem armazenar e manipular dados em nossos programas. Para declarar e atribuir um valor a uma variável em Python, utilizamos o operador de atribuição =. O nome da variável vai à esquerda do operador, e o valor que você deseja atribuir vai à direita. Por exemplo:

```python
nome = "Juan"
idade = 25
altura = 1.75
é estudante = True
```

No exemplo, declaramos e atribuímos valores às variáveis nome, idade, altura e é_estudante. O Python infere automaticamente o tipo de dados de cada variável com base no valor atribuído.

Você também pode atribuir o mesmo valor a várias variáveis em uma única linha usando o operador de atribuição múltipla:

```python
a = b = c = 10
```

Neste caso, as variáveis a, b e c terão o valor 10.

### Regras para nomear variáveis

- Os nomes das variáveis só podem conter letras (a-z, A-Z), números (0-9) e sublinhados (_). Não podem começar com um número.
- Não se pode usar palavras-chave reservadas do Python como nomes de variáveis (por exemplo, if, else, for, while, etc.).
- O Python diferencia maiúsculas de minúsculas, então nome e Nome são variáveis diferentes.
- Recomenda-se usar nome descritivos para as variáveis, que indiquem claramente seu propósito: nome, idade, total_vendas, etc.

Variáveis válidas:

```python
idade
nome_completo
total_vendas
_contador
```

Variáveis inválidas:

```python
1idade # Começa com número
nome-completo # Usa um hífen em vez de um sublinhado
if # Palavra-chave reservada do Python
```

<aside>

📌 **Escolher nomes descritivos para suas variáveis facilita a leitura e compreensão do código, tanto para você quanto para outros desenvolvedores que possam trabalhar no mesmo projeto.**

</aside>

## Operadores

### Operadores Aritméticos

| Operador | Descrição | Exemplo (`a=10`, `b=3`) | Resultado |
| --- | --- | --- | --- |
| `+` | Soma | `a + b` | 13 |
| `-` | Subtração | `a - b` | 7 |
| `*` | Multiplicação | `a * b` | 30 |
| `/` | Divisão (float) | `a / b` | 3.333... |
| `//` | Divisão inteira | `a // b` | 3 |
| `%` | Módulo (resto) | `a % b` | 1 |
| `**` | Exponenciação | `a ** b` | 1000 |

### Operadores de Comparação

| Operador | Descrição | Exemplo (`a=10`, `b=3`) | Resultado |
| --- | --- | --- | --- |
| `==` | Igual a | `a == b` | False |
| `!=` | Diferente de | `a != b` | True |
| `>` | Maior que | `a > b` | True |
| `<` | Menor que | `a < b` | False |
| `>=` | Maior ou igual a | `a >= b` | True |
| `<=` | Menor ou igual a | `a <= b` | False |

### Operadores Lógicos

| Operador | Descrição | Exemplo (`a=10`, `b=3`) | Resultado |
| --- | --- | --- | --- |
| `and` | Verdadeiro se **ambos** forem verdadeiros | `(a > 5) and (b < 5)` | True |
| `or` | Verdadeiro se **um** for verdadeiro | `(a > 15) or (b < 5)` | True |
| `not` | Inverte o valor lógico | `not (a > 5)` | False |

<aside>

💡 **Python segue as regras de precedência de operadores, onde certos operadores têm prioridade sobre outros. Em geral, a precedência segue a ordem: parênteses, exponenciação, multiplicação/divisão, soma/subtração, operadores de comparação e operadores lógicos.**

</aside>
# Introdução ao Python

Data: September 4, 2025

Python foi criado por Guido van Rossum, um programador holandês, no final dos anos 80 e início dos anos 90. A primeira versão do Python, a 0.9.0, foi lançada em 1991. Guido van Rossum nomeou a linguagem em homenagem ao grupo de comédia britânico Monty Python, do qual era um grande fã.

**Python foi projetado com o objetivo de ser uma linguagem fácil de ler e escrever, com uma sintaxe clara e concisa**. Ao longo dos anos, evoluiu e ganhou popularidade até se tornar uma das linguagens de programação mais utilizadas no mundo.

## Características

**Legibilidade**: Python utiliza uma sintaxe clara e simples, o que facilita a leitura e compreensão do código. Utiliza identação (espaço e tabulações) para delimitar blocos de código, o que promove um estilo de programação estruturado e legível

**Multiplataforma**: Pode ser executado em diferentes sistemas operacionais, como Windows, macOS e Linux, sem precisar modificar o código. Isso o torna uma linguagem versátil e portátil.

**Tipagem dinâmica**: Não é necessário declarar explicitamente o tipo de dado das variáveis. Python infere automaticamente o tipo de dado com base no valor atribuído a uma variável, o que simplifica a escrita de código.

**Ampla biblioteca padrão**: Python vem com uma extensa biblioteca padrão que fornece uma grande quantidade de módulos e funções para realizar diversas tarefas, como manipulação de arquivos, conexão a banco de dados, processamento de texto, entre outros.

**Interpretado**: O código é executado linha por linha em tempo real. Isso permite um ciclo de desenvolvimento rápido e facilita a depuração do código.

**Comunidade ativa**: Python conta com uma comunidade de desenvolvedores grande e ativa que contribui com bibliotecas, frameworks e ferramentas adicionais. Isso significa que você encontrará uma grande quantidade de recursos e suporte disponíveis.

## Aplicações

**Desenvolvimento web**: Python é amplamente utilizado no desenvolvimento web backend, com frameworks populares como Django e Flask.

**Ciência de dados**: É a linguagem preferida para análise de dados e ciência de dados devido a bibliotecas como NumPy, Pandas e Matplotlib.

**Inteligência artificial e machine learning**: É a escolha principal para projetos de IA e machine learning, graças a bibliotecas como TensorFlow e Scikit-learn.

**Automatização de tafefas**: Pode ser utilizado para automatizar tarefas repetitivas, como processamento de arquivos, web scraping e testes de software.

**Desenvolvimento de jogos**: É utilizado no desenvolvimento de jogos simples, especialmente com bibliotecas como Pygame.

### Jupyter notebook

Uma aplicação web interativa que permite criar e compartilhar documentos que contêm código ao vivo, equações, visualizações e texto explicativo. É comumente usado em ciência de dados, análise e aprendizado de Python.

Para usar Jupyter Notebook:

1. Abra a linha de comando (Terminal no macOS/Linux ou Prompt de Comando no Windows).
2. Execute o seguinte comando para instalar Jupyter Notebooks:
    
    ```
    pip install jupyter notebook
    ```
    
3. Uma vez instalado, execute o seguinte comando para iniciar Jupyter Notebook:
    
    ```
    jupyter notebook
    ```
    
    Uma janela do navegador será aberta com a interface do Jupyter Notebook.
    
4. Clique em "New" e selecione "Python 3" para criar um novo caderno (*notebook)*.

### Executar pela linha de comando

```
python .\ola_mundo.py // nome do arquivo                                                                             
```

# Conceitos básicos da sintaxe em Python

### Indentação

No Python, a indentação (espaços ou tabulações no início de uma linha) é utilizada para delimitar blocos de código. Diferente de outras linguagens que utilizam chaves ou palavras-chave, o Python utiliza a indentação para delimitar o escopo das declarações. Por exemplo:

```python
if condition:
		# Bloco de código se a condição for verdadeira
    instrucao1
    instrucao2
else:
		# Bloco de código se a condição for falsa
    instrucao3
    instrucao4
```

<aside>

⚠️ **É fundamental manter uma indentação consistente em todo o código para evitar erros de sintaxe.**

</aside>

### Comentários

Os comentários são linhas de texto no código que são ignoradas pelo interpretador do Python. Eles são utilizados para explicar ou documentar o código. No Python, os comentários de uma única linha começam com o símbolo #, enquanto os comentários de várias linhas são delimitados por três aspas """ . Por exemplo:

```python
# Este é um comentário de uma única linha

"""
Este é um comentário
de várias linhas
"""
```

### Sensibilidade a maiúsculas e minúsculas

Python distingue entre maiúsculas e minúsculas. Portanto, variável, Variável e VARIÁVEL são consideras variáveis diferentes.

### Ponto e vírgula

Diferente de outras linguagens, o Python não requer o uso de ponto e vírgula (;) ao final de cada instrução. No entanto, se você desejar escrever várias instruções em uma única linha, pode separá-las com um ponto e vírgula. Por exemplo:

```python
instrucao1; instrucao2; instrucao3
```

### Uso de parênteses

Os parênteses são utilizados para agrupar expressões, definir funções e realizar chamadas a funções. Por exemplo:

```python
resultado = (a + b) * c
```
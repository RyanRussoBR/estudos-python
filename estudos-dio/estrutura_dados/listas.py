# # As listas são sequências que podem guardar qualquer tipo de objeto, tendo str, float, outras listas (listas aninhadas), entre outras.
# # Pode-se criar uma lista usando o construtor list, ou colocando colchetes, que por sinal é o mais comum
# frutas = ['laranja', 'maca', 'uva']
# frutas = [] # lista vazia

# letras = list('python') # usando list, esse construtor pede um argumento iterável, ou seja, pode percorrer o que está sendo argumentado, string e range por exemplo.
# numeros = list(range(10))

# carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True] # Listas com string, inteiros e booleanos tudo junto.
# # Para exibir algum objeto de uma lista, é possível fazer o acesso direto, usando chaves e o índice do objeto que quero exibir.(indice começa do 0)
# print(carro[0], carro[4])
# print(carro[-1]) # Quando pegamos uma lista da direita para esquerda, o índice começa pelo -1 (ultimo elemento)

# # Listas Aninhadas (lista dentro de lista)
# # É usado para criar tabelas e matrizes.
# matriz = [
#     [1, "a", 2],
#     ["b", 3, 4],
#     [6, 5, "c"]
# ]

# print(matriz[0]) # primeira lista inteira
# print(matriz[0][0]) # primeiro elemento da matriz
# print(matriz[0][-1]) # ultimo elemento da primeira lista
# print(matriz[-1][-1]) # ultimo elemento da matriz

# # Para fazer a leitura dos elementos de uma lista ou matriz, é usando o operador de repetição for
# carros = ["gol", "siena", "celta"]
# for carro in carros: # lembra dessa sintaxe mané
#     print(carro, end=' -> ')
# print("fim")

# # E tem a função enumerate, que vi por fora primeiro, agora vem a tona, ela permite com que mostremos o indice do elemento que está sendo exibido olha que legal
# carros = ["gol", "siena", "celta"]
# for indice, carro in enumerate(carros): 
#     print(f'{carro} Indice({indice})', end=' -> ')
# print("fim")

# # Compreensão de lista
# # Usando o for, cria-se uma nova lista baseada em uma existente, porém aplicando novos valores nos elementos, ou métodos e funções, ou seja, modificando-a

# numeros = [1, 4, 56, 23, 36, 27, 43, 56]
# pares = []
# for numero in numeros:
#     if numero % 2 == 0 and numero not in pares: # essa foi para não exibir o 56 duas vezes, só um teste mental mesmo.
#         pares.append(numero) # no append declara primeiro antes do . em qual lista vai adicionar o que estar no parênteses, que é o valor que está percorrendo

# print(pares)

# # tem outra versão para isso, mas sei la, achei mais zoado
# numeros = [1, 4, 56, 23, 36, 27, 43, 56]
# pares = [numero for numero in numeros if numero % 2 == 0]
# print(pares)

# # da para modificar os valores tambem

# numeros = [1, 4, 56, 23, 36, 27, 43, 56]
# quadrado = []
# for numero in numeros:
#     quadrado.append(numero ** 2) 

# print(quadrado)

# # versão one line
# numeros = [1, 4, 56, 23, 36, 27, 43, 56]
# quadrado = [numero ** 2 for numero in numeros]
# print(quadrado)

# Métodos:
# Como tem ali em cima, o método append[] realiza a adição de elementos em uma lista. lista_que_quero_add.append(elemento_add)
# Também tem o método clear, limpa a lista, sempre coloca parenteses no final por ser um método
# lista = [1, 5 , 8, ["A", 2, "c"]]
# lista.clear()
# print(lista) # Realmente limpa a lista inteira, imagina num código legado jesus amado

# # Já o método copy, ao meu ver, é como se fosse uma branch separada (igual no git hub), que a pessoa pode mexer no conteúdo sem interferir no código, ou no caso a lista original, só que é uma copia superficial, no caso da lista dentro da lista, a copia considera a lista como um unico elemento, se há alteração nele, altera tanto na cópia quanto na original
# lista = ["a", 12 , 58, "Ryan", [1,2,3]]
# l2 = lista.copy()

# print(id(lista), id(l2))

# l2[4][0] = "sei la bro"
# l2[2] = "Shaolin matador de porco"

# print(lista)
# print(l2)

# # Já o count conta quantas vezes um elemento aparece em uma lista: a sintaxe é a mesma, coloca primeira antes do . a lista que quero "mexer", o método, e o elemento que quero exibir ou modificar informações
# cores = ['vermelho', 'vermelho', 'verde', 'azul', 'verde', 'rosa']
# print(cores.count('vermelho'))
# print(cores.count('rosa'))
# print(cores.count('verde'))

# # Tem o extended que adiciona mais elementos e uma só vez, ao contrário do append que adiciona de um em um
# ling = ['java', 'c#', 'c']
# print(ling)
# ling.extend(['python', 'ruby']) # nunca esquecer dos colchetes malandro heheheh
# print(ling)

# # Tem o index que ve quando é a primeira ocorrência de um elemento, qual indice fica o primeiro elemento citado no argumento, bom para testes
# ling = ['java', 'c#', 'c']
# print(ling)
# ling.extend(['python', 'ruby']) # nunca esquecer dos colchetes malandro heheheh
# print(ling.index('c#'))

# O pop remove o ultimo elemento, mas quando indica o índice ele remove o indicado
# ling = ['java', 'c#', 'c', 'c#']
# print(ling.pop(0))
# print(ling)
# # Já o remove remove o que for indicado no argumento, porém remove somente a primeira ocorrência
# ling = ['java', 'c#', 'c', 'c#']
# ling.remove('c#')
# print(ling)

# O reverse espelha a lista;
# ling = ['java', 'c#', 'c', 'c#']
# ling.reverse()
# print(ling)

# Já o sort faz a ordenação de uma lista, com a função reverse = true invertendo-a, e lambna (função anônima) x: len(x) ordenando de acordo com o tamanho das strings
# ling = ['python', 'java', 'c', 'c#', 'ruby']
# ling.sort()
# print(ling)
# ling.sort(reverse=True)
# print(ling)
# ling.sort(key=lambda x: len(x))
# print(ling)
# ling.sort(key=lambda x: len(x), reverse=True)
# print(ling)

# # Se não quiser usar o sort, posso usar o sorted, faz a mesma coisa, porém para printar direto ele é o ideal, economiza linhas no código
# print(sorted(ling))

# # O len indica o tamanho de uma lista
# print(len(ling))
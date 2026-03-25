# Tuplas é como se fosse a irmã da lista, porém as tuplas são imutáveis(seus elementos não podem ser modificados), já as listas são mutáveis(seus elementos podem ser modficados)
# Para criar, se utiliza a classe tuple, ou colocando os valores entre parênteses, separados por vírgula

# frutas = ('laranja', 'maça', 'uva',) # para o python diferenciar a tupla de precedência de operadores, se coloca aquela vírgula depois do ultimo elemento
# numeros = tuple([1,2,5,67])
# letras = tuple("python") # quando tem a classe tuple, nao precisa de utilizar a vírgula no final

# pais = ("Brasil",) # mesma coisa ali da primeira tupla

# # Para fazer o Acesso Direto de um elemento de uma tupla, é igual ao de listas, usando colchetes e o indice 
# print(pais[0])
# print(letras[4])

# # Detalhe que reparei, quando se usa o tuple em uma string, parece que é um for, ele percorre a string, já sem o tuple, a string inteira é considerada um índice

# # E como a lista, com a tupla é possivel fazer elas aninhadas, ou seja, fazer matrizes e tabelas
# matriz = (
#     (1, "a", 2),
#     ("b", 3, 4),
#     (6, 5, "c"),
# )

# # para acessar elementos é a mesma coisa das listas aninhadas
# print(matriz[0])
# print(matriz[1][1])
# print(matriz[0][-1])
# print(matriz[-1][-1]) 

# e como se não fosse diferente, o fatiamento é a mesma coisa que as listas, com os [start:stop:step]

# No caso de métodos, as tuplas não possuem o remove, pop, e de ordenamento como o sort, pois são imutáveis, mas tem esses
# Index, para saber a posição de um elemento na tupla
# linguagens = ('java', 'ruby', 'typescript', 'python')
# print(linguagens.index('java'))

# # count, para informar quantas vezes ocorre um objeto na tupla
# linguagens = ('java', 'python', 'ruby', 'typescript','java', 'python',)
# print(linguagens.count('python'))

# # e o len, para saber o "tamanho" ou quantos elementos tem a tupla
# print(len(linguagens))

# Detalhe pós-exercício, é OBRIGATÓRIO colocar a vírgula em uma tupla com único elemento, se não o python interpretará como uma string.
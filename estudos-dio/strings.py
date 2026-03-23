# Principais métodos de String
# Upper -> deixa TODAS as letras da string maiúsculas.
# Lower -> deixa todas as letras da string minúsculas.
# Title -> deixa somente a PRIMEIRA letra maiúscula.
# nome = 'ryaN'
# print(nome.title())

# Quando o usuário faz com que recebamos alguma informação com espaço, tem um método para eliminarmos esses espaços, com o método STRIP
# rstrip(direita) - lstrip(esquerda), strip(remove todos os espaços)
# nome = input()
# print(nome.lstrip())

# Para centralizar uma string, é usado o método CENTER, que possui dois argumentos (10, "#"), o 10 é a quantidade de caracteres que a string vai ocupar, e o segundo é opcional, sendo o caracter que vai ocupar os espaços vazios que ficarão, e se não ter nada, vai ser espaço vazio

# Também têm a junção, com o método JOIN, o formato dele é meio diferente: print(".".join(curso)), é como se fosse o for, ele passa letra a letra e adiciona entre elas o caracter que tem antes do .join
# nome = input()
# print('-'.join(nome))

# nome = input('Qual o seu nome? -> ')

# while True:
#     print('-'*140)
#     print('O que quer fazer?\n1. Para mostrar seu nome maiúsculo e minúsculo e título\n2. Para mostrar corrigir seu nome sem espaços em branco.\n3. Para mostrar seu nome com caracter que voce querer entre as letras, e centralizado com os caracteres que você quiser (ou não :p)\n4. para Sair. ')
#     print('-'*140)
#     escolha = int(input('-> '))

#     if escolha == 1:
#         print(nome.upper(), '-> Nome Maiúsculo')
#         print(nome.lower(), '-> Nome Minúsculo')
#         print(nome.title(), '-> Nome no modo Título')
#     elif escolha == 2:
#         print(nome.strip())
#     elif escolha == 3:
#         caract = str(input('Qual caracter -> '))
#         print(f'{caract}'.join(nome))
#         print(nome.center(30, caract))
#     elif escolha == 4:
#         print('Programa Encerrado.')
#         break
# Programa criado totalmente no improviso pra eu aprender hauhudasushdu


# Interpolação de strings
# Aula da famosa f-string, porém há métodos antigos, os com %, %s, % ou #f
# E também esse format ai, que até fiz uma piadinha, 

# #é ultrapassado mas quando tem um dicionario, as vezes utilizam esse método ainda.
# dados = {"nome": 'Ryan', "idade": 20, "saldo": 209.2345}

# print('Nome: {nome}, idade: {idade}, Saldo: {saldo:.2f}'.format(**dados))

# E o método mais atual que temos, que é o maravilhoso e incrível f-string, com o formato sendo f'sou o {nome}, tenho {idade} anos.
# E com a f string, tem como formatar pontos flutuantes, usando o :.2f (duas casas decimais por exemplo)
# nome = 'Ryan'
# idade = 20
# print('Olá, meu nome é {1}, tenho {0} anos'.format(nome, idade)) # piadinha uiui meu nome é 20 rsrsrsr

# PI = 3.14159
# print(f'Valor de pi: {PI:.5f}')
# print(f'Valor de Pi: {PI:20.2f}') # o 10 ali é o tamanho que vai ficar, ele vai mais pra direita, famoso width


# Fatiamento de string
# É como se eu pegasse parte da string e exibisse só o que é informado dentro das chaves, nome[start:stop:step] - esse formato ai mano
# Curiosidade, para fazer o espelhamento, se faz nome[::-1]
# nome = 'Ryan Gorecki Russo'
# print(nome[::-1])

# String com multiplas linhas
# É feita com tres aspas simples (''') ou 3 aspas duplas (""")
# Bom para menus, e para evitar um monte de \n no print
# nome = input('NOme:')
# print(f'''
# Olá meu nome é {nome}
# Eu estou aprendendo Python
#       ''')

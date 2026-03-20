# print('Hello World!, Vou aprender python e entrar no mercado ihuu') #primeiro programa do dio :)



# Aula de Variáveis e Constantes

# Quando for atribuir nome para constantes, sempre colocar o nome em MAIÚSCULO, pois o Python não sabe diferenciar uma variável de uma constante (nenhuma linguagem na vdd huashudsahuha)

# nome = 'Ryan'
# idade = 20
# nome, idade = ("Ryan", 20) -> Outra forma
# print(nome, idade)

# limiteSaque_diario = 1000 # Esse tipo de nome ficou estiloso


# BRAZILIAN_STATES = [ "SP", "RJ", "PR", "AL"] # Esse é uma constante, nome somente com letras maíusculas, letra até fica diferente uwu

# # BRAZILIAN_STATES = 10 #Porém se tentar alterá-lo, ele irá pois o Python não identifica automaticamente como constante, tudo pra ele é variável

# print(BRAZILIAN_STATES)



# Aula de conversão de tipos.

# print(int('10')+5) #Não precisa fazer isso, somente teste.

# preco = 10
# # print(preco)

# # preco = float(preco)
# # print(preco)

# # Divisão retorna resultado com ponto flutuante, mesmo se o resultado de um número inteiro
# print(preco/2)

# # E para tirar o ponto flutuante só converter para int o valor.
# print(int(preco/2))



# Aula de funções de entrada e saída

# nome = input('Qual o nome -> ')
# print('Olá',nome,'-','Seja bem vindo(a)') 

# Print com argumentos opcionais

# nome = 'Ryan'
# sobrenome = 'Russo'

# print(nome, sobrenome)
# print(nome, sobrenome, end='...\n') #O end coloca o que está nas aspas no final do print
# print(nome, sobrenome, sep='#')#Já o sep coloca o que está nas aspas no espaço que o print terá

# nome = input('Qual o seu nome? ')
# sobrenome = input('Qual seu sobrenome? ')

# print(nome, sobrenome)
# print(nome, sobrenome, end='...\n')
# print(nome, sobrenome, end='...\n', sep='$')
# print(nome, sobrenome, sep='$')


#Tive a impressão de que o end além de adicionar coisas no final, ele "junta" dois prints na mesma linha



# Operadores aritméticos
# print(12/2) #Divisão
# print(12//3) #Divisão por inteiro

# print(10%3) # Módulo (quantos 3 cabem dentro de 10)
# print(2**3) # Exponenciação


# Ordem de precedência
# x = 10 / 2 * 4
# print(x)
# Quest: Resultado vai dar 0 ou 10
# ans: Acho que vai dar 0 segunda a ordem de precedência. CORRECT

# A precedência ocorre na seguinte ordem:
# Parênteses -> Expoentes (Exponenciação) -> Multiplicação e Divisão (da esquerda para direita, desde que sem parênteses) -> Adição e Subtração (da esquerda para direita, desde que sem parênteses) 

# Operadores de comparação (para comparar dois valores) E sempre retorna um valor booleano (True ou False):
# Igualdade (==)
# Maior / Maior ou igual (>=) 
# Menor / Menor ou igual (<=) parece uma flecha bem legal
# saldo = 600
# saque = 500
# print(saldo < saque)
# UM DOS MAIS IMPORTANTES NO CÓDIGO

# Operadores de atribuição 
# Aqui é o sinal de = (igual), mas como vi na aula de lógica de programação, mudei meu pensamento, não chamo mais sinal de igual, mas sim de atribuição (etiqueta)
# Também consigo fazer adição na atribuição com +=
# Já para subtrair fica -=
# Com multiplicação *=
# Com divisão /= e Divisão inteira //=
# Com módulo %= e com Exponenciação **=
# saldo = 500
# print(saldo)
# saldo //= 200
# print(saldo)

# Operadores lógicos
# É uma operação que geralmente está junto com os operadores de comparação que "concatena" tudo como uma grande expressão lógica
# Operador e (and) - Para ser True, os dois (ou todas as comparações) devem ser True
# Operador ou (or) - Para ser True, basta uma das comparações ser True, já para ser False todos devem ser False
# Operador Negação (not) - O contrário da comparação, se for um True, vai resultar em False, pode negar tanto sequências de caracteres (strings) e objetos (listas)
# Os operadores lógicos e de comparação sempre trabalham juntinhos, olha que fofo!
# saldo = 1000
# saque = 200
# limite = 100

# print(not saldo >= saque or saque <= limite)

# Interessante usar parêtenses se o operador lógico ser muito extenso, seguindo o exemplo:

# saldo = 1000
# saque = 200
# limite = 100
# conta_especial = True

# print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))

# Dica: As comparações são melhores guardarem em variáveis para que o código fique mais legível
# saldo = 1000
# saque = 200
# limite = 100
# conta_especial = True

# conta_com_saldoSuficiente = saldo > saque and saque <= limite
# conta_especial_com_saldoSuficiente = conta_especial and saldo >= saque

# exp2 = conta_com_saldoSuficiente or conta_especial_com_saldoSuficiente
# print(exp2) # Caraca fica bem melhor
 
# Operadores de identidade: Ele comparar se dois objetos ocupam mesmo espaço na memória
# Operador Is, ele verifica se o objeto em questão ocupa a mesma posição de outro objeto
# Operador Is not, é somente a negação como todo o not :)
# Operador is instance, verifica o tipo de dado que uma variável é, se é int, str, etc. # esse peguei porque sou curioso kkkkkk
# Funciona tanto com strings quanto com numeros
# curso = 'Curso de Python'
# nome_curso = curso
# saldo, limite = 200, 200

# # print(saldo is limite)
# saldo, limite = 'Alo', 1000
# print(isinstance(saldo, str))


# Operadores de Associação: Verifica se algum objeto pertence a uma sequência
# Operador in
# Operador not in (contrário)
# Muito utilizado, principalmente em banco de dados
# frutas = [
#     "melancia",
#     "laranja",
#     "uva"
# ]

# print("uva" in frutas)

# curso = ('Curso de Python')

# print('python' not in curso)


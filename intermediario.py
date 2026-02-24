#1 Sistema de login, com acessos e bloqueios em caso de senha incorreta por 3 vezes
# from time import sleep
# print('-'*97)
# print('Bem vindo(a) ao nosso site! Crie um login e uma senha para continuar!')
# print('-'*97)

# login = str(input('Login: '))
# senha = str(input('Senha: '))

# sleep(2)
# print('Processando...')
# sleep(2)

# print('Conta criada! Agora logue para poder continuar!')
# print('-'*97)

# erros = 0
# user = ''
# senhaUser = ''

# while erros < 3:
#     user = str(input('Digite o seu login: '))
#     senhaUser = str(input('Digite sua senha: '))

#     if user == login and senhaUser == senha:
#         print('Acesso Liberado!')
#         break

#     print('Login ou senha incorretos! Tente novamente')
#     erros += 1

# if erros == 3:
#     print('Acesso bloqueado!')

#2 Jogo de adivinhação com dicas se o número sorteado é menor ou maior que o digitado pelo usuário
from random import randint
from time import sleep
print('-'*50)
print('Jogo da Adivinhação')
print('-'*50)

sleep(2)
numSort = randint(0,50)
print('Sorteando o número de 0 a 50...')
sleep(2)
print(numSort) # Usei hack kkk, só para testar o acerto de primeira
num = int(input('Qual número foi sorteado? -> '))
tentativas = 0
while num != numSort:
    tentativas += 1
    if num > numSort:
        print('Menor!')
    elif num < numSort:
        print('Maior!')
    num = int(input('Qual número foi sorteado? -> '))
tentativas += 1

if tentativas == 1:
    print('Acertou de primeira!!!!!!!!!!!!')
else:
    print(f'Número Correto!\nVocê precisou de {tentativas} tentativas para acertar!')  # Creio que há alternativas melhores ao invés de fazer dois if's, corrigirei assim que possível.


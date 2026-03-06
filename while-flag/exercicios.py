# 1 - Programa irá ler valores do teclado, irá parar somente se digitar 999 (flag), logo deverá mostrar quantos numeros foram digitados e a soma entre eles (desconsiderar flag)

# soma = numeros = 0
# while True:
#     n = int(input('Digite um número -> '))
#     if n == 999:
#         break
#     soma += n
#     numeros += 1

# print(f'A soma dos numeros digitados foi {soma}, foram digitados {numeros} numeros.')

#2 - Tabuada do valor digitado pelo usuário, com a flag sendo um número negativo

# while True:
#     escolha = int(input('Qual número quer ver a tabuada? -> '))
#     if escolha < 0:
#         print('Programa encerrado.')
#         break
#     print('-'*50)
#     for i in range(11):
#         print(f'{escolha} x {i} = {escolha*i}')
#     print('-'*50)

#3 Jogo de par ou ímpar
# from random import randint

# print('-='*50)
# print('Jogão de Par ou Ímpar')
# print('-='*50)

# wins = 0
# while True:
#     numPlayer = int(input('Digite um número -> '))
#     escolha = str(input('O que acha que vai dar? (I para Ímpar ou P para Par) -> ')).upper()
#     numCpu = randint(0,100)
#     soma = numPlayer + numCpu
#     print('-'*70)
#     if soma % 2 == 0:
#         print(f'Você escolheu {numPlayer}, e o computador escolheu {numCpu}. Total de {soma} é um número PAR')
#     else:
#         print(f'Você escolheu {numPlayer}, e o computador escolheu {numCpu}. Total de {soma} é um número ÍMPAR')
#     print('-'*70)
#     if soma % 2 == 0 and escolha == 'P':
#         print('Você VENCEU! Vamos jogar novamente!')
#         wins += 1
#     elif soma % 2 != 0 and escolha == 'I':
#         print('Você VENCEU! Vamos jogar novamente!')
#         wins += 1
#     else:
#         print(f'Você perdeu! Ganhou {wins} vezes')
#         break
#     print('-'*50)
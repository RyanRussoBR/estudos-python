# 1 Contador Simples - Mostrar numeros de 0 a 10 na tela:

# n = 0
# while n < 11:
#     print(n)
#     n += 1

# 2 Pedir números infinitamente, na qual somente o 0 irá parar o looping, e todos os números irão somar, ao final do código mostrada a soma

# soma = 0
# num = int(input('Qual número escolhe? -> '))
# soma += num
# while num != 0:
#     num = int(input('Qual número escolhe? -> '))
#     soma += num
# print(f'A soma dos números digitados foi {soma}')

#3  Usuário digitará varios números, e se o mesmo quiser parar digitando N, irá mostrar o maior e menor número digitado pelo usuário.

# maior = 0
# menor = 0
# escolha = ''
# while escolha != 'N':
#     num = int(input('Digite um número: '))
#     if maior == 0 and menor == 0:
#         maior = num
#         menor = num

#     if num > maior:
#         maior = num
#     if num < menor:
#         menor = num

#     escolha = str(input('Quer continuar? (S/N) -> ')).upper()
#     while escolha != 'N' and escolha != 'S': # Adicionado um verificador para que o usuário não quebre o programa
#         escolha = str(input('Código inválido, digite S para Continuar, ou N para Não Continuar. -> ')).upper()  
# print('-'*30)
# print(f'O maior número digitado foi: {maior}\nJá o menor número digitado foi: {menor}')
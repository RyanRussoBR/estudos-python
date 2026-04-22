# Questões de Lógica de Programação para Prática

## 1. Imprimir números de 1 a 10
# Escreva um programa que imprima os números de 1 a 10 usando um loop.
# for i in range(1,11):
#     print(i, end=' -> ')
# print('FIM')

## 2. Soma dos primeiros 10 números naturais
# Calcule e imprima a soma dos números de 1 a 10.
# soma = 0
# for i in range(1,11): # Com o 1 antes do ,11 fica melhor
#     soma += i
# print(soma) 

## 3. Verificar se um número é par ou ímpar
# Peça ao usuário um número e diga se é par ou ímpar.
# num = int(input('Digite um número ->'))
# print('Par' if num % 2 == 0 else 'Ímpar') # Questão de output, nada grave

## 4. Fatorial de um número
# Calcule o fatorial de um número fornecido pelo usuário.
# fat = int(input('Qual número quer a fatorial? -> '))
# res = 1
# for i in range(fat, 0, -1):
#     res *= i
# print(res)

## 5. Sequência de Fibonacci
# Gere os primeiros 10 termos da sequência de Fibonacci.
# for i in range(8):
#     if i == 0:
#         num1 = 0
#         num2 = 1
#         print(f'{num1} -> {num2}')
#     next = num1 + num2
#     print(next, end=' -> ')
#     num1 = num2
#     num2 = next
# print('FIM')

# Versão corrigida:
# num1, num2 = 0, 1

# for i in range(10):
#     print(num1, end=' -> ')
#     num1, num2 = num2, num1 + num2

# print('FIM')


## 6. Inverter uma string
# Peça uma string ao usuário e imprima ela invertida.
# texto = input('Qual palavra inverter -> ')
# print(texto[::-1])
# Mesma ideia da 7


## 7. Verificar se uma string é palíndromo
# Verifique se uma string fornecida é um palíndromo (lê-se igual de trás para frente).
# texto = input('Palavra -> ')
# print('É palíndromo' if texto == texto[::-1] else 'Nâo é palíndromo' )
# Mudei nome de variáveis pra evitar alguns erros e ser mais profissional 

## 8. Encontrar o maior número em uma lista
# Dada uma lista de números, encontre e imprima o maior.
# lista = [1,8,34,2,4]
# print(max(lista)) # Versão mais rapidinha

# TEm essa tambem
# lista = [1,8,34,2,4]
# maior = lista[0]
# for i in lista:
#     if i > maior:
#         maior = i

# print(maior)

## 9. Contar vogais em uma string
# Conte quantas vogais (a, e, i, o, u) há em uma string fornecida.
# palavra = input('Palavra -> ').lower()
# vogais = 'aeiou'
# contVogais = 0
# for i in palavra:
#     if i in vogais:
#         contVogais += 1

# print(f'Essa palavra tem {contVogais} vogais')

## 10. Calculadora simples
# Crie uma calculadora que faça operações básicas (+, -, *, /) com dois números fornecidos pelo usuário.

# num1 = int(input('Digite um número: '))
# num2 = int(input('Digite um número: '))
# conta = int(input('Qual conta fazer? 1.soma 2.subtração 3.mult 4.div -> '))
# if conta == 1:
#     print(num1 + num2)
# elif conta == 2:
#     print(num1 - num2)
# elif conta == 3:
#     print(num1 * num2)
# elif conta == 4:
#     if num2 != 0:
#         print(num1/num2)
#     else:
#         print('Erro, divisão por zero.') # ESqueci de fazer essa parte.
# else:
#     print('Comando inválido')
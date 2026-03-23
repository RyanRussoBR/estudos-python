# Estruturas de Condição

# Aqui usa-se o operador if, para verificar se uma expressão lógica está correta para executar um bloco de código.
# E dependendo da para usar o else, se o if for falso, o bloco de código que estiver no else irá executar.
# E o elif, um outro operador, é quando o código precisa somente de uma verificação, sem precisar verificar toods, isso evita lentidão em um sistema ao meu ver.

# saldo = 2000.0
# saque = float(input('Informe o valor do saque: R$'))

# if saldo >= saque:
#     print('Realizando o saque...')
# else:
#     print('Saldo insuficiente.')

# opcao = int(input('Informe a opção que deseja [1]Sacar\n[2]Extrato'))

# #Com elif
# if opcao == 1:
#     valor = float(input('Informe o valor do saque: R$'))
# elif opcao == 2:
#     print('Exibindo o extrato')
# else:
#     print('Opção inválida')

# IDADE_ESPECIAL = 17
# MAIOR_IDADE = 18
# idade = int(input("Quantos aninhos voce tem?teré téu téu -> "))
# if idade >= MAIOR_IDADE:
#     print('CNH liberada meu nobre.')
# elif idade == IDADE_ESPECIAL:
#     print('Pode fazer umas aulinhas ai, até dirigir, mas nada de ir na rua heheh.')
# else:
#     print('Menor de idade, não pode ter CNH.')


# Estruturas de Repetição
# Temos o operador for, ele é excelente para quando temos um controle definido da repetição, ele geralmente percorre o que está atribuido a uma variável ou a um range definido, tem como colocar o else no final para fazer algo, fica melhor para ler, mais profissional digamos...

# Já o for com o built-in range, ao invés de colocar uma variável para percorrer, dá para colocar o numero de vezes que irá percorrer

# Já o operador while é para executar várias vezes ou até uma lógica ser concretizada geralmente usa um controlador, desavantagem que tem em relação ao seu irmão for.

# Aqui existe tanto o break, que interrompe um laço de repetiçao, funciona tanto no for quanto no while, e o continue, que ele simplesmente ignora algum bloco de código, se for uma condicional, ele pode ignorar (no print) se for uma sequencia.

# texto = input('Informe um texto -> ')
# VOGAIS = 'AEIOU'
# for i, letra in enumerate(texto):
#     if letra.upper() in VOGAIS:
#         print(f'Letra {i} -> {letra}')
# Lá vai o ryanzao curioso pegando função kkkkkk

# for i in range(1, 11):
#     print(i, end=" -> ")

# print('FIM')

# escolha = -1
# while True: #Mais comum
#     escolha = int(input('Informe a opção que deseja\n[1]Sacar\n[2]Extrato\n->'))
#     if escolha == 1:
#         print('Valor sacado')
#     elif escolha == 2:
#         print('Imprimindo extrato')
#     elif escolha == 10:
#         print('Cara me encerrou que vacilo bua bua')
#         break

# Entendo as transações da conta. BLOCO 1
# class Conta:
#     def __init__(self):
#         self.saldo = 0
    
#     def sacar(self, valor):
#         valor = float(input('Qual valor sacar? -> R$'))
#         if valor <= self.saldo:
#             self.saldo -= valor
#         else:
#             print('Saldo insuficiente.')
        
#     def depositar(self, valor):
#         valor = float(input('Qual valor depositar? -> R$'))
#         self.saldo += valor

#     def __str__(self):
#         return f"{self.saldo}"

# conta = Conta()
# conta.depositar(1)
# conta.sacar(1)
# print(conta)

# Jeito um pouco diferente, mas gosto de interatividade com o usuário :)

# BLOCO 2 - Histórico de transações.
# class Conta:
#     def __init__(self):
#         self.saldo = 0
    
#     def sacar(self, valor):
#         valor = float(input('Qual valor sacar? -> R$'))
#         if valor <= self.saldo:
#             self.saldo -= valor
#         else:
#             print('Saldo insuficiente.')
        
#     def depositar(self, valor):
#         valor = float(input('Qual valor depositar? -> R$'))
#         self.saldo += valor

#     def __str__(self):
#         return f"{self.saldo}"
    
# class Historico:
#     def __init__(self):
#         self.transacoes = []

#     def adicionar(self, transacao):
#         self.transacoes.append({
#             "tipo": transacao.__class__.__name__,
#             "valor": transacao.valor
#         })
    
#     def __str__(self):
#         return f"{self.transacoes}"
    
# class Deposito:
#     def __init__(self, valor):
#         self.valor = valor
#         pass
    

# class Saque:
#     def __init__(self, valor):
#         self.valor = valor
#         pass

# historico = Historico()
# s = Saque(100)
# d = Deposito(100)
# # conta = Conta()
# # conta.depositar(1)
# # historico.adicionar()
# # conta.sacar(1)
# # historico.adicionar()
# # print(conta)
# # print(historico)
# historico.adicionar(d)
# historico.adicionar(s)
# print(historico)

# As classes Deposito e Saque são feitas para representar o tipo e o valor feito na operação realizada pelo usuário.


#Aplicando interatividade com o usuário e finalização do bloco 3
class Conta:
    def __init__(self):
        self.saldo = 0
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            print('Saldo insuficiente.')
            return False
        
    def depositar(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"{self.saldo}"
    
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor
        })
    
    def __str__(self):
        texto = ''
        for t in self.transacoes:
            texto += f"Operação: {t['tipo']} -> R${t['valor']}\n"

        return texto if texto else 'Não houve transações'
    
class Deposito:
    def __init__(self, valor):
        self.valor = valor
        pass
    

class Saque:
    def __init__(self, valor):
        self.valor = valor
        pass

def menu():
    print('0. Sair\n1. Saque\n2. Depósito')

def main():
    historico = Historico()
    contateste = Conta()
    while True:
        menu()
        opcao = int(input('Qual opção escolher? -> '))

        if opcao == 0:
            break

        elif opcao == 1:
            valor = float(input('Qual valor sacar? -> R$'))
            operacao_realizada = contateste.sacar(valor)
            if operacao_realizada:
                s = Saque(valor)
                historico.adicionar(s)


        elif opcao == 2:
            valor = float(input('Qual valor depositar?-> R$'))
            contateste.depositar(valor)
            d = Deposito(valor)
            historico.adicionar(d)
        else:
            print('Nem existe esse comando parça')
        print(f"R${contateste}")
        print(historico)

main()
        
# O encapsulamento é o agrupamento de dados e métodos afim de proteger a manipulação errada de variáveis que podem comprometer gravemente o código, deixa o código mais seguro.
# Com isso, temos modificadores de acesso, como python não tem recursos para definir o nível de acesso como java e c++, temos convenções para definir recuros públicos e privados.
# Público: Pode ser acessado fora da classe
# Privado: Pode ser acessado somente dentro da classe

# class Conta:
#     def __init__(self, nro_agencia, saldo=0):
#         self._saldo = saldo
#         self.nro_agencia = nro_agencia
#     def depositar(self, valor):
#         self._saldo += valor

#     def sacar(self, valor):
#         self._saldo -= valor # perceba que estou acessando o valor do saldo somente no escopo da classe, que é o correto a se fazer

#     def mostrarSaldo(self):
#         return self._saldo

# conta = Conta("0001", 100)
# # print(conta._saldo) # Isso funciona, porém não é recomendado, pois o underline indica ser um recurso privado
# # conta._saldo += 100 # Isso também
# conta.depositar(100)
# print(conta.nro_agencia) # E aqui tenho os recursos públicos.

# print(conta.mostrarSaldo())


# Agora na questão do property, ele vem com o @ antes, e esse é o decorador, que o prof colocou antes de explicar sei la o porque mas tudo bem, spoilers né nenem.
# Mas ele é um decorador, fazendo que o método se comporte como um atributo na hora de chamá-lo no código, melhorando a fluidez do código   
# class Foo:
#     def __init__(self, x=None):
#         self._x = x
    
#     @property # agora fiz com que o método se comporte como atributo fora do código, não precisando do () no final.
#     def x(self):
#         return self._x or 0
    
#     @x.setter # Esse setter modifica o valor
#     def x(self, value):
#         self._x += value

#     @x.deleter # Esse bicho véio deleta, prof tentou explicar a importância mas sei la, desviou o assunto grrrr
#     def x(self):
#         self._x = -1

# foo = Foo(10)
# print(foo.x)

# foo.x = 10
# print(foo.x)

# del foo.x
# print(foo.x)


# class Pessoa:
#     def __init__(self, nome, ano_nascimento):
#         self.nome = nome
#         self._ano_de_nascimento = ano_nascimento

#     @property
#     def idade(self):
#         ano_atual = 2026
#         return ano_atual - self._ano_de_nascimento
    
# pessoa = Pessoa("Ryan", 2005)

# print(f'Nome: {pessoa.nome}\t idade:{pessoa.idade}')

# Achei que nesse modo ficou mais fluido o código, por isso a importância do encapsulamento.
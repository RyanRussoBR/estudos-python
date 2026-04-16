# Para começar temos os atributos de classe, que são atributos que podem ser compartilhados com outras variáveis
# # Já os atributos de instância são atributos específicos de uma variável, que é atribuido, geralmente está depois da definição de classe.

# class Estudante:
#     escola = "DIO" # Já este é a variável de classe, é a característica que vai ser compartilhada com todos os objetos

#     def __init__(self, nome, matricula):
#         self.nome = nome
#         self.matricula = matricula # Aqui encontram-se as variáveis de instância, pois possuem somente uma cópia para um objeto, este tendo suas próprias características

#     def __str__(self):
#         return f"{self.nome} - {self.matricula} - {self.escola}"


# aluno1 = Estudante('ryan', 1)
# aluno2 = Estudante('Shaolin', 2)


# print(aluno1)
# print(aluno2)
# Estudante.escola = 'Missa de sétimo dia do porco mono bola'
# aluno1.matricula = 69
# aluno2.escola = 'Retroescavadeira'
# Estudante.nome = 'Ihhh la ele' # Se tentar fazer isso, não vai fazer nada, porque não tem como alterar uma variável de instância, ele só cria um atributo de classe, mas como ja tem um self.nome, vai acontecer nada no output
# print(aluno1)
# print(aluno2)

# class Pessoa:
#     def __init__(self, nome= None, idade=None):
#         self.nome = nome
#         self.idade = idade

#     @classmethod
#     def criar_partir_datanasc(cls, ano, mes, dia, nome): # quando é método de classe, a convenção é colocar cls no lugar de self
#         idade = 2026 - ano
#         return cls(nome, idade)  

#     @staticmethod
#     def e_maior_idade(idade):
#         return idade >= 18
    
# # p = Pessoa('ryan', 20)

# # print(p.nome, p.idade)

# p = Pessoa.criar_partir_datanasc(2005,12,28, 'ryan')

# print(p.nome, p.idade)

# print(Pessoa.e_maior_idade(17))
# print(Pessoa.e_maior_idade(19))

# #Método da classe necessita do contexto da classe, já os métodos estáticos não necessita diretamente.

# Interface, ou contrato em python, é uma definição do que o método deve fazer, não como.

#CLASSES ABSTRATAS
# São classes que não podem ser instanciadas, servem como molde para outras classes, ou seja, voce pode herdar coisas dela, mas não criar um objeto de classe abstrata

# from abc import ABC, abstractmethod

# class ControleRemoto(ABC):

#     @abstractmethod
#     def ligar(self):
#         pass

#     @abstractmethod
#     def desligar(self):
#         pass 
#     pass

#     @property
#     @abstractmethod
#     def marca(self):
#         pass

# class controleTV(ControleRemoto):
#     def ligar(self):
#         print('Ligando a tv')
#         print('tv ligada')

#     def desligar(self):
#         print('desligando a tv')
#         print('tv desligada')

#     @property
#     def marca(self):
#         print('Marca: Philips')


# class ControleAr(ControleRemoto):
#     def ligar(self):
#         print('Ligando o ar cond')
#         print('ar cond ligada')

#     def desligar(self):
#         print('desligando o ar cond')
#         print('ar cond desligado')

#     @property
#     def marca(self):
#         print('Marca: LG')


# controle = controleTV() #TypeError: Can't instantiate abstract class controleTV with abstract methods desligar, ligar, nao posso instanciar pois tenho de implementar esses dois métodos    
# controle.ligar() 
# controle.desligar()

# controle2 = ControleAr()

# Importante para não haver erros graves no desenvolvimento de algum código.
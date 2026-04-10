# Para começar tem todo o conceito de Paradigma de Programação, que é nada mais que um estilo de programar que foca na resolução de problemas. Dependendo da estrutura e como vai fazer essa solução.
# Alguns paradigmas
# Imperativo ou procedual
# Funcional
# Orientado a eventos (o que vai mais ser focado.)

# A orientação a objetos é nada mais que um paradigma, um dos mais utilizados na área por sua flexibilidade tornando o código mais modular e extensível, ou seja, o sistema é dividido em partes menores que fica com um entendimento melhor.
# Aqui vou trabalhar comn dois conceitos importantes para esse paradigma, que é as classes e objetos.

# A classe é o que define os comportamentos (métodos) e características (atributos) de um objeto, como não conseguimos usá-los diretamente, pois a função dele é só definições temos:
# O objeto, que é o que usaremos, pois ele carrega o que foi definido pelas classes para usarmos.

# Estrutura classe:
# class Cachorro:
#     def __init__(self, nome, cor, acordado = True):
#         self.nome = nome
#         self.cor = cor
#         self.acordado = acordado

#     def latir(self):
#         print("Auuuuu")
    
#     def dormir(self):
#         self.acordado = False
#         print('Zzzzz...')

# # Estrutura objeto:
# cao1 = Cachorro("shaolin matador de porco", "preto", False)
# cao2 = Cachorro("negão", "branco")

# cao1.latir()

# print(cao2.acordado)
# cao2.dormir()
# print(cao2.acordado)

# self significa que é a instância do objeto, a referência direta ao objeto.


# Também em poo tem os construtores e destrutores
# O método construtor é quando uma nova instância é criada, geralmente é descrito como __init__. É feito para inicializar o estado de um objeto. Também pode ser chamado como método inicializador (achei maneirinho esse outro nome)
# Já o destrutor é o que faz um estado de um objeto seja destruído (meio assustador kkkkk). Não é muito utilizado em Python pois ele tem um coletor de lixo automático. É representado como __del__

class Cachorro:
    def __init__(self, nome, cor, idade, acordado = True):
        print('Inicializando a instância')
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.acordado = acordado
    
    def __del__(self):
        print("removendo instância")

    def falar(self):
        print("auuauauau")


# def criar_dog():
#     c = Cachorro("sei la", "colorido", 11)
#     print(c.nome)

c = Cachorro("Negão", 'caramelo', 15)
c.falar()
print('sei la')
del c
print('sei la')
print('sei la')
print('sei la')
print('sei la')
print('sei la')

# criar_dog()

# Quando o del está dentro da classe, ele irá ser executado quando todos os objetos forem chamados e executados, mas para forçar a execução antes é só usar o del
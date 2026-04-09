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

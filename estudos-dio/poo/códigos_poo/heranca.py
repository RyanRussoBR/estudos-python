# Herança Simples
# class Veiculos:
#     def __init__(self, cor, placa, numero_rodas):
#         self.cor = cor
#         self.placa = placa
#         self.numero_rodas = numero_rodas

#     def ligar_motor(self):
#         print("ligando o motor")
    
#     def __str__(self):
#         return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

# class Motocicleta(Veiculos):
#     pass

# class Caminhao(Veiculos):
#     def __init__(self, cor, placa, numero_rodas, carregado):
#         super().__init__(cor, placa, numero_rodas) # Método bacana para evitar de repetir a implementação
#         self.carregado = carregado

#     def esta_carregado(self):
#         print(f"{'Sim, tá carregado' if self.carregado else 'Não estou carregado'}")

#     def tombar(self):
#         print('Parou para descansar') # Quando coloco um método específico em uma classe filha, ela não influencia nas demais

# class Carro(Veiculos):
#     pass


# moto = Motocicleta('amarelo', '98-shaolin', 2)
# moto.ligar_motor()

# # carro = Carro("colorido", "jb-2222", 4)
# caminhao = Caminhao("vinho", 'diesel-69', 8, True)
# print(caminhao)
# # carro.ligar_motor()

# # caminhao.ligar_motor()
# # caminhao.tombar()
# # caminhao.esta_carregado()


# Herança Múltipla

class Animalia:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Mamiferos(Animalia):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Aves(Animalia):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class falarkapakapa:
    def falaroi(self):
        return 'Six seven haushudahsushu'

class Cachorro(Mamiferos):
    pass    

class Gato(Mamiferos):
    pass

class leão_gilbertobarros(Mamiferos):
    pass

class ornitorrinco(Mamiferos, Aves, falarkapakapa):
    pass

class galinha(Aves):
    pass

gato = Gato(nro_patas=4, cor_pelo='colorido')
print(gato) 

ornitorrinco = ornitorrinco(nro_patas=2, cor_pelo='marrom', cor_bico='rosa')
print(ornitorrinco)
print(ornitorrinco.falaroi())

# O comportamento da herança múltipla começa a ficar bem confusa, até o python se perde kkkkkkkkkkkkkkkk
# E um detalhe, o python usa o MRO (method resolution order), na qual ele faz uma ordem de precedencia de execução, no caso das heranças, ele sempre executa primeiro a classe filha até achar o str.
# Por ser complexo, tenho que tomar cuidado e cautela quando for usar isso. Me confundi bastante, sorte que to num bom dia, não me perdi tanto na explicação
# E para fehcar fiz ali uma classe nova para dar uma funcionalidade a uma classe filha, não interfere muito por ser uma funcionalidade, não implementação de característica.
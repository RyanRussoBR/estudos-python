# João tem uma bicicletaria e gostaria de registrar as vendas de suas  bicicletas. Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode buzinar, parar e correr.
from time import sleep
from playsound import playsound

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def correr(self):
        print("Zuuuummmmmm *correndo muuuuito*")
    
    def parar(self):
        print("Freando a bicicleta...")
        sleep(3)
        print('Bicileta parada.')
    
    def buzina(self):
        playsound(r'C:\Users\GAMER\Documents\GitHub\estudos-python\estudos-dio\poo\programa\buzina.mp3')

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}" # Código bem importante para ganhar tempo :P

bicicleta1 = Bicicleta("branca", "bmx", 1994, 500)

print(bicicleta1)
bicicleta1.parar()

print(bicicleta1.cor, bicicleta1.modelo)
# Bicicleta.buzina(bicicleta1) Outra forma de chamar uma função
bicicleta1.buzina()
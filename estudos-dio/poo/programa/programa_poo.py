# João tem uma bicicletaria e gostaria de registrar as vendas de suas  bicicletas. Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode buzinar, parar e correr.
from time import sleep
from playsound import playsound

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, buzina = False, correr = False, parar = True):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.correr = correr
        self.parar = parar
        self.buzina = buzina

    def correr(self):
        self.parar = False
        self.correr = True
        print("Zuuuummmmmm *correndo muuuuito*")
    
    def parar(self):
        self.parar = True
        print("Freando a bicicleta...")
        sleep(3)
        self.correr = False
        print('Bicileta parada.')
    
    def bibi(self):
        self.buzina = True
        playsound('buzina.mp3')

bicicleta1 = Bicicleta("branca", "bmx", "1994", 500)

bicicleta1.bibi()
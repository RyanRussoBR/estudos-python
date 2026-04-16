# Conceito de poliformismo: é quando uma função ou operação pode ser feita de tipos diferentes, tendo cada tipo uma resposta diferente, como o len("python") e len([10,2]), um conta caracteres (string) e outro conta elementos

# Polimorfismo com Herança: Na herança, a classe filha herda métodos da classe pai, porém, quando algum método não se encaixa na classe filha, podemos fazer a modificação do método diretamente na classe filha.

# class Passaro:
#     def voar(self): pass

# class Pardal(Passaro):
#     def voar(self):
#         print("Voando...")

# class Avestruz(Passaro):
#     def voar(self):
#         print(f"Avestruz não voa")

# def plano_voo(passaro):
#     passaro.voar() # Nesta função, o parâmetro (passaro) não depende do tipo específico do objeto, ele somente se importa se o objeto chamado possui a função voar. Isso que faz o polimorfismo, é um mesmo método que dois objetos utilizam. Ou melhor, são duas implementações diferentes, com a mesma chamada, no caso ali o .voar

# plano_voo(Pardal())
# plano_voo(Avestruz())


# Observação importante: O polimorfismo não depende 100% da herança, mas pode esperar bastante polimorfismo vindo com herança!!!!!!!!!!!!!!!!!!

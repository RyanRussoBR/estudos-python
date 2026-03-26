# Dicionários em Python
# O conceito de dicionário é um conjunto de pares não ordenados, tendo sempre chave (sendo essa objeto imutável), e o valor (sendo qualquer tipo de objeto.)
# Para declarar um dicionário, tenho que usar chaves, ou o dict
pessoa = {"nome": "Ryan", "idade": 20}
pessoa = dict(nome= "Ryan", idade=20)
# Para adicionar uma chave no dicionario, uso colchetes e dentro a chave que quero criar, e atribuindo o valor que quero deixar nessa chave
pessoa["telefone"] = 3300-9833

# O Python permite fazer dicionários aninhados, ou seja, dicionário dentro de outros dicionários
pessoa_completa = {
    "nome": "Ryan",
    "idade": 20,
    "contato": {
        "email": "ryan@email.com",
        "telefone": "3300-9833",
        "redes_sociais": {
            "instagram": "@ryan",
            "github": "RyanRussoBR"
        }
    },
    "endereco": {
        "cidade": "Curitiba",
        "estado": "PR",
    }
}
teste = pessoa_completa["contato"]["email"]
print(teste)

for chave, valor in pessoa_completa.items():
    print(chave, valor)

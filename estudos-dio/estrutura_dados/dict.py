# # Dicionários em Python
# # O conceito de dicionário é um conjunto de pares não ordenados, tendo sempre chave (sendo essa objeto imutável), e o valor (sendo qualquer tipo de objeto.)
# # Para declarar um dicionário, tenho que usar chaves, ou o dict
# # pessoa = {"nome": "Ryan", "idade": 20}
# # pessoa = dict(nome= "Ryan", idade=20)
# # # Para adicionar uma chave no dicionario, uso colchetes e dentro a chave que quero criar, e atribuindo o valor que quero deixar nessa chave
# # pessoa["telefone"] = 3300-9833

# # # O Python permite fazer dicionários aninhados, ou seja, dicionário dentro de outros dicionários
# # pessoa_completa = {
# #     "nome": "Ryan",
# #     "idade": 20,
# #     "contato": {
# #         "email": "ryan@email.com",
# #         "telefone": "3300-9833",
# #         "redes_sociais": {
# #             "instagram": "@ryan",
# #             "github": "RyanRussoBR"
# #         }
# #     },
# #     "endereco": {
# #         "cidade": "Curitiba",
# #         "estado": "PR",
# #     }
# # }
# # # Para acessar um elemento de um dicionário, deve-se fazer isso, porém ele somente acessa as chaves, jamais altera o nome da chave, mas sim do elemento
# # print(pessoa_completa["idade"])
# # pessoa_completa["idade"] = 52
# # print(pessoa_completa)

# # Métodos da classe dict
# # Tem o método clear, ele limpa todos os elementos de um dicionário
# # O método fromkeys ele permite criar chaves com o mesmo valor

# pessoa_completa = {
#     "nome": "Ryan",
#     "idade": 20,
#     "contato": {
#         "email": "ryan@email.com",
#         "telefone": "3300-9833",
#         "redes_sociais": {
#             "instagram": "@ryan",
#             "github": "RyanRussoBR"
#         }
#     }
# }   

# Já o método copy é como se fosse um backup, ele cria uma cópia do dicionário que é atribuido o método, bom para alterar dados de um dicionário sem mudar o original.
# copia = pessoa_completa.copy()
# copia["nome"] = "Shaolin matador de porco"
# print(copia)
# print(pessoa_completa)


# print(pessoa_completa.get("jogos", "nao encontrado")) # O método get é bom para análises.

# # Tem o método pop, que remove elementos de uma chave de um dicionario
# print(pessoa_completa.pop("idade", "nao encontrado"))
# print(pessoa_completa)
# # Uma coisa que percebi é que no segundo argumento desses dois ultimos itens, da para colocar uma mensagem para caso o interpretador não encontre a chave indicada no método.

# # O método setdefault ele adiciona valor na chave se a mesma não existir, é como se verificasse sem precisar de if ou operador de associação
# pessoa_completa.setdefault("idade", 20)
# print(pessoa_completa)
# # Problema é que o valor adicionado vai pro final

# # Já o método update atualiza valores do dicionário, e também adiciona dicionário novo.

# # Método in também existe aqui, porém ele é uma forma mais elegante do setdefault
# print("idade" in pessoa_completa) 
# # Vejo como um algoritmo importante para autenticação de usuarios

# # O del, como o pop, tem a função de remover uma chave do dicionário

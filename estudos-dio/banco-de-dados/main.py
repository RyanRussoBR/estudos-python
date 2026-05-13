# Banco de Dados: São coleções organizadas de dados que podem ser acessadas e armazenadas por um sistema de computador
# Já o banco de dados relacionais é um tipo de banco que organiza os dados em forma de tabelas, contendo registros individuais armazenados em linhas, e campos de dados representados em colunas
# No banco de dados existe a chave primária, que no caso do exemplo do professor, nessa tabela o primeiro termo indica a chave primária, como o ID, que é um identificador de um usuário, um código que vai ser único para cada usuário na tabela, garantindo a unicidade e neutralização de riscos ao usuário.
# TODA TABELA TEM QUE TER UMA CHAVE PRIMÁRIA.

# Avançando nos conceitos, temos a chave estrageira, que indica a chave primária de uma outra tabela, por exemplo, em uma tabela Pedidos ter uma coluna chamada ClienteID, indicando a chave primária(ID) da tabela Clientes
# As relações podem ser "um para um", "um para muitos" e "muitos para muitos" (no caso desse último, cria-se uma tabela separada para relacionar tudo!!!!)

# Agora para fazer tudo isso, há a linguagem SQL (Structured Query Language), usada para interagir com banco de dados relacionais, podendo fazer operações como criar tabelas, inserir, deletar, atualizar registros, tambem podendo realizar consultas para buscar dados.

# Comandos SQL:
# CREATE: Cria alguma coisa
# INSERT: Comando para inserir, com o INTO, ele inlcui dados em uma tabela.
# SELECT * FROM: Faz com que liste todos os dados em uma tabela 
# UPDATE: Usado para como próprio nome sugere, atualizar um dado, exemplo : "UPDATE produtos SET (pra identificar qual linha quero modificar eu acho) nome='Curso de python para iniciantes' WHERE id = 1 (Aqui é sempre interessante identificar qual id está sendo atualizado.)"
# DELETE FROM: Usado para excluir dados, também sempre interessante usar o WHERE id=1 no final para identificar qual id terá seus dados excluidos.

# Vi no REDDIT, e confirmei no GPT uma coisa de suma importância, o ; no sql indica o fim de uma instrução, ou seja, isso é muito perigoso, principalmente a mim kkkk.  
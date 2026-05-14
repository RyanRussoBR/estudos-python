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

# Vou ver sobre Python DB API
# Para realizar uma conexão, é usado:
# import sqlite3
# con = sqlite3.connect('banco_dados.db') -> Daqui que vem o tão falado formato db, que o pessoal ignora no commit quando vai subir o projeto, para não expor o banco de dados de uma aplicação
# Para criar o arquivo db, é importante utilizar a biblioteca pathlib, importando o Path, pois ele permite trabalhar com caminhos de forma mais eficiente, tornando a execução do banco de dados mais flexível, evitando conflitos com caminhos
# Para realizar comandos com o sqlite, devemos definir o cursor, logo em seguida, com o método execute no cursor, é realizado os comandos no banco de dados.
# Para criar a tabela devemos fazer cursor.execute('CREATE TABLE lala(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100))') -> Quando é um dado que é uma string, importante colocar VARCHAR.
# nome = 'Ryan Lindo'
# Para inserir dados usa-se o cursor.execute('INSERT INTO lala(nome)' VALUES(?);' nome)
# Importante colocar aquela interrogação, para evitar o sql injection, método meio chato dos hacker ai
# Porque há pessoas que fazem concatenação, colocando f string no insert, e colocando {nome} no lugar da interrogação, fazendo com que a segurança do banco de dados fique comprometida.
# E para atualizar dados, é usado o método UPDATE, que vem acompanhado do SET nome_coluna = ? para indicar qual dado vai ser atualizado ou dados né :D, e o WHERE id = ?, para indicar qual usuário terá seus dados atualizados. 
import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

dados = sqlite3.connect(ROOT_PATH /'banco_dados.sqlite')
cursor = dados.cursor() 

def criar(dados):
    cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR (150))')
    dados.commit()

def inserir(dados, cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT clientes(nome, email) VALUES(?,?);', data)
    dados.commit()

def atualizar(dados, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE  clientes SET nome = ?, email = ? WHERE id = ?;', data)
    dados.commit()

def remover(dados, cursor, id):
    data = (id,) # Para passar uma tupla de unico valor, tem que colocar virgula
    cursor.execute('DELETE FROM clientes WHERE id = ?;', data)
    dados.commit()

def inserirMuitos(dados, cursor, infos):
    cursor.executemany("INSERT INTO clientes (nome,email) VALUES(?,?);", infos)
    dados.commit()

def consultar(cursor, id):
    cursor.row_factory = sqlite3.Row
    cursor.execute('SELECT * FROM clientes WHERE id = ?;', (id,))
    return cursor.fetchone()

def consultarBastante(cursor):
    return cursor.execute('SELECT * FROM clientes;')

clientes = consultarBastante(cursor)
for cliente in clientes:
    print(cliente)

cliente = consultar(cursor, 3)
print(dict(cliente))
print(cliente['nome'])
# print(cliente["nome"])

# infos = [
#     ('Outra pessoa', 'gg@gmail.com'),
#     ('Negão', 'g@gmail.com'),
#     ('Jeuy', '12@gmail.com'),
#     ('kkk', '55gmail.com'),
# ]

# inserirMuitos(dados, cursor, infos)


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


atualizar(dados, cursor, 'Ryan Bruto legalzão', 'ry@hotmail.com', 1)
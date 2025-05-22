import sqlite3
import os

# Caminho do banco de dados
DATABASE = os.path.join(os.path.dirname(__file__), 'banco.db')

# Conecta ao banco
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Lista de produtos para inserir
produtos = [
    ("LIVE BOX CAP-23",),
    ("BEAT BOX CAP-32",),
    ("DOUBLE BLACK CAP-34",),
    ("LUMI BOX CAP-38",),
    ("LIGHT BOX CAP-39",)
]

# Inserção
cursor.executemany("INSERT INTO produtos (nome) VALUES (?)", produtos)
conn.commit()
conn.close()

print("Produtos adicionados com sucesso!")

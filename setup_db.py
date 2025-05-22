import sqlite3
import os

DATABASE = os.path.join(os.path.dirname(__file__), 'banco.db')

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS respostas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        atendimento INTEGER,
        tempo INTEGER,
        satisfacao INTEGER,
        observacao TEXT,
        produto_id INTEGER,
        FOREIGN KEY(produto_id) REFERENCES produtos(id)
    )
    ''')

    conn.commit()
    conn.close()
    print("Banco e tabelas criados com sucesso!")

if __name__ == "__main__":
    init_db()

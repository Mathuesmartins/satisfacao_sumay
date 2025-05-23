from flask import Flask, render_template, request, redirect, flash, send_file, session, url_for
import sqlite3, os
import pandas as pd
from io import BytesIO

app = Flask(__name__)
app.secret_key = "chave_secreta"

DATABASE = os.path.join(os.path.dirname(__file__), 'banco.db')

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        atendimento = int(request.form['atendimento'])
        tempo = int(request.form['tempo'])
        satisfacao = int(request.form['satisfacao'])
        observacao = request.form['observacao']
        produto_id = int(request.form['produto'])

        cursor.execute('''
            INSERT INTO respostas (nome, email, atendimento, tempo, satisfacao, observacao, produto_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (nome, email, atendimento, tempo, satisfacao, observacao, produto_id))
        conn.commit()
        conn.close()

        flash("Resposta enviada com sucesso!", "success")
        return redirect("/")

    return render_template("form.html", produtos=produtos)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        if usuario == "sumay" and senha == "Sumay2025!":
            session["logado"] = True
            return redirect("/relatorio")
        else:
            flash("Usuário ou senha inválidos", "danger")
    return render_template("login.html")

@app.route("/relatorio")
def relatorio():
    if not session.get("logado"):
        return redirect(url_for("login"))

    conn = get_db()
    df = pd.read_sql_query("""
        SELECT respostas.*, produtos.nome AS produto_nome 
        FROM respostas
        JOIN produtos ON respostas.produto_id = produtos.id
    """, conn)

    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Respostas')

    output.seek(0)
    return send_file(output, download_name="relatorio.xlsx", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

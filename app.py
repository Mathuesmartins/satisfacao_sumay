from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import sqlite3, os

from google_sheets import adicionar_resposta_na_planilha

app = Flask(__name__)
app.secret_key = "chave_secreta"

# Configuração de e-mail (use credenciais corretas)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='sumaydobr@gmail.com',
    MAIL_PASSWORD='Sumay2025!',
)
mail = Mail(app)

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

        # Salvar também no Google Sheets
        adicionar_resposta_na_planilha([
            nome, email, atendimento, tempo, satisfacao, observacao, produto_id
        ])

        # E-mail de confirmação
        msg = Message("Confirmação de Pesquisa",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[email])
        msg.body = f"Olá {nome}, obrigado por responder nossa pesquisa!"
        mail.send(msg)

        flash("Resposta enviada com sucesso!", "success")
        return redirect("/")

    return render_template("form.html", produtos=produtos)

if __name__ == "__main__":
    app.run(debug=True)

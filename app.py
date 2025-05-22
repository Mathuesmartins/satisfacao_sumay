from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "chave_secreta"

# Configurar e-mail (adapte conforme seu provedor SMTP)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='seuemail@gmail.com',
    MAIL_PASSWORD='sua_senha',
)
mail = Mail(app)

# Caminho do banco SQLite
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

        msg = Message("Confirmação de Pesquisa de Satisfação",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[email])
        msg.body = f"Olá {nome},\n\nObrigado por responder nossa pesquisa!"
        mail.send(msg)

        flash("Resposta enviada com sucesso! Verifique seu e-mail.", "success")
        return redirect("/")

    return render_template("form.html", produtos=produtos)

if __name__ == "__main__":
    app.run(debug=True)

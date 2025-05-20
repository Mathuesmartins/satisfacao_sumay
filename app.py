from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
from config import Config
from models import db, Produto, Resposta

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = "chave_secreta"

db.init_app(app)
mail = Mail(app)

@app.route("/", methods=["GET", "POST"])
def index():
    produtos = Produto.query.all()
    if request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        atendimento = int(request.form['atendimento'])
        tempo = int(request.form['tempo'])
        satisfacao = int(request.form['satisfacao'])
        observacao = request.form['observacao']
        produto_id = int(request.form['produto'])

        resposta = Resposta(
            nome=nome,
            email=email,
            atendimento=atendimento,
            tempo=tempo,
            satisfacao=satisfacao,
            observacao=observacao,
            produto_id=produto_id
        )
        db.session.add(resposta)
        db.session.commit()

        # Enviar e-mail
        msg = Message("Confirmação de Pesquisa de Satisfação",
                      sender="seuemail@gmail.com",
                      recipients=[email])
        msg.body = f"Olá {nome},\n\nObrigado por responder nossa pesquisa!"
        mail.send(msg)

        flash("Resposta enviada com sucesso! Verifique seu e-mail.", "success")
        return redirect("/")
    return render_template("form.html", produtos=produtos)

if __name__ == "__main__":
    app.run(debug=True)

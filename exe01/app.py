from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("exercicio1.html")

@app.route("/submissao")
def submissao_formulario():
    nome = request.args.get('nome')
    email = request.args.get('email')
    assunto = request.args.get('assunto')
    mensagem = request.args.get('mensagem')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>email: {email}<br>assunto: {assunto}<br>mensagem: {mensagem}"
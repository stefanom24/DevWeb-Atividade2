from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("exercicio4.html")

@app.route("/submissao")
def submissao_formulario():
    nome = request.args.get('nome')
    email = request.args.get('email')
    numero = request.args.get('number')
    eventos = request.args.getlist('eventos')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>escolha: {email}<br>numero: {numero}<br>eventos escolhidos: {eventos}"
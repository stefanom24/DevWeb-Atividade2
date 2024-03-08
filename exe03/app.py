from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("exercicio3.html")

@app.route("/submissao")
def submissao_formulario():
    nome = request.args.get('nome')
    options = request.args.get('options')
    area = request.args.get('mensagem')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>escolha: {options}<br>mensagem: {area}"
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("exercicio5.html")

@app.route("/submissao")
def submissao_formulario():
    nome = request.args.get('nome')
    endereco = request.args.get('endereco')
    contato = request.args.get('contato')
    comidas = request.args.getlist('comidas')
    delivery = request.args.get('entrega')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>endereco: {endereco}<br>contato: {contato}<br>comidas escolhidos: {comidas}<br>entrega escolhida: {delivery}"
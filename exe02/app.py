from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("exercicio2.html")

@app.route("/submissao")
def submissao_formulario():
    email = request.args.get('email')
    options = request.args.get('options')
    
    return f"<h1>Sucesso!</h1><br>email: {email}<br>escolha: {options}"
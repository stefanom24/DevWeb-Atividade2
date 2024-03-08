from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index/voltar")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/index/exe01")
def exe01():
    return render_template("exe01.html")

@app.route("/exe01-result")
def submissao_formulario():
    nome = request.args.get('name')
    email = request.args.get('mail')
    checkin = request.args.get('in')
    checkout = request.args.get('out')
    numero = request.args.get('numero')
    quartos = request.args.get('quartos')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>endereco: {email}<br>contato: {checkin}<br>comidas escolhidos: {checkout}<br>entrega escolhida: {numero}<br>tipo de quarto escolhido: {quartos}"

@app.route("/index/exe02")
def exe02():
    return render_template("exe02.html")

@app.route("/exe02-result")
def submissao_formulario():
    nome = request.args.get('name')
    email = request.args.get('mail')
    checkin = request.args.get('in')
    checkout = request.args.get('out')
    numero = request.args.get('numero')
    quartos = request.args.get('quartos')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>endereco: {email}<br>contato: {checkin}<br>comidas escolhidos: {checkout}<br>entrega escolhida: {numero}<br>tipo de quarto escolhido: {quartos}"

@app.route("/index/exe03")
def exe03():
    return render_template("exe03.html")

@app.route("/exe03-result")
def submissao_formulario():
    nome = request.args.get('name')
    email = request.args.get('mail')
    checkin = request.args.get('in')
    checkout = request.args.get('out')
    numero = request.args.get('numero')
    quartos = request.args.get('quartos')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>endereco: {email}<br>contato: {checkin}<br>comidas escolhidos: {checkout}<br>entrega escolhida: {numero}<br>tipo de quarto escolhido: {quartos}"

@app.route("/index/exe04")
def exe04():
    return render_template("exe04.html")

@app.route("/exe04-result")
def submissao_formulario():
    nome = request.args.get('name')
    email = request.args.get('mail')
    checkin = request.args.get('in')
    checkout = request.args.get('out')
    numero = request.args.get('numero')
    quartos = request.args.get('quartos')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>endereco: {email}<br>contato: {checkin}<br>comidas escolhidos: {checkout}<br>entrega escolhida: {numero}<br>tipo de quarto escolhido: {quartos}"

@app.route("/index/exe05")
def exe05():
    return render_template("exe05.html")

@app.route("/exe05-result")
def submissao_formulario():
    nome = request.args.get('name')
    email = request.args.get('mail')
    checkin = request.args.get('in')
    checkout = request.args.get('out')
    numero = request.args.get('numero')
    quartos = request.args.get('quartos')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>endereco: {email}<br>contato: {checkin}<br>comidas escolhidos: {checkout}<br>entrega escolhida: {numero}<br>tipo de quarto escolhido: {quartos}"

@app.route("/index/exe06")
def exe06():
    return render_template("exe06.html")

@app.route("/exe06-result")
def submissao_formulario():
    nome = request.args.get('name')
    email = request.args.get('mail')
    checkin = request.args.get('in')
    checkout = request.args.get('out')
    numero = request.args.get('numero')
    quartos = request.args.get('quartos')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>endereco: {email}<br>contato: {checkin}<br>comidas escolhidos: {checkout}<br>entrega escolhida: {numero}<br>tipo de quarto escolhido: {quartos}"

@app.route("/index/exe07")
def exe07():
    return render_template("exe07.html")

@app.route("/exe07-result")
def submissao_formulario():
    nome = request.args.get('name')
    email = request.args.get('mail')
    checkin = request.args.get('in')
    checkout = request.args.get('out')
    numero = request.args.get('numero')
    quartos = request.args.get('quartos')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>endereco: {email}<br>contato: {checkin}<br>comidas escolhidos: {checkout}<br>entrega escolhida: {numero}<br>tipo de quarto escolhido: {quartos}"

@app.route("/index/exe08")
def exe08():
    return render_template("exe08.html")

@app.route("/exe08-result")
def submissao_formulario():
    nome = request.args.get('name')
    email = request.args.get('mail')
    checkin = request.args.get('in')
    checkout = request.args.get('out')
    numero = request.args.get('numero')
    quartos = request.args.get('quartos')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>endereco: {email}<br>contato: {checkin}<br>comidas escolhidos: {checkout}<br>entrega escolhida: {numero}<br>tipo de quarto escolhido: {quartos}"

@app.route("/index/exe09")
def exe09():
    return render_template("exe09.html")

@app.route("/exe09-result")
def submissao_formulario():
    nome = request.args.get('name')
    email = request.args.get('mail')
    checkin = request.args.get('in')
    checkout = request.args.get('out')
    numero = request.args.get('numero')
    quartos = request.args.get('quartos')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>endereco: {email}<br>contato: {checkin}<br>comidas escolhidos: {checkout}<br>entrega escolhida: {numero}<br>tipo de quarto escolhido: {quartos}"

@app.route("/index/exe10")
def exe10():
    return render_template("exe10.html")

@app.route("/exe10-result")
def submissao_formulario():
    nome = request.args.get('name')
    email = request.args.get('mail')
    checkin = request.args.get('in')
    checkout = request.args.get('out')
    numero = request.args.get('numero')
    quartos = request.args.get('quartos')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>endereco: {email}<br>contato: {checkin}<br>comidas escolhidos: {checkout}<br>entrega escolhida: {numero}<br>tipo de quarto escolhido: {quartos}"
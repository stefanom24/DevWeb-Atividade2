from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index/voltar")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/index/exe01")
def exe01():
    return render_template("exercicio1.html")

@app.route("/exe01-result")
def exe01_result():
    nome = request.args.get('nome')
    email = request.args.get('email')
    assunto = request.args.get('assunto')
    mensagem = request.args.get('mensagem')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>endereco: {email}<br>contato: {assunto}<br>comidas escolhidos: {mensagem}<br>"

@app.route("/index/exe02")
def exe02():
    return render_template("exercicio2.html")

@app.route("/exe02-result")
def exe02_result():
    email = request.args.get('email')
    options = request.args.get('options')
    
    return f"<h1>Sucesso!</h1><br>email: {email}<br>escolha: {options}"

@app.route("/index/exe03")
def exe03():
    return render_template("exercicio3.html")

@app.route("/exe03-result")
def exe03_result():
    nome = request.args.get('nome')
    options = request.args.get('options')
    area = request.args.get('mensagem')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>escolha: {options}<br>mensagem: {area}"

@app.route("/index/exe04")
def exe04():
    return render_template("exercicio4.html")

@app.route("/exe04-result")
def exe04_result():
    nome = request.args.get('nome')
    email = request.args.get('email')
    numero = request.args.get('number')
    eventos = request.args.getlist('eventos')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>escolha: {email}<br>numero: {numero}<br>eventos escolhidos: {eventos}"

@app.route("/index/exe05")
def exe05():
    return render_template("exercicio5.html")

@app.route("/exe05-result")
def exe05_result():
    nome = request.args.get('nome')
    endereco = request.args.get('endereco')
    contato = request.args.get('contato')
    comidas = request.args.getlist('comidas')
    delivery = request.args.get('entrega')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>endereco: {endereco}<br>contato: {contato}<br>comidas escolhidos: {comidas}<br>entrega escolhida: {delivery}"

@app.route("/index/exe06")
def exe06():
    return render_template("exe06.html")

@app.route("/exe06-result")
def exe06_result():
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
def exe07_result():
    nome = request.args.get('name')
    email = request.args.get('mail')
    checkin = request.args.get('in')
    checkout = request.args.get('out')
    numero = request.args.get('numero')
    quartos = request.args.get('quartos')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>endereco: {email}<br>contato: {checkin}<br>comidas escolhidos: {checkout}<br>entrega escolhida: {numero}<br>tipo de quarto escolhido: {quartos}"

@app.route("/index/exe08")
def exe08():
    return render_template("exercicio8.html")

@app.route("/exe08-result")
def exe08_result():
    nome = request.args.get('name')
    email = request.args.get('mail')
    checkin = request.args.get('in')
    checkout = request.args.get('out')
    numero = request.args.get('numero')
    quartos = request.args.get('quartos')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>endereco: {email}<br>contato: {checkin}<br>comidas escolhidos: {checkout}<br>entrega escolhida: {numero}<br>tipo de quarto escolhido: {quartos}"

@app.route("/index/exe09")
def exe09():
    return render_template("exercicio9.html")

@app.route("/exe09-result")
def exe09_result():
    nome = request.args.get('nome')
    email = request.args.get('email')
    area = request.args.get('area')
    disponibilidade = request.args.get('disponibilidade')
    hora = request.args.get('hora')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>endereco: {email}<br>contato: {area}<br>comidas escolhidos: {disponibilidade}<br>entrega escolhida: {hora}"

@app.route("/index/exe10")
def exe10():
    return render_template("exercicio10.html")

@app.route("/exe10-result")
def exe10_result():
    nome = request.args.get('name')
    telefone = request.args.get('telefone')
    email = request.args.get('email')
    educacao = request.args.get('educacao')
    futuro = request.args.get('futuro')
    
    return f"<h1>Sucesso!</h1><br>nome: {nome}<br>endereco: {email}<br>contato: {telefone}<br>comidas escolhidos: {educacao}<br>entrega escolhida: {futuro}"
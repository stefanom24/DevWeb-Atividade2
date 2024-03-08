from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    # Renderiza o formulário HTML
    return render_template("index.html")

@app.route("/input")
def input():
    # Renderiza o formulário HTML
    return render_template("input.html")

@app.route("/input-result")
def input_result():
    # Obtém os dados do formulário via método GET
    first_name = request.args.get('fname')
    last_name = request.args.get('lname')

    # Retorna uma resposta simples para o usuário
    return f"<h1>Submission Successful</h1><p>First name: {first_name}<br>Last name: {last_name}</p>"

@app.route("/radio")
def radio():
    # Renderiza o formulário HTML
    return render_template("radio.html")

@app.route('/radio-result', methods=['GET'])
def radio_result():
    # Obtendo o valor do botão de rádio selecionado
    favorite_language = request.args.get('fav_language')

    # Retornando uma resposta com a seleção
    return f'Sua linguagem web favorita é: {favorite_language}'

@app.route("/checkbox")
def checkbox():
    # Renderiza o formulário HTML
    return render_template("checkbox.html")

@app.route('/checkbox-result', methods=['GET'])
def checkbox_result():
    # Inicializando uma lista para armazenar as escolhas
    choices = []

    # Verificando quais checkboxes foram marcadas
    if request.args.get('vehicle1'):
        choices.append(request.args.get('vehicle1'))
    if request.args.get('vehicle2'):
        choices.append(request.args.get('vehicle2'))
    if request.args.get('vehicle3'):
        choices.append(request.args.get('vehicle3'))

    # Gerando uma string com as escolhas para exibição
    choices_str = ', '.join(choices) if choices else 'Nenhuma escolha feita'

    # Retornando as escolhas do usuário
    return f'Você selecionou: {choices_str}'


@app.route("/select")
def select():
    # Renderiza o formulário HTML
    return render_template("select.html")


@app.route('/select-result', methods=['GET'])
def select_result():
    # Obtém a marca de automóvel selecionada pelo usuário
    selected_car = request.args.get('cars')

    # Retornando uma resposta com a seleção do usuário
    return f'Sua marca de automóvel favorita é: {selected_car}'

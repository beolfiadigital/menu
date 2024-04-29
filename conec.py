from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    # Aqui você pode processar os dados como desejar, por exemplo, salvar no banco de dados, etc.
    print(f"Novo cadastro recebido:\nNome: {name}\nEmail: {email}")

    return "Cadastro recebido com sucesso!"

if __name__ == '__main__':
    # Executa o Flask para ser acessível em todas as interfaces de rede
    app.run(port=4444, debug=True)

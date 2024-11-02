from flask import Flask, make_response, jsonify, request
from scrapp.prod import producao

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/producao', methods=['GET'])
def get_producao():
    return make_response(
        jsonify(
            Mensagem='Produção de vinhos, sucos e derivados do Rio Grande do Sul',
            Dados=producao
        )
    )


@app.route('/producao', methods=['POST'])
def insert_producao():
    prod = request.json
    producao.append(prod)
    return make_response(
        jsonify(
            Mensagem='Produção cadastrada com sucesso.',
            Dados=prod
        )
    )


app.run()

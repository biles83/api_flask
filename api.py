from flask import Flask, make_response, jsonify, request
from scrapp.prod import producao
from scrapp.comercial import comercial

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# ----------------------------
# ROUTES -- Producao
# ----------------------------


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

# ----------------------------
# ROUTES -- Comercializacao
# ----------------------------


@app.route('/comercial', methods=['GET'])
def get_comercial():
    return make_response(
        jsonify(
            Mensagem='Comercialização de vinhos e derivados no Rio Grande do Sul',
            Dados=comercial
        )
    )


@app.route('/comercial', methods=['POST'])
def insert_comercial():
    comerc = request.json
    comercial.append(comerc)
    return make_response(
        jsonify(
            Mensagem='Comercialização cadastrada com sucesso.',
            Dados=comerc
        )
    )


app.run()

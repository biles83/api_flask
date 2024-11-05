from flask import Flask, make_response, jsonify, request
from services.prod import producao
from services.processada import processada
from services.comercial import comercial
from services.importacao import importacao
from services.exportacao import exportacao
from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
app.config['JSON_SORT_KEYS'] = False

# ----------------------------
# Autenticação Simples
# ----------------------------

auth = HTTPBasicAuth()
USER_DATA = {
    "Username": "password"
}


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password


class endpoint(Resource):
    @auth.login_required
    def get(self):
        return jsonify({"status": True})


api.add_resource(endpoint, "/")

# ----------------------------
# ROUTES -- Producao
# ----------------------------


@app.route('/producao', methods=['GET'])
@auth.login_required
def get_producao():
    return make_response(
        jsonify(
            Mensagem='Produção de vinhos, sucos e derivados do Rio Grande do Sul.',
            Dados=producao
        )
    )


@app.route('/producao', methods=['POST'])
@auth.login_required
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
@auth.login_required
def get_comercial():
    return make_response(
        jsonify(
            Mensagem='Comercialização de vinhos e derivados no Rio Grande do Sul.',
            Dados=comercial
        )
    )


@app.route('/comercial', methods=['POST'])
@auth.login_required
def insert_comercial():
    comerc = request.json
    comercial.append(comerc)
    return make_response(
        jsonify(
            Mensagem='Comercialização cadastrada com sucesso.',
            Dados=comerc
        )
    )

# ----------------------------
# ROUTES -- Processamento
# ----------------------------


@app.route('/processamento', methods=['GET'])
@auth.login_required
def get_processa():
    return make_response(
        jsonify(
            Mensagem='Quantidade de uvas processadas no Rio Grande do Sul.',
            Dados=processada
        )
    )


@app.route('/processamento', methods=['POST'])
@auth.login_required
def insert_processa():
    process = request.json
    processada.append(process)
    return make_response(
        jsonify(
            Mensagem='Processamento cadastrado com sucesso.',
            Dados=process
        )
    )


# ----------------------------
# ROUTES -- Importacao
# ----------------------------


@app.route('/importacao', methods=['GET'])
@auth.login_required
def get_importa():
    return make_response(
        jsonify(
            Mensagem='Importação de derivados de uva.',
            Dados=importacao
        )
    )


@app.route('/importacao', methods=['POST'])
@auth.login_required
def insert_importa():
    importa = request.json
    importacao.append(importa)
    return make_response(
        jsonify(
            Mensagem='Importacao cadastrada com sucesso.',
            Dados=importa
        )
    )

# ----------------------------
# ROUTES -- Exportacao
# ----------------------------


@app.route('/exportacao', methods=['GET'])
@auth.login_required
def get_exporta():
    return make_response(
        jsonify(
            Mensagem='Exportação de derivados de uva.',
            Dados=exportacao
        )
    )


@app.route('/exportacao', methods=['POST'])
@auth.login_required
def insert_exporta():
    exporta = request.json
    exportacao.append(exporta)
    return make_response(
        jsonify(
            Mensagem='Exportação cadastrada com sucesso.',
            Dados=exporta
        )
    )


if __name__ == "__main__":
    app.run(debug=True)

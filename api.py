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


@app.route('/producao/<int:item_id>', methods=['PUT'])
@auth.login_required
def update_producao(item_id):
    prod = request.get_json()
    if 0 <= item_id < len(producao):
        producao[item_id].update(prod)
        return make_response(
            jsonify(
                Mensagem='Produção alterada com sucesso.',
                Dados=producao[item_id]
            )
        )
    return jsonify({"error": "Item not found"}), 404


@app.route('/producao/<int:item_id>', methods=['DELETE'])
@auth.login_required
def delete_producao(item_id):
    if 0 <= item_id < len(producao):
        removed = producao.pop(item_id)
        return make_response(
            jsonify(
                Mensagem='Produção deletada com sucesso.',
                Dados=removed
            )
        )
    return jsonify({"error": "Item not found"}), 404


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


@app.route('/comercial/<int:item_id>', methods=['PUT'])
@auth.login_required
def update_comercial(item_id):
    comerc = request.get_json()
    if 0 <= item_id < len(comercial):
        comercial[item_id].update(comerc)
        return make_response(
            jsonify(
                Mensagem='Comercialização alterada com sucesso.',
                Dados=comercial[item_id]
            )
        )
    return jsonify({"error": "Item not found"}), 404


@app.route('/comercial/<int:item_id>', methods=['DELETE'])
@auth.login_required
def delete_comercial(item_id):
    if 0 <= item_id < len(comercial):
        removed = comercial.pop(item_id)
        return make_response(
            jsonify(
                Mensagem='Comercialização deletada com sucesso.',
                Dados=removed
            )
        )
    return jsonify({"error": "Item not found"}), 404


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


@app.route('/processamento/<int:item_id>', methods=['PUT'])
@auth.login_required
def update_processa(item_id):
    process = request.get_json()
    if 0 <= item_id < len(processada):
        processada[item_id].update(process)
        return make_response(
            jsonify(
                Mensagem='Processamento alterado com sucesso.',
                Dados=processada[item_id]
            )
        )
    return jsonify({"error": "Item not found"}), 404


@app.route('/processamento/<int:item_id>', methods=['DELETE'])
@auth.login_required
def delete_processa(item_id):
    if 0 <= item_id < len(processada):
        removed = processada.pop(item_id)
        return make_response(
            jsonify(
                Mensagem='Processamento deletado com sucesso.',
                Dados=removed
            )
        )
    return jsonify({"error": "Item not found"}), 404


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
            Mensagem='Importação cadastrada com sucesso.',
            Dados=importa
        )
    )


@app.route('/importacao/<int:item_id>', methods=['PUT'])
@auth.login_required
def update_importa(item_id):
    importa = request.get_json()
    if 0 <= item_id < len(importacao):
        importacao[item_id].update(importa)
        return make_response(
            jsonify(
                Mensagem='Importação alterada com sucesso.',
                Dados=importacao[item_id]
            )
        )
    return jsonify({"error": "Item not found"}), 404


@app.route('/importacao/<int:item_id>', methods=['DELETE'])
@auth.login_required
def delete_importa(item_id):
    if 0 <= item_id < len(importacao):
        removed = importacao.pop(item_id)
        return make_response(
            jsonify(
                Mensagem='Importação deletada com sucesso.',
                Dados=removed
            )
        )
    return jsonify({"error": "Item not found"}), 404

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


@app.route('/exportacao/<int:item_id>', methods=['PUT'])
@auth.login_required
def update_exporta(item_id):
    exporta = request.get_json()
    if 0 <= item_id < len(exportacao):
        exportacao[item_id].update(exporta)
        return make_response(
            jsonify(
                Mensagem='Exportação alterada com sucesso.',
                Dados=exportacao[item_id]
            )
        )
    return jsonify({"error": "Item not found"}), 404


@app.route('/exportacao/<int:item_id>', methods=['DELETE'])
@auth.login_required
def delete_exporta(item_id):
    if 0 <= item_id < len(exportacao):
        removed = exportacao.pop(item_id)
        return make_response(
            jsonify(
                Mensagem='Exportação deletada com sucesso.',
                Dados=removed
            )
        )
    return jsonify({"error": "Item not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)

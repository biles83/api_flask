from flask import Flask, make_response, jsonify, request
from scrapp.prod import producao
from scrapp.processada import processada
from scrapp.comercial import comercial
from scrapp.importacao import importacao
from scrapp.exportacao import exportacao

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# ----------------------------
# ROUTES -- Producao
# ----------------------------


@app.route('/producao', methods=['GET'])
def get_producao():
    return make_response(
        jsonify(
            Mensagem='Produção de vinhos, sucos e derivados do Rio Grande do Sul.',
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
            Mensagem='Comercialização de vinhos e derivados no Rio Grande do Sul.',
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

# ----------------------------
# ROUTES -- Processamento
# ----------------------------


@app.route('/processamento', methods=['GET'])
def get_processa():
    return make_response(
        jsonify(
            Mensagem='Quantidade de uvas processadas no Rio Grande do Sul.',
            Dados=processada
        )
    )


@app.route('/processamento', methods=['POST'])
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
def get_importa():
    return make_response(
        jsonify(
            Mensagem='Importação de derivados de uva.',
            Dados=importacao
        )
    )


@app.route('/importacao', methods=['POST'])
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
def get_exporta():
    return make_response(
        jsonify(
            Mensagem='Exportação de derivados de uva.',
            Dados=exportacao
        )
    )


@app.route('/exportacao', methods=['POST'])
def insert_exporta():
    exporta = request.json
    exportacao.append(exporta)
    return make_response(
        jsonify(
            Mensagem='Exportação cadastrada com sucesso.',
            Dados=exporta
        )
    )


app.run()

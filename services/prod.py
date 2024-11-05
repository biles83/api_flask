import requests
from bs4 import BeautifulSoup
import pandas as pd
from flask import Flask, make_response, jsonify, request
from json import loads, dumps

bd_full = []
for year in range(2021, 2024):

    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?ano=' + \
        str(year)+'&opcao=opt_02'
    response = requests.get(url)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        html_content = response.text  # Armazenando o conteúdo HTML da resposta
    else:
        print(f'Erro ao acessar a página: {response.status_code}')

    soup = BeautifulSoup(html_content, 'html.parser')

    teste = soup.findAll(True, {"class": ["tb_item", "tb_subitem"]})
    bd = []
    item = ""
    sub_item = ""
    valor = ""
    for result in teste:
        i = teste.index(result)
        if i % 2 == 0:
            text = result.text.strip()
            x = text.isupper()
            if x:
                item = text
            else:
                sub_item = text
        else:
            valor = result.text.strip()
            if item == "" or sub_item == "" or valor == "":
                continue
            else:
                # print(item)
                # print(sub_item)
                # print(valor)
                dados = [str(year), item, sub_item, valor]
                bd.append(dados)
                sub_item = ""
                valor = ""
    bd_full.append(bd)

df_producao = pd.DataFrame(bd_full[0])
i = 1

for i in range(len(bd_full)):
    df_temp = pd.DataFrame(bd_full[i])
    df_producao = pd.concat([df_producao, df_temp])

# Preparando o dataset para a API
df_producao = df_producao.drop_duplicates()  # Removendo duplicados caso exista
df_producao.columns = ['Ano', 'Item', 'Sub_item', 'Quantidade']
df_producao['Id'] = df_producao.index
df_producao = df_producao[['Id', 'Ano', 'Item', 'Sub_item', 'Quantidade']]
# df_producao.to_csv('prod.csv', sep=';', index=False, encoding=' Latin-1')
producao = df_producao.to_json(orient='records')
producao = loads(producao)

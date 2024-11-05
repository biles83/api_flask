import requests
from bs4 import BeautifulSoup
import pandas as pd
from flask import Flask, make_response, jsonify, request
from json import loads, dumps

bd_full = []

for opc in range(1, 5):

    for year in range(2021, 2024):

        url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?ano=' + \
            str(year)+'&opcao=opt_03&subopcao=subopt_0' + str(opc)
        response = requests.get(url)

        # Verificando se a requisição foi bem-sucedida
        if response.status_code == 200:
            html_content = response.text  # Armazenando o conteúdo HTML da resposta
        else:
            print(f'Erro ao acessar a página: {response.status_code}')

        soup = BeautifulSoup(html_content, 'html.parser')

        tipo = soup.find_all('button', class_='btn_sopt')[opc-1].string.strip()
        # botao = soup.find_all('button', class_='btn_sopt')

        teste = soup.findAll(True, {"class": ["tb_item", "tb_subitem"]})
        bd = []
        item = ""
        sub_item = ""
        valor = ""
        for result in teste:  # Exibindo apenas os primeiros 10 links
            i = teste.index(result)
            if i % 2 == 0:
                text = result.text.strip()
                x = text[0:3].isupper()
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
                    dados = [str(year), tipo, item, sub_item, valor]
                    bd.append(dados)
                    sub_item = ""
                    valor = ""
        bd_full.append(bd)

    # Ano
    # df_process_1 = pd.DataFrame(bd_full[0])
    # i = 1

    # for i in range(len(bd_full)):
    #    df_temp = pd.DataFrame(bd_full[i])
    #    df_process_1 = pd.concat([df_process_1, df_temp])

# Ano
df_process = pd.DataFrame(bd_full[0])
i = 1

for i in range(len(bd_full)):
    df_temp = pd.DataFrame(bd_full[i])
    df_process = pd.concat([df_process, df_temp])


df_process = df_process.drop_duplicates()  # Removendo duplicados caso exista
df_process.columns = ['Ano', 'Tipo', 'Item', 'Sub_item', 'Quantidade']
# df_process.to_csv('processada.csv', sep=';', index=False, encoding=' Latin-1')
processada = df_process.to_json(orient='records')
processada = loads(processada)

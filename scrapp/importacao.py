import requests
from bs4 import BeautifulSoup
import pandas as pd
from flask import Flask, make_response, jsonify, request
from json import loads, dumps

bd_full = []

for opc in range(1, 5):

    for year in range(2021, 2024):

        url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?ano=' + \
            str(year)+'&opcao=opt_05&subopcao=subopt_0' + str(opc)
        response = requests.get(url)

        # Verificando se a requisição foi bem-sucedida
        if response.status_code == 200:
            html_content = response.text  # Armazenando o conteúdo HTML da resposta
        else:
            print(f'Erro ao acessar a página: {response.status_code}')

        soup = BeautifulSoup(html_content, 'html.parser')

        # botao = soup.find_all('button', class_='btn_sopt')[1].string.strip()
        botao = soup.find_all('button', class_='btn_sopt')

        for result in botao:
            tipo = result.string
            table = soup.find('table', {'class': 'tb_base tb_dados'})
            data = []
            rows = table.find_all('tr')

            for row in rows:
                # Inclui cabeçalhos (th) e dados (td)
                cells = row.find_all(['th', 'td'])
                cells_text = [cell.get_text(strip=True) for cell in cells]
                data.append(cells_text)

            df = pd.DataFrame(data)
            df['Ano'] = year
            df['Tipo'] = tipo
            df.drop(len(df)-1, axis=0, inplace=True)  # Remover Total
            df.drop(0, axis=0, inplace=True)  # Remover Titulo
            df.columns = ['País', 'Quantidade', 'Valor', 'Ano', 'Tipo']

            bd_full.append(df)

        # Botao
        df_import_1 = pd.DataFrame(bd_full[0])
        i = 1

        for i in range(len(bd_full)):
            df_temp = pd.DataFrame(bd_full[i])
            df_import_1 = pd.concat([df_import_1, df_temp])

    # Ano
    df_import = pd.DataFrame(bd_full[0])
    i = 1

    for i in range(len(bd_full)):
        df_temp = pd.DataFrame(bd_full[i])
        df_import = pd.concat([df_import, df_temp])

    df_import.to_csv('import.csv', index=False, encoding=' Latin-1')
    importacao = df_import.to_json(orient='records')
    importacao = loads(importacao)

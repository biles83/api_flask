# My Flask API

Este é um projeto de API desenvolvido com Flask, que inclui operações CRUD, web scraping e autenticação básica.

## 🚀 Funcionalidades

- **Autenticação Básica**: Protege rotas sensíveis usando autenticação HTTP básica.
- **Operações CRUD**: Permite criar, ler, atualizar e deletar itens.
- **Web Scraping**: Extrai dados de páginas web (título, cabeçalhos, parágrafos) usando BeautifulSoup.
- **Cache e Documentação**: Implementa cache para otimização e documentação automática com Swagger.

## 📁 Estrutura do Projeto

```bash
intro_api/
├── api_flask/
│   ├── __init__.py
│   ├── api/
│   │   ├── auth_routes.py
│   │   ├── crud_routes.py
│   │   ├── scrape_routes.py
│   │   └── services/
│   │       ├── __init__.py
│   │       ├── comercial.py
│   │       ├── exportacao.py
│   │       ├── importacao.py
│   │       ├── processada.py
│   │       └── prod.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── comercial.py
│   │   ├── exportacao.py
│   │   ├── importacao.py
│   │   ├── processada.py
│   │   └── prod.py
│   ├── requirements.txt
│   ├── api.py
│   ├── README.md
│   └── vercel.json
```

- **`api_flask/`**: Diretório principal do aplicativo.
  - **`api/`**: Contém os códigos para rodar no Vercel.
  - **`services/`**: Serviços para lógica de negócios, como scraping.
- **`api.py`**: Ponto de entrada para iniciar o aplicativo.
- **`requirements.txt`**: Lista de dependências do projeto.
- **`vercel.json`**: Configurações para Vercel.
- **`README.md`**: Documentação do projeto.

## 🛠️ Como Executar o Projeto

### 1. Clone o Repositório

```bash
git clone https://github.com/biles83/api_flask
cd api_flask
```

### 2. Crie um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o Aplicativo

```bash
python api.py
```

O aplicativo estará disponível em `http://localhost:5000`.

## 🐳 Como Usar com Docker

### 1. Construa a Imagem Docker

```bash
docker build -t my-flask-api .
```

### 2. Execute o Container

```bash
docker run -p 5000:5000 my-flask-api
```

Acesse a aplicação em `http://localhost:5000`.

## 📖 Documentação da API

A documentação da API é gerada automaticamente com Swagger e está disponível em `http://localhost:5000/apidocs/`.

## 🤝 Contribuindo

1. Fork este repositório.
2. Crie sua branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Faça push para sua branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.
instalar, configurar e usar o projeto. Ele também cobre contribuições, contato, licença e agradecimentos, tornando-o completo e fácil de entender para novos desenvolvedores.

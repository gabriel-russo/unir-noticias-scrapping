# Notícias UNIR Scrapping

## Preparação

```commandline
virtualenv venv
```

```commandline
source venv/bin/activate
```

```commandline
pip install -r requirements.txt
```

## Documentação:

- NewsDatabase: Classe para trabalhar com sqlite de forma simplificada
- scrap: Função que executa o web scrapping
- init: Função que cria e popula o banco de dados sqlite
- monitoring: Função que faz o scrapping e adiciona novos dados as tabelas caso houver

### Monitoramento
Na primeira execução, será criado todas as tabelas, com a coluna "viewed" com TRUE. 

Nas execuções posteriores, caso uma nova notícia surja, ela será inserida como "viewed" FALSE.

Dessa forma, você poderá saber se a notícia é nova através das tuplas com o viewed = FALSE.

Após consumir essas tuplas, é necessário atribuir um novo valor a esta coluna como TRUE por meio de um UPDATE

### Entrypoint
Execute o arquivo main.py

```commandline
python3 main.py
```

### Banco de dados
#### Tabelas
- dacc_news: Tabela com as notícias do site https://dacc.unir.br/noticia/pagina

- announcements: Tabela com as notícias do site https://www.unir.br/noticia/lista_comunicados

- unir_news: Tabela com as notícias do site https://www.unir.br/noticia/lista_noticias

#### Colunas
- title: Coluna com o título da notícia
- date: Data de publicação da notícia
- link: Link para a página da notícia
- viewed: Coluna para verificar se a notícia é nova em relação aos dados da primeira execução do scrapper
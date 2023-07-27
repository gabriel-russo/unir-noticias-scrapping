from scrapping import scrap, NewsDatabase

if __name__ == "__main__":
    db = NewsDatabase(".", "news.db")

    scrap(
        url="https://dacc.unir.br/noticia/pagina",
        classes="col-md-6 col-lg-6 py-2",
        tablename="dacc_news",
        db_connection=db,
    )
    scrap(
        url="https://www.unir.br/noticia/lista_comunicados",
        classes="col-6 mt-4 pl-3",
        tablename="announcement",
        db_connection=db,
    )
    scrap(
        url="https://www.unir.br/noticia/lista_noticias",
        classes="col-md-6 pl-3",
        tablename="unir_news",
        db_connection=db,
    )

    db.disconnect()

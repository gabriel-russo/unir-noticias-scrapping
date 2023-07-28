from os.path import exists
from scrapping import scrap, NewsDatabase


def init(props):
    db = NewsDatabase(db_name="news.db")

    for prop in props:
        tablename = prop.pop("tablename")

        db.load_dataframe(
            scrap(
                **prop,
            ),
            tablename,
        )

    db.disconnect()


def monitoring(props):
    db = NewsDatabase(db_name="news.db")

    for prop in props:
        tablename = prop.pop("tablename")

        db.insert_difference(
            scrap(
                **prop,
            ),
            tablename,
        )

    db.disconnect()


if __name__ == "__main__":
    scrap_props = [
        {
            "url": "https://dacc.unir.br/noticia/pagina",
            "classes": "col-md-6 col-lg-6 py-2",
            "tablename": "dacc_news",
        },
        {
            "url": "https://www.unir.br/noticia/lista_comunicados",
            "classes": "col-6 mt-4 pl-3",
            "tablename": "announcements",
        },
        {
            "url": "https://www.unir.br/noticia/lista_noticias",
            "classes": "col-md-6 pl-3",
            "tablename": "unir_news",
        },
    ]

    if not exists("news.db"):
        init(scrap_props)
    else:
        monitoring(scrap_props)

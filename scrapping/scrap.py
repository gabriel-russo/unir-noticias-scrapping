from bs4 import BeautifulSoup
from requests import get, ConnectionError
from pandas import DataFrame
from .NewsDatabase import NewsDatabase


def scrap(url: str, classes: str, tablename: str, db_connection: NewsDatabase) -> None:
    """
    Função Scrapping base para os sites de notícias da UNIR, pois os mesmos possuem a mesma estrutura HTML, apenas
    mudando o nome das classes dos cards de notícias.

    Args:
        url (str): URL da página de notícias.
        classes (str): Nome da classe dos cards de notícias.
        tablename (str): Nome da tabela no banco de dados sqlite.
        db_connection (NewsDatabase): Objeto de conexão com o banco de dados sqlite.
    Returns:
        None
    """

    req = get(url)

    if req.status_code >= 400:
        raise ConnectionError("Erro de conexão com a página!!")

    page = BeautifulSoup(req.content, "html.parser")

    all_cards = page.find_all("div", attrs={"class": classes})

    if len(all_cards):
        rows = []

        for card in all_cards:
            while "\n" in card.contents:
                card.contents.remove("\n")

            date, info_container = card.contents

            info = info_container.find("a")

            rows.append((info.string, date.string, info.get("href")))

        db_connection.load_dataframe(
            DataFrame(rows, columns=["title", "date", "link"]), tablename
        )

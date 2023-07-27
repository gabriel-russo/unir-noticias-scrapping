from bs4 import BeautifulSoup
from requests import get, ConnectionError
from pandas import DataFrame


def dacc_scrapping():
    req = get("https://dacc.unir.br/noticia/pagina")

    if req.status_code >= 400:
        raise ConnectionError("Erro de conexão com a página do DACC!")

    page = BeautifulSoup(req.content, "html.parser")

    all_news_cards = page.find_all("div", attrs={"class": "col-md-6 col-lg-6 py-2"})

    if len(all_news_cards):
        dacc_news = []

        for news_card in all_news_cards:
            while "\n" in news_card.contents:
                news_card.contents.remove("\n")

            date, news_container = news_card.contents

            news = news_container.find("a")

            dacc_news.append((news.string, date.string, news.get("href")))

        DataFrame(dacc_news, columns=["title", "date", "link"]).to_csv(
            "dacc_news.csv", index=False
        )

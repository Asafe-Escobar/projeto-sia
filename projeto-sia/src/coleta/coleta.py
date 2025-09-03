
import requests
import xml.etree.ElementTree as ET


def fetch_news(query: str, max_items: int = 15) -> list:
    """Busca notícias via feed RSS do Google News para a `query` dada.

    Retorna uma lista de dicionários com `title`, `link` e `description`.
    """
    url = (
        f"https://news.google.com/rss/search?q={query.replace(' ', '+')}" 
        f"&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    )
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        items = []
        for item in root.findall('.//item')[:max_items]:
            title = item.find('title').text if item.find('title') is not None else ''
            link = item.find('link').text if item.find('link') is not None else ''
            description = item.find('description').text if item.find('description') is not None else ''
            items.append({
                "title": title,
                "link": link,
                "description": description,
            })
        if not items:
            # log leve, não quebra execução
            print("Nenhuma notícia encontrada para a busca.")
        return items
    except Exception as error:
        print(f"Erro ao buscar notícias: {error}")
        return []

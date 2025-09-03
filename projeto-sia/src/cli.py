"""Script de linha de comando (simples) para coletar e salvar notícias."""

import pandas as pd
from src.coleta import fetch_news
from src.processamento import clean_text, classify_sentiment


def main() -> None:
    """Coleta notícias e salva em `data/latest.csv`."""
    query = "Inteligência Artificial Piauí"
    news = fetch_news(query)
    processed = []
    for item in news:
        cleaned = clean_text(item["description"])
        sentiment = classify_sentiment(cleaned)
        processed.append(
            {
                "title": item["title"],
                "link": item["link"],
                "description": cleaned,
                "sentiment": sentiment,
            }
        )
    df = pd.DataFrame(processed)
    df.to_csv("data/latest.csv", index=False)
    print("Dados salvos em data/latest.csv")


if __name__ == "__main__":
    main()

import re
import unicodedata
from typing import List

from src.utils import normalize_word
from src.lexicons import POSITIVE, NEGATIVE


def clean_text(text: str) -> str:
    """Remove HTML, pontuação e normaliza acentuação do texto."""
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    text = re.sub(r"\s+", " ", text).strip()
    return text

def classify_sentiment(text: str) -> str:
    """Classifica o sentimento como 'positivo', 'negativo' ou 'neutro'."""
    score = 0
    text_norm = clean_text(text)

    for pos_word in POSITIVE:
        if pos_word in text_norm:
            score += 1
    for neg_word in NEGATIVE:
        if neg_word in text_norm:
            score -= 1
    
    words = [normalize_word(w) for w in text_norm.split()]
    for word in words:
        for suf in ["s", "a", "o", "os", "as", "es", "is", "ar", "ado", "ada", "ido", "ida", "ando", "endo", "indo", "ou", "eu", "iu"]:
            if word.rstrip(suf) in POSITIVE:
                score += 1
            if word.rstrip(suf) in NEGATIVE:
                score -= 1
    if score > 0:
        return "positivo"
    elif score < 0:
        return "negativo"
    else:
        return "neutro"

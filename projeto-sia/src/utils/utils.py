import re

# ...existing code...


def normalize_word(word):
    word = re.sub(r"[^\w\s]", "", word)
    return word.lower()

import unittest
from src.processamento import clean_text, classify_sentiment

class TestProcessamento(unittest.TestCase):
    def test_clean_text(self):
        self.assertEqual(clean_text('<b>Olá!</b> Bom dia.'), 'ola bom dia')
    def test_classify_sentiment(self):
        self.assertEqual(classify_sentiment('excelente otimo perfeito'), 'positivo')
        self.assertEqual(classify_sentiment('ruim horrivel lixo'), 'negativo')
        self.assertEqual(classify_sentiment('noticia comum'), 'neutro')

if __name__ == "__main__":
    unittest.main()

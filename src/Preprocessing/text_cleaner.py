# src/preprocessing/text_cleaner.py

import re
import nltk
from nltk.corpus import stopwords

# Nota: No ambiente de hospedagem (Streamlit Cloud), você precisará garantir que 'punkt' e 'stopwords'
# do NLTK sejam baixados. Isso pode ser feito adicionando um script de pré-execução
# ou uma seção no próprio código se ele for rodado uma única vez na inicialização.
# Por exemplo:
# try:
#     nltk.data.find('corpora/stopwords')
# except nltk.downloader.DownloadError:
#     nltk.download('stopwords')
# try:
#     nltk.data.find('tokenizers/punkt')
# except nltk.downloader.DownloadError:
#     nltk.download('punkt')


def clean_text(text):
    """Remove caracteres especiais, números e múltiplas quebras de linha."""
    if not isinstance(text, str):
        return "" # Retorna string vazia se não for texto
    text = re.sub(r'[\d\W_]+', ' ', text) # Remove números e não-palavras (exceto espaços)
    text = re.sub(r'\s+', ' ', text).strip() # Remove múltiplos espaços e espaços no início/fim
    return text

def tokenize_text(text):
    """Divide o texto em palavras (tokens)."""
    if not isinstance(text, str):
        return [] # Retorna lista vazia se não for texto
    try:
        return nltk.word_tokenize(text, language='portuguese')
    except LookupError:
        # Se 'punkt' não estiver baixado, tenta baixá-lo (útil para ambientes que não persistem downloads)
        nltk.download('punkt')
        return nltk.word_tokenize(text, language='portuguese')


def remove_stopwords(tokens):
    """Remove stop words de uma lista de tokens."""
    try:
        stop_words = set(stopwords.words('portuguese'))
    except LookupError:
        # Se 'stopwords' não estiver baixado, tenta baixá-lo
        nltk.download('stopwords')
        stop_words = set(stopwords.words('portuguese'))

    return [word for word in tokens if isinstance(word, str) and word.lower() not in stop_words]


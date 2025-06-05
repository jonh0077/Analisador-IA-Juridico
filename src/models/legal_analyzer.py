# src/models/legal_analyzer.py

import spacy

class LegalDocumentAnalyzer:
    def __init__(self, model_name="pt_core_news_sm"):
        """Inicializa o analisador com um modelo spaCy."""
        try:
            # Tenta carregar o modelo especificado
            self.nlp = spacy.load(model_name)
        except OSError:
            print(f"Modelo '{model_name}' não encontrado. Tentando baixar e carregar.")
            # Se o modelo não for encontrado, tenta baixá-lo
            # Esta parte só funcionará se o ambiente tiver permissão para baixar
            spacy.cli.download(model_name)
            self.nlp = spacy.load(model_name)


    def analyze_entities(self, text):
        """Extrai entidades nomeadas do texto."""
        if not isinstance(text, str) or not text.strip():
            return [] # Retorna lista vazia se o texto for inválido
        doc = self.nlp(text)
        entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
        return entities

    def summarize_text(self, text, max_sentences=3):
        """
        Função placeholder para sumarização.
        Para uma sumarização robusta, você precisaria de um modelo dedicado de transformers (e.g., de Hugging Face).
        Esta implementação é um exemplo muito básico (pega as primeiras frases).
        """
        if not isinstance(text, str) or not text.strip():
            return "" # Retorna string vazia se o texto for inválido

        sentences = text.split('.') # Divisão simples por ponto
        summary_sentences = []
        count = 0
        for sentence in sentences:
            if sentence.strip(): # Garante que a frase não está vazia
                summary_sentences.append(sentence.strip())
                count += 1
                if count >= max_sentences:
                    break

        return ". ".join(summary_sentences) + ("." if summary_sentences and not summary_sentences[-1].endswith('.') else "")

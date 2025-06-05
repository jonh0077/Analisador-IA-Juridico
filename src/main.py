# src/main.py
import streamlit as st
import os # Importar para lidar com caminhos de arquivo
from .utils import read_document # Vamos criar isso em src/utils/read_document.py
from .preprocessing.text_cleaner import clean_text, tokenize_text, remove_stopwords # Novos imports
from .models.legal_analyzer import LegalDocumentAnalyzer # Novo import

def main():
    st.set_page_config(layout="wide") # Opcional: Para usar a largura total da tela
    st.title("AI-Powered Legal Document Analyzer")
    st.write("Bem-vindo ao analisador inteligente de documentos jurídicos.")
    st.write("Esta é a base do seu projeto. Comece a construir aqui!")

    st.subheader("Faça upload do seu documento jurídico")
    # Permite upload de PDF, DOCX e TXT
    uploaded_file = st.file_uploader(
        "Selecione um arquivo",
        type=["pdf", "docx", "txt"],
        help="Faça upload de um documento em formato PDF, DOCX ou TXT para análise."
    )

    # Inicializa o analisador de IA (para carregar o modelo spaCy uma vez)
    # É bom inicializar fora do 'if uploaded_file' para não recarregar a cada upload
    # Mas para simplicidade inicial, podemos deixar aqui
    analyzer = LegalDocumentAnalyzer() 

    if uploaded_file is not None:
        st.success(f"Arquivo '{uploaded_file.name}' carregado com sucesso!")

        # Processar o arquivo carregado
        file_extension = os.path.splitext(uploaded_file.name)[1].lower()

        # Usar uma função de utilidade para ler o documento
        text_content = read_document(uploaded_file, file_extension)

        if text_content:
            st.subheader("Conteúdo do Documento:")
            st.text_area("Texto Extraído", text_content, height=300, disabled=True)

            st.subheader("Pré-processamento:")
            cleaned_text = clean_text(text_content)
            st.text_area("Texto Limpo", cleaned_text, height=150, disabled=True)

            tokens = tokenize_text(cleaned_text)
            st.write(f"Primeiros 20 tokens: {tokens[:20]}...")

            filtered_tokens = remove_stopwords(tokens)
            st.write(f"Primeiros 20 tokens sem stopwords: {filtered_tokens[:20]}...")

            st.subheader("Análise Jurídica:")
            
            # Chama as funções de análise
            entities = analyzer.analyze_entities(cleaned_text)
            st.write("Entidades Extraídas:")
            if entities:
                st.json(entities) # Mostra as entidades em formato JSON
            else:
                st.info("Nenhuma entidade encontrada.")

            summary = analyzer.summarize_text(cleaned_text, max_sentences=5)
            st.subheader("Resumo do Documento:")
            if summary:
                st.text_area("Resumo", summary, height=150, disabled=True)
            else:
                st.info("Não foi possível gerar um resumo.")

        else:
            st.error("Não foi possível extrair o texto do documento.")

    st.markdown("---")
    st.caption("Desenvolvido com Streamlit e Python")


if __name__ == "__main__":
    main()



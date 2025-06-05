# src/main.py
import streamlit as st
import os # Importar para lidar com caminhos de arquivo
from .utils import read_document # Vamos criar isso em src/utils/read_document.py

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

    if uploaded_file is not None:
        st.success(f"Arquivo '{uploaded_file.name}' carregado com sucesso!")

        # Processar o arquivo carregado
        file_extension = os.path.splitext(uploaded_file.name)[1].lower()

        # Usar uma função de utilidade para ler o documento
        text_content = read_document(uploaded_file, file_extension)

        if text_content:
            st.subheader("Conteúdo do Documento:")
            st.text_area("Texto Extraído", text_content, height=300, disabled=True)
        else:
            st.error("Não foi possível extrair o texto do documento.")

    st.markdown("---")
    st.caption("Desenvolvido com Streamlit e Python")


if __name__ == "__main__":
    main()
      

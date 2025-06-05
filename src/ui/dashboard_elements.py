# src/ui/dashboard_elements.py
import streamlit as st

def display_analysis_results(entities, summary):
    """Função para exibir os resultados da análise de forma organizada."""
    st.subheader("Resultados da Análise")

    with st.expander("Ver Entidades Extraídas"):
        if entities:
            st.json(entities)
        else:
            st.info("Nenhuma entidade encontrada ou dados de entidade não disponíveis.")

    with st.expander("Ver Resumo do Documento"):
        if summary:
            st.write(summary)
        else:
            st.info("Resumo não disponível.")

# Você pode ter mais funções aqui para outros elementos de UI, como:
# def create_sidebar_options():
#    st.sidebar.header("Opções")
#    # ... adicionar widgets de sidebar aqui

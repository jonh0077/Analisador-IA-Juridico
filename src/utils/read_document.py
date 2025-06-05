# src/utils/read_document.py

import io
from docx import Document # Para arquivos .docx
from PyPDF2 import PdfReader # Para arquivos .pdf

def read_document(uploaded_file, file_extension):
    """
    Lê o conteúdo de um arquivo carregado (UploadedFile do Streamlit)
    baseado na sua extensão.
    """
    text_content = ""
    try:
        if file_extension == ".txt":
            # Decodifica o conteúdo como texto (UTF-8 é comum)
            text_content = uploaded_file.getvalue().decode("utf-8")
        elif file_extension == ".docx":
            # Usa BytesIO para ler o arquivo DOCX em memória
            doc = Document(io.BytesIO(uploaded_file.getvalue()))
            for para in doc.paragraphs:
                text_content += para.text + "\n"
        elif file_extension == ".pdf":
            # Usa BytesIO para ler o arquivo PDF em memória
            reader = PdfReader(io.BytesIO(uploaded_file.getvalue()))
            for page in reader.pages:
                text_content += page.extract_text() + "\n"
        else:
            text_content = "Formato de arquivo não suportado."
    except Exception as e:
        text_content = f"Erro ao ler o arquivo: {e}"
        print(f"Erro ao ler o arquivo: {e}") # Para depuração

    return text_content.strip() # Remove espaços em branco extras no início/fim
      

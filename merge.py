

import os
import glob
from datetime import datetime

try:
    from PyPDF2 import PdfMerger
except ImportError:
    print("A biblioteca PyPDF2 não está instalada.")
    print("Por favor, instale-a executando o comando: pip install PyPDF2")
    exit()

def extrair_data_do_nome(nome_arquivo):
    """Extrai a data do nome do arquivo PDF."""
    try:
        # A data está no formato DD-MM-AA antes de '.pdf'
        parte_data = nome_arquivo.split('_venc_')[1].split('.')[0]
        return datetime.strptime(parte_data, '%d-%m-%y')
    except (IndexError, ValueError):
        # Retorna uma data muito antiga se o padrão não for encontrado
        return datetime.min

def juntar_pdfs_por_data():
    """
    Junta todos os PDFs em um único arquivo, ordenados pela data no nome do arquivo.
    """
    # Encontra todos os arquivos PDF no diretório atual
    arquivos_pdf = glob.glob('*.pdf')

    if not arquivos_pdf:
        print("Nenhum arquivo PDF encontrado no diretório.")
        return

    # Ordena os arquivos pela data extraída do nome
    arquivos_pdf.sort(key=extrair_data_do_nome)

    merger = PdfMerger()

    for pdf in arquivos_pdf:
        merger.append(pdf)

    nome_arquivo_final = 'documento_final.pdf'
    merger.write(nome_arquivo_final)
    merger.close()

    print(f"PDFs juntados com sucesso no arquivo: {nome_arquivo_final}")
    print("\nOrdem dos arquivos juntados:")
    for pdf in arquivos_pdf:
        print(f"- {os.path.basename(pdf)}")

if __name__ == "__main__":
    juntar_pdfs_por_data()


from pypdf import PdfReader, PdfWriter


## dividir_pdf_em_paginas("meu_arquivo.pdf", "pasta_dos_resultados")
## Instalar --> $ pip install pypdf
def dividir_pdf_em_paginas(arquivo_entrada, pasta_saida):
    reader = PdfReader(arquivo_entrada)
    for i, pagina in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(pagina)
        
        nome_saida = f"{pasta_saida}/pagina_{i+1}.pdf"
        with open(nome_saida, "wb") as saida:
            writer.write(saida)
        print(f"Página {i+1} salva em: {nome_saida}")

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
from tkcalendar import DateEntry

try:
    from PIL import Image, ImageTk
except ImportError:
    messagebox.showerror("Erro", "A biblioteca Pillow é necessária. Instale-a usando 'pip install Pillow'.")

# Função para selecionar o diretório
def selecionar_diretorio():
    caminho = filedialog.askdirectory()
    entrada_diretorio.delete(0, tk.END)
    entrada_diretorio.insert(0, caminho)

# Função para apagar arquivos de acordo com o intervalo de tempo e formatos
def deletar_arquivos():
    try:
        diretorio = entrada_diretorio.get()
        data_inicial = datetime.strptime(entrada_data_inicial.get(), "%d/%m/%Y")
        data_final = datetime.strptime(entrada_data_final.get(), "%d/%m/%Y")

        # Formatos de arquivo
        formatos = []
        if var_xlsx.get():
            formatos.append(".xlsx")
        if var_docx.get():
            formatos.append(".docx")
        if var_pdf.get():
            formatos.append(".pdf")
        if var_xml.get():
            formatos.append(".xml")
        if var_zip.get():
            formatos.append(".zip")
        if var_ogg.get():
            formatos.append(".ogg")
        if var_png.get():
            formatos.append(".png")
        if var_jpeg.get():
            formatos.append(".jpeg")
        if var_py.get():
            formatos.append(".py")
        if var_exe.get():
            formatos.append(".exe")
        if var_pyw.get():
            formatos.append(".pyw")

        # Palavra-chave para exceção
        palavra_excecao = entrada_palavra_excecao.get()

        # Apagar arquivos dentro do intervalo de tempo, com os formatos selecionados e filtrando a palavra
        for root, dirs, files in os.walk(diretorio):
            for file in files:
                caminho_arquivo = os.path.join(root, file)
                # Obtém a data de modificação do arquivo
                data_modificacao = datetime.fromtimestamp(os.path.getmtime(caminho_arquivo))
                
                # Verifica se o arquivo está no intervalo, no formato correto e se não contém a palavra de exceção
                if data_inicial <= data_modificacao <= data_final and any(file.endswith(f) for f in formatos):
                    if palavra_excecao and palavra_excecao in file:
                        continue  # Pula o arquivo que contém a palavra de exceção
                    os.remove(caminho_arquivo)

        messagebox.showinfo("Sucesso", "Arquivos deletados com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# Interface Tkinter
root = tk.Tk()
root.title("Delete Master V1.2")

# Diretório
tk.Label(root, text="Selecione o Diretório:").grid(row=0, column=0, padx=10, pady=5)
entrada_diretorio = tk.Entry(root, width=50)
entrada_diretorio.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Procurar", command=selecionar_diretorio).grid(row=0, column=2, padx=10, pady=5)

# Intervalo de tempo com DataEntry
tk.Label(root, text="Intervalo de Tempo:").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="De (Data Inicial)").grid(row=2, column=0, padx=10, pady=5)
entrada_data_inicial = DateEntry(root, date_pattern="dd/mm/yyyy", width=12)
entrada_data_inicial.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Até (Data Final)").grid(row=3, column=0, padx=10, pady=5)
entrada_data_final = DateEntry(root, date_pattern="dd/mm/yyyy", width=12)
entrada_data_final.grid(row=3, column=1, padx=10, pady=5)

# Define automaticamente a data final como a data atual
entrada_data_final.set_date(datetime.now())

# Formatos de arquivo
tk.Label(root, text="Selecione os formatos a deletar:").grid(row=4, column=0, columnspan=2, padx=10, pady=5)

var_xlsx = tk.BooleanVar()
var_docx = tk.BooleanVar()
var_pdf = tk.BooleanVar()
var_xml = tk.BooleanVar()
var_zip = tk.BooleanVar()
var_ogg = tk.BooleanVar()
var_png = tk.BooleanVar()
var_jpeg = tk.BooleanVar()
var_py = tk.BooleanVar()
var_exe = tk.BooleanVar()
var_pyw = tk.BooleanVar()

tk.Checkbutton(root, text=".xlsx (Excel)", variable=var_xlsx).grid(row=5, column=0, sticky="w")
tk.Checkbutton(root, text=".docx (Word)", variable=var_docx).grid(row=5, column=1, sticky="w")
tk.Checkbutton(root, text=".pdf (PDF)", variable=var_pdf).grid(row=6, column=0, sticky="w")
tk.Checkbutton(root, text=".xml (XML)", variable=var_xml).grid(row=6, column=1, sticky="w")
tk.Checkbutton(root, text=".zip (ZIP)", variable=var_zip).grid(row=7, column=0, sticky="w")
tk.Checkbutton(root, text=".ogg (OGG)", variable=var_ogg).grid(row=7, column=1, sticky="w")
tk.Checkbutton(root, text=".png (PNG)", variable=var_png).grid(row=8, column=0, sticky="w")
tk.Checkbutton(root, text=".jpeg (JPEG)", variable=var_jpeg).grid(row=8, column=1, sticky="w")
tk.Checkbutton(root, text=".py (Python)", variable=var_py).grid(row=9, column=0, sticky="w")
tk.Checkbutton(root, text=".exe (EXE)", variable=var_exe).grid(row=9, column=1, sticky="w")
tk.Checkbutton(root, text=".pyw (Python Windows)", variable=var_pyw).grid(row=10, column=0, sticky="w")

# Filtro de exceção de palavra
tk.Label(root, text="Exceção de Palavra (opcional):").grid(row=11, column=0, padx=10, pady=5)
entrada_palavra_excecao = tk.Entry(root, width=20)
entrada_palavra_excecao.grid(row=11, column=1, padx=10, pady=5)

# Botão para deletar arquivos
tk.Button(root, text="Deletar Arquivos", command=deletar_arquivos).grid(row=12, column=0, columnspan=3, pady=10)

# Aviso no rodapé
rodape = tk.Label(root, text="ATENÇÃO: USE ESTE PROGRAMA, SE SOUBER O QUE PRETENTE FAZER. COM RISCO DE DELETAR O SISTEMA.", fg="red")
rodape.grid(row=13, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()

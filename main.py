import os
import re
import locale
import numpy as np
from tkinter import Tk, filedialog, ttk, messagebox, StringVar, IntVar
from tkinter import Button, Label, Spinbox
from PIL import Image
import ghostscript
import shutil

Image.MAX_IMAGE_PIXELS = None

def gerar_separacoes_tiffsep(input_pdf, output_dir, dpi=300):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    args = [
        "gs",
        "-dNOPAUSE",
        "-dBATCH",
        "-sDEVICE=tiffsep",
        f"-r{dpi}",
        f"-sOutputFile={output_dir}/pagina_%03d.tif",
        input_pdf
    ]
    encoding = locale.getpreferredencoding()
    args = [a.encode(encoding) for a in args]
    ghostscript.Ghostscript(*args)

def calcular_cobertura_tinta(imagem_path):
    img = Image.open(imagem_path).convert('L')
    arr = np.array(img)
    tinta = (255 - arr) / 255.0
    cobertura_total = tinta.sum()
    total_pixels = arr.shape[0] * arr.shape[1]
    return round((cobertura_total / total_pixels) * 100, 2)

def analisar_separacoes(dir_path, progress_bar, status_var):
    resultados = {}
    padrao = re.compile(r'pagina_(\d{3})\((Cyan|Magenta|Yellow|Black)\)\.tif')

    arquivos = sorted([f for f in os.listdir(dir_path) if padrao.match(f)])
    total = len(arquivos)
    progresso = 0

    for arquivo in arquivos:
        match = padrao.match(arquivo)
        if not match:
            continue

        num_pagina = int(match.group(1))
        cor_nome = match.group(2)
        canal = {'Cyan': 'C', 'Magenta': 'M', 'Yellow': 'Y', 'Black': 'K'}[cor_nome]

        caminho = os.path.join(dir_path, arquivo)
        porcentagem = calcular_cobertura_tinta(caminho)

        resultados.setdefault(num_pagina, {})[canal] = porcentagem

        progresso += 1
        progress_bar["value"] = (progresso / total) * 100
        progress_bar.update()
        status_var.set(f"📊 Analisando ({progresso}/{total})...")

    return resultados

def analisar_pdf(pdf_path, tree, status_var, progress_bar, dpi):
    output_dir = "separacoes_temp"
    try:
        status_var.set(f"🔄 Gerando separações (DPI={dpi}) com Ghostscript...")
        progress_bar["value"] = 0
        progress_bar.update()
        tree.delete(*tree.get_children())

        gerar_separacoes_tiffsep(pdf_path, output_dir, dpi)

        status_var.set("📊 Analisando separações...")
        resultados = analisar_separacoes(output_dir, progress_bar, status_var)

        for pagina in sorted(resultados.keys()):
            dados = resultados[pagina]
            c = dados.get('C', 0.0)
            m = dados.get('M', 0.0)
            y = dados.get('Y', 0.0)
            k = dados.get('K', 0.0)
            total = round((c + m + y + k)/4, 2)
            tree.insert("", "end", values=[pagina, c, m, y, k, total, dpi])

        progress_bar["value"] = 100
        status_var.set("✅ Análise concluída.")
        
        shutil.rmtree(output_dir)

    except Exception as e:
        status_var.set("❌ Erro na análise.")
        messagebox.showerror("Erro", str(e))
        progress_bar["value"] = 0

def selecionar_pdf(tree, status_var, progress_bar, dpi_var):
    caminho = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if caminho:
        dpi = dpi_var.get()
        analisar_pdf(caminho, tree, status_var, progress_bar, dpi)

def criar_interface():
    root = Tk()
    root.title("Analisador de Cobertura CMYK")
    root.geometry("800x500")

    # Controle de DPI
    dpi_var = IntVar(value=300)
    frame_top = ttk.Frame(root)
    frame_top.pack(pady=10)

    label_dpi = Label(frame_top, text="DPI:")
    label_dpi.pack(side="left", padx=(10, 5))

    spin_dpi = Spinbox(frame_top, from_=72, to=1200, increment=1, width=6, textvariable=dpi_var)
    spin_dpi.pack(side="left", padx=(0, 20))

    botao = Button(frame_top, text="Selecionar PDF e Analisar",
                   command=lambda: selecionar_pdf(tree, status_var, progress_bar, dpi_var))
    botao.pack(side="left")

    # Tabela
    colunas = ("Página", "C (%)", "M (%)", "Y (%)", "K (%)", "Média (%)", "DPI")
    tree = ttk.Treeview(root, columns=colunas, show="headings")
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=90 if col != "Página" else 70, anchor="center")
    tree.pack(expand=True, fill="both", padx=10, pady=10)

    # Barra de progresso
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")
    progress_bar.pack(pady=5)

    # Status
    status_var = StringVar()
    status_var.set("Aguardando PDF...")
    status_label = Label(root, textvariable=status_var, anchor="w")
    status_label.pack(fill="x", padx=10, pady=(0, 10))

    root.mainloop()

if __name__ == "__main__":
    criar_interface()

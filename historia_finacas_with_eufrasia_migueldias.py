
import io
import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

def mostrar_fato(detalhe):
    
    messagebox.showinfo("Curiosidade Eufrasia", detalhe)


janela = tk.Tk()
janela.title("História Financeira: Eufrásia Teixeira Leite")

janela.geometry("500x580")  
janela.configure(bg="#0d6e8a")

lbl_titulo = tk.Label(
    janela,
    text="Eufrásia Teixeira Leite",
    font=("Times New Roman", 26, "bold"),
    bg="#0d6e8a",
    fg="#f1d417",
)
lbl_titulo.pack(pady=7)


lbl_subtitulo = tk.Label(
    janela,
    text="A primeira investidora global do Brasil",
    font=("Arial", 10, "italic"),
    bg="#0d6e8a",
    fg="#f1d417",
)
lbl_subtitulo.pack(pady=2)


url_imagem = "https://ichef.bbci.co.uk/ace/ws/640/cpsprodpb/5960/live/0e4b9020-0aef-11f0-88b7-5556e7b55c5e.jpg.webp"



foto_eufrasia = None

try:

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    resposta = requests.get(url_imagem, headers=headers, timeout=5)
    resposta.raise_for_status()  

    dados_imagem = resposta.content

   
    imagem_pil = Image.open(io.BytesIO(dados_imagem))
    imagem_pil = imagem_pil.resize(
        (130, 160), Image.Resampling.LANCZOS
    )  

    foto_eufrasia = ImageTk.PhotoImage(imagem_pil)

   
    lbl_imagem = tk.Label(janela, image=foto_eufrasia, bg="#f4f4f9")
    lbl_imagem.image = foto_eufrasia  
    lbl_imagem.pack(pady=10)

except Exception as erro:
    
    print(f"Erro ao carregar imagem: {erro}")
    lbl_erro = tk.Label(
        janela,
        text="[Foto de Eufrásia Teixeira Leite - Indisponível sem internet]",
        font=("Arial", 9, "italic"),
        fg="gray",
        bg="#f4f4f9",
    )
    lbl_erro.pack(pady=10)


eventos = {
    "1850 - Nascimento": "Nasceu em Vassouras (RJ), no auge do ciclo do café.",
    "1872 - Herança & Europa": "Após perder os pais, mudou-se para Paris e assumiu a gestão da fortuna da família.",
    "1873-1930 - Carteira Global": "Investiu em títulos, ações e ferrovias em 13 países e 7 moedas diferentes.",
    "1930 - Legado": "Faleceu deixando sua fortuna para causas sociais e educacionais no Brasil.",
    "1952 - Herança": "O inventário da herança de Eufrásia Teixeira Leite levou 22 anos para ser concluído, devido ao tamanho de sua fortuna que era exorbitante.", 
    "1873 - Relacionamento": "Eufrasia nunca se casou, porém teve uma relacionamento ao longo de 14 anos com o Joaquim Nabuco mas nunca se casou com ele pois queria liberdade financeira e não tinha interesse em se casarqueria ter que dividir seu patrimonio.",
    # herança, relacionamento.
}


for data, detalhe in eventos.items():
    btn = tk.Button(
        janela,
        text=data,
        font=("Arial", 11),
        bg="#00a3e0",
        fg="white",
        relief="flat",
        command=lambda d=detalhe: mostrar_fato(d),
    )
    btn.pack(fill="x", padx=40, pady=6)


janela.mainloop()
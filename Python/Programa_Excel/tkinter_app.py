import customtkinter
from tkinter import messagebox, Toplevel, Scrollbar, Text
import pandas as pd
from mecanica import getLista, getDimensoes, getPneus

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

nome_arquivo = 'dados_carros.xlsx'

df = pd.read_excel(nome_arquivo)

def numero_para_palavra(numero):
    numeros_palavras = {
        '1': 'uma',
        '2': 'duas',
        '3': 'três',
        '4': 'quatro',
        '5': 'cinco',
        '6': 'seis',
        '7': 'sete',
        '8': 'oito',
        '9': 'nove',
        '10': 'dez',
    }
    return numeros_palavras.get(numero, numero)  # Retorna a palavra correspondente ou o próprio número se não estiver na lista

# Restante do código (formatar_descricao, login() e outros trechos)


def formatar_descricao(descricao):
    if "Zonas de ar-condicionado" in descricao:
        numero_zonas = descricao.split(":")[-1].strip()
        if numero_zonas == "1":
            numero_palavra = numero_para_palavra(numero_zonas)
            descricao_formatada = f"Ar condicionado de {numero_palavra} zona"
            return descricao_formatada
        else:
            numero_palavra = numero_para_palavra(numero_zonas)
            descricao_formatada = f"Ar condicionado de {numero_palavra} zonas"
            return descricao_formatada
    else:
        return descricao
    


def login():
    linha_num = entry1.get()
    linha_num = linha_num
    
    try:
        linha_num = int(linha_num)
        linha_num = linha_num - 1
        if 0 <= linha_num < len(df):            
            top = Toplevel(root)
            top.title("Dados")
            seguranca = df.at[linha_num, "Itens de segurança"]
            itens_seguranca = seguranca.split(', ')

            conforto = df.at[linha_num, "Itens de Conforto"]
            itens_conforto = conforto.split(', ')

            itens_conforto = [formatar_descricao(descricao) for descricao in itens_conforto if "Ar-condicionado" not in descricao]
    
            infotenimento = df.at[linha_num, "Itens de Infotenimento"]

            itens_infotenimento = infotenimento.split(', ')

            itens_mecanica = getLista(linha_num)

            itens_dimensoes = getDimensoes(linha_num)

            itens_pneus = getPneus(linha_num)
            #text = "\n".join([f"{col}: {valor}" for col, valor in linha_especifica.items()])
            
            text = "Mecânica\n" + "\n".join([f"•  {valor}" for valor in itens_mecanica]) + "\n\n\n" + \
                    "Segurança\n" + "\n".join([f"•  {valor}" for valor in itens_seguranca]) + "\n\n\n" + \
                    "Conforto\n" + "\n".join([f"•  {valor}" for valor in itens_conforto ]) + "\n\n\n" + \
                    "Infotenimento\n" + "\n".join([f"•  {valor}" for valor in itens_infotenimento]) + "\n\n\n" + \
                    "Dimensões\n" + "\n".join([f"•  {valor}" for valor in itens_dimensoes]) + "\n\n\n" + \
                    "Pneus\n" + "\n".join([f"•  {valor}" for valor in itens_pneus])  


            text_widget = Text(top, wrap="none", font=("Helvetica", 12))
            text_widget.insert("1.0", text)
            text_widget.pack(side="left", fill="both", expand=True)
            
            scrollbar = Scrollbar(top, command=text_widget.yview)
            scrollbar.pack(side="right", fill="y")
            
            text_widget.config(yscrollcommand=scrollbar.set)
        else:
            messagebox.showwarning("Error", "Invalid line number.")
    except ValueError:
        messagebox.showwarning("Error", "Please enter a valid line number.")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx= 60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Pegar dados")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Linha")
entry1.pack(pady=12, padx=10)



button = customtkinter.CTkButton(master=frame, text="Pegar", command=login)

button.pack(pady=12, padx=10)


root.mainloop()

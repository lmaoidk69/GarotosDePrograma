import customtkinter as ctk
import time as t
import App_Cadastro as cadastro
import Dados_Login as dados
import ctkdateentry as ctkde
import datetime as dt

ctk.deactivate_automatic_dpi_awareness()
def abrir_nviagem():

    #Tive que trazer cidades p ca, pois parece que para um dropdown menu, os valores tem que ser definidos no mesmo arquivo, ou seja, não podem ser importados de outro arquivo. Se alguém souber como contornar isso, me avise.
    Cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Brasília", "Curitiba", "Fortaleza", "Manaus", "Recife", "Porto Alegre"]

    NViagem = ctk.CTkToplevel()
    NViagem.geometry("1280x720")
    NViagem.title("Nova Viagem")
    NViagem.grab_set()

    # ── Header ───────────────────────────────────────────────────────────────────
    NviagemFrameT = ctk.CTkFrame(NViagem, height=90, fg_color="#FF5733", corner_radius=0)
    NviagemFrameT.pack(fill="x")
    NviagemFrameT.pack_propagate(False)
    NViagemTitle = ctk.CTkLabel(
        NviagemFrameT, text="Criar Nova Viagem",
        font=ctk.CTkFont(size=40, weight="bold"),
        text_color="white", fg_color="#FF5733"
    )
    NViagemTitle.pack(expand=True, padx=30, anchor="w")

    # ── Form card (centralizado) ─────────────────────────────────────────────────
    NviagemCard = ctk.CTkFrame(NViagem, fg_color="#2D2C2C", corner_radius=15)
    NviagemCard.pack(expand=True)

    NviagemCard.grid_columnconfigure(0, minsize=280)
    NviagemCard.grid_columnconfigure(1, minsize=280)

    LABEL_FONT = ctk.CTkFont(size=17, weight="bold")
    ENTRY_W, ENTRY_H = 250, 42

    # Número de pessoas
    ctk.CTkLabel(NviagemCard, text="Número de pessoas", font=LABEL_FONT).grid(
        row=0, column=0, padx=(40, 20), pady=(40, 12), sticky="w")
    NViagemEntry1 = ctk.CTkEntry(
        NviagemCard, placeholder_text="Ex: 3",
        width=ENTRY_W, height=ENTRY_H, corner_radius=10)
    NViagemEntry1.grid(row=0, column=1, padx=(0, 40), pady=(40, 12), sticky="w")

    # Destino
    ctk.CTkLabel(NviagemCard, text="Destino", font=LABEL_FONT).grid(
        row=1, column=0, padx=(40, 20), pady=12, sticky="w")
    NViagemOptionMenu2 = ctk.CTkOptionMenu(
        NviagemCard, values=Cidades,
        width=ENTRY_W, height=ENTRY_H, corner_radius=10,
        fg_color="#3D3C3C", button_color="#B84025", button_hover_color="#FE6543")
    NViagemOptionMenu2.grid(row=1, column=1, padx=(0, 40), pady=12, sticky="w")

    # Data inicial
    ctk.CTkLabel(NviagemCard, text="Data inicial", font=LABEL_FONT).grid(
        row=2, column=0, padx=(40, 20), pady=12, sticky="w")
    NViagemDate1Entry = ctkde.CTkDateEntry(NviagemCard, width=ENTRY_W, height=ENTRY_H, corner_radius=10)
    NViagemDate1Entry.grid(row=2, column=1, padx=(0, 40), pady=12, sticky="w")

    # Data final
    ctk.CTkLabel(NviagemCard, text="Data final", font=LABEL_FONT).grid(
        row=3, column=0, padx=(40, 20), pady=12, sticky="w")
    NViagemDate2Entry = ctkde.CTkDateEntry(NviagemCard, width=ENTRY_W, height=ENTRY_H, corner_radius=10)
    NViagemDate2Entry.grid(row=3, column=1, padx=(0, 40), pady=12, sticky="w")

    # Botão
    NViagemButton = ctk.CTkButton(
        NviagemCard, text="Criar Viagem",
        width=220, height=45, corner_radius=10,
        font=ctk.CTkFont(size=18, weight="bold"),
        fg_color="#B84025", hover_color="#FE6543", text_color="white",
        command=lambda: criar_viagem())
    NViagemButton.grid(row=4, column=0, columnspan=2, pady=(30, 10))

    # Status
    NViagemStatusLabel = ctk.CTkLabel(
        NviagemCard, text="",
        font=ctk.CTkFont(size=15), text_color="white")
    NViagemStatusLabel.grid(row=5, column=0, columnspan=2, pady=(0, 30))


    def criar_viagem():
        NViagemStatusLabel.configure(text="", text_color="white")

        num_pessoas = NViagemEntry1.get()
        destino = NViagemOptionMenu2.get()
        data_inicial_str = NViagemDate1Entry.entry.get()
        data_final_str = NViagemDate2Entry.entry.get()

        if not num_pessoas.isdigit():
            NViagemStatusLabel.configure(text="Por favor, insira um número válido de pessoas.", text_color="red")
            return

        num_pessoas = int(num_pessoas)

        if not data_inicial_str or not data_final_str:
            NViagemStatusLabel.configure(text="Por favor, selecione as datas da viagem.", text_color="red")
            return

        data_inicial = dt.datetime.strptime(data_inicial_str, "%d/%m/%Y").date()
        data_final = dt.datetime.strptime(data_final_str, "%d/%m/%Y").date()
        hoje = dt.date.today()

        if data_inicial < hoje:
            NViagemStatusLabel.configure(text="A data inicial não pode ser anterior a hoje.", text_color="red")
            return

        if data_inicial >= data_final:
            NViagemStatusLabel.configure(text="A data inicial deve ser anterior à data final.", text_color="red")
            return

        if (data_final - data_inicial).days > 20:
            NViagemStatusLabel.configure(text="A viagem não pode ter mais de 20 dias.", text_color="red")
            return

        nova_viagem = (num_pessoas, destino, data_inicial, data_final)
        dados.MViagens = dados.MViagens + (nova_viagem,)
        NViagemStatusLabel.configure(text="Viagem criada com sucesso!", text_color="green")



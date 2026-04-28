import customtkinter as ctk
import time as t
import App_Cadastro as cadastro
import Dados_Login as dados
import App_NViagem as App_NViagem
def abrir_telaP():
    ctk.deactivate_automatic_dpi_awareness()
    ctk.set_appearance_mode("dark")

    Telap = ctk.CTk()
    Telap.geometry("1280x720")
    Telap.title("Tela Inicial")

    # ── Tab view ──────────────────────────────────────────────────────────────────
    Abas = ctk.CTkTabview(
        Telap,
        fg_color="#1C1C1E",
        segmented_button_fg_color="#2C2C2E",
        segmented_button_selected_color="#FF5733",
        segmented_button_selected_hover_color="#FE6543",
        segmented_button_unselected_color="#2C2C2E",
        segmented_button_unselected_hover_color="#3A3A3C",
        text_color="white",
        text_color_disabled="#8E8E93"
    )
    Abas.pack(fill="both", expand=True)

    Abas.add("Home")
    Abas.add("Viagens")
    Abas.add("Configurações")

    for tab in ["Home", "Viagens", "Configurações"]:
        Abas.tab(tab).grid_columnconfigure(0, weight=1)

    # ── Aba Home ──────────────────────────────────────────────────────────────────
    HomeTab = Abas.tab("Home")

    HeaderHome = ctk.CTkFrame(HomeTab, height=80, fg_color="#FF5733", corner_radius=0)
    HeaderHome.grid(row=0, column=0, sticky="ew")
    HeaderHome.grid_propagate(False)
    ctk.CTkLabel(HeaderHome, text="Bem-vindo!",
        font=ctk.CTkFont(size=38, weight="bold"),
        text_color="white", fg_color="#FF5733"
    ).pack(expand=True, padx=30, anchor="w")

    SubHeader = ctk.CTkFrame(HomeTab, height=52, fg_color="#2C2C2E", corner_radius=0)
    SubHeader.grid(row=1, column=0, sticky="ew")
    SubHeader.grid_propagate(False)
    ctk.CTkLabel(SubHeader, text="Novo por aqui? Veja como começar:",
        font=ctk.CTkFont(size=17, weight="bold"),
        text_color="#AEAEB2", fg_color="#2C2C2E"
    ).pack(expand=True, padx=30, anchor="w")

    CardsFrame = ctk.CTkFrame(HomeTab, fg_color="transparent")
    CardsFrame.grid(row=2, column=0, padx=30, pady=28, sticky="ew")
    CardsFrame.grid_columnconfigure((0, 1, 2), weight=1)

    steps = [
        ("1", "Crie uma viagem", "Acesse a aba Viagens\ne clique em Nova Viagem."),
        ("2", "Defina os detalhes", "Escolha destino,\npessoas e datas."),
        ("3", "Acompanhe", "Veja seu itinerário\ne ajuste quando quiser."),
    ]
    for i, (num, title, desc) in enumerate(steps):
        card = ctk.CTkFrame(CardsFrame, fg_color="#2C2C2E", corner_radius=12)
        card.grid(row=0, column=i, padx=12, pady=8, sticky="nsew")
        ctk.CTkLabel(card, text=num,
            font=ctk.CTkFont(size=34, weight="bold"), text_color="#FF5733",
            fg_color="transparent").pack(pady=(22, 4), padx=22, anchor="w")
        ctk.CTkLabel(card, text=title,
            font=ctk.CTkFont(size=16, weight="bold"), text_color="white",
            fg_color="transparent").pack(padx=22, anchor="w")
        ctk.CTkLabel(card, text=desc,
            font=ctk.CTkFont(size=13), text_color="#8E8E93",
            fg_color="transparent", justify="left").pack(pady=(6, 22), padx=22, anchor="w")

    # ── Aba Viagens ───────────────────────────────────────────────────────────────
    ViagemTab = Abas.tab("Viagens")

    HeaderViagens = ctk.CTkFrame(ViagemTab, height=80, fg_color="#FF5733", corner_radius=0)
    HeaderViagens.grid(row=0, column=0, sticky="ew")
    HeaderViagens.grid_propagate(False)
    ctk.CTkLabel(HeaderViagens, text="Minhas Viagens",
        font=ctk.CTkFont(size=38, weight="bold"),
        text_color="white", fg_color="#FF5733"
    ).pack(expand=True, padx=30, anchor="w")

    BotaoNViagem = ctk.CTkButton(ViagemTab, text="+ Nova Viagem", command=lambda: App_NViagem.abrir_nviagem(),
        width=200, height=46, corner_radius=10,
        font=ctk.CTkFont(size=16, weight="bold"),
        fg_color="#B84025", hover_color="#FE6543", text_color="white")
    BotaoNViagem.grid(row=1, column=0, padx=30, pady=24, sticky="w")

    # ── Aba Configurações ─────────────────────────────────────────────────────────
    ConfigTab = Abas.tab("Configurações")

    HeaderConfig = ctk.CTkFrame(ConfigTab, height=80, fg_color="#FF5733", corner_radius=0)
    HeaderConfig.grid(row=0, column=0, sticky="ew")
    HeaderConfig.grid_propagate(False)
    ctk.CTkLabel(HeaderConfig, text="Configurações",
        font=ctk.CTkFont(size=38, weight="bold"),
        text_color="white", fg_color="#FF5733"
    ).pack(expand=True, padx=30, anchor="w")

    ctk.CTkLabel(ConfigTab, text="Em breve...",
        font=ctk.CTkFont(size=16), text_color="#8E8E93"
    ).grid(row=1, column=0, pady=40)

    Telap.mainloop()

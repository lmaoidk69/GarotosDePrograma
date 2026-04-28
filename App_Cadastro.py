import time as t
import customtkinter as ctk
from PIL import Image, ImageDraw
import Dados_Login as dados

ctk.deactivate_automatic_dpi_awareness()

def _make_hero(w, h):
    img = Image.new("RGBA", (w, h))
    draw = ImageDraw.Draw(img)
    for y in range(h):
        t_ = y / h
        r = int(255 + (110 - 255) * t_)
        g = int(87  + (18  -  87) * t_)
        b = int(51  + (0   -  51) * t_)
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))
    ov = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    od.ellipse([w // 2 - 80, -220,  w + 240,  h // 2 + 20], fill=(255, 140, 85,  55))
    od.ellipse([-220,         h // 2 - 20, w // 3, h + 220], fill=(140, 22,  0,  50))
    od.ellipse([60,   10,    340,   290],                     fill=(255, 210, 150, 28))
    od.ellipse([w - 200, h - 240, w + 100, h + 100],         fill=(180, 45,  5,  40))
    return Image.alpha_composite(img, ov).convert("RGB")

def fazer_cadastro():
    cadastro = ctk.CTkToplevel()
    cadastro.geometry("1280x720")
    cadastro.resizable(False, False)
    cadastro.title("Cadastro de usuário")
    cadastro.grab_set()

    HERO_W = 730
    _hero_pil = _make_hero(HERO_W, 720)
    hero_img = ctk.CTkImage(light_image=_hero_pil, dark_image=_hero_pil, size=(HERO_W, 720))

    # ── Layout principal ──────────────────────────────────────────────────────
    cadastro.grid_columnconfigure(0, weight=0)
    cadastro.grid_columnconfigure(1, weight=1)
    cadastro.grid_rowconfigure(0, weight=1)

    # ── Painel esquerdo (hero) ────────────────────────────────────────────────
    LeftPanel = ctk.CTkFrame(cadastro, fg_color="transparent", corner_radius=0, width=HERO_W)
    LeftPanel.grid(row=0, column=0, sticky="nsew")
    LeftPanel.grid_propagate(False)

    HeroLabel = ctk.CTkLabel(LeftPanel, image=hero_img, text="")
    HeroLabel.place(x=0, y=0, relwidth=1, relheight=1)

    ctk.CTkLabel(LeftPanel, text="✏️",
        font=ctk.CTkFont(size=52), text_color="white",
        fg_color="transparent").place(relx=0.1, rely=0.26)

    ctk.CTkLabel(LeftPanel, text="Crie sua\nConta",
        font=ctk.CTkFont(size=46, weight="bold"), text_color="white",
        fg_color="transparent", justify="left").place(relx=0.1, rely=0.36)

    ctk.CTkLabel(LeftPanel,
        text="Junte-se a nós e comece a\nplanejar sua próxima viagem.",
        font=ctk.CTkFont(size=16), text_color="#FFD4C8",
        fg_color="transparent", justify="left").place(relx=0.1, rely=0.62)

    # ── Painel direito (formulário) ───────────────────────────────────────────
    RightPanel = ctk.CTkFrame(cadastro, fg_color="#1C1C1E", corner_radius=0)
    RightPanel.grid(row=0, column=1, sticky="nsew")
    RightPanel.grid_rowconfigure(0, weight=1)
    RightPanel.grid_rowconfigure(2, weight=1)
    RightPanel.grid_columnconfigure(0, weight=1)

    FormFrame = ctk.CTkFrame(RightPanel, fg_color="transparent")
    FormFrame.grid(row=1, column=0, padx=55, sticky="ew")

    ctk.CTkLabel(FormFrame, text="Criar nova conta",
        font=ctk.CTkFont(size=28, weight="bold"), text_color="white"
    ).pack(anchor="w", pady=(0, 6))

    ctk.CTkLabel(FormFrame, text="Preencha os campos para se cadastrar",
        font=ctk.CTkFont(size=13), text_color="#8E8E93"
    ).pack(anchor="w", pady=(0, 32))

    ctk.CTkLabel(FormFrame, text="USUÁRIO",
        font=ctk.CTkFont(size=11, weight="bold"), text_color="#AEAEB2"
    ).pack(anchor="w", pady=(0, 6))
    CUser = ctk.CTkEntry(FormFrame, placeholder_text="Escolha um nome de usuário",
        width=360, height=44, corner_radius=10,
        border_color="#3A3A3C", fg_color="#2C2C2E", border_width=1)
    CUser.pack(anchor="w", pady=(0, 18))

    ctk.CTkLabel(FormFrame, text="SENHA",
        font=ctk.CTkFont(size=11, weight="bold"), text_color="#AEAEB2"
    ).pack(anchor="w", pady=(0, 6))
    CPass = ctk.CTkEntry(FormFrame, placeholder_text="Crie uma senha", show="*",
        width=360, height=44, corner_radius=10,
        border_color="#3A3A3C", fg_color="#2C2C2E", border_width=1)
    CPass.pack(anchor="w", pady=(0, 28))

    CStatus = ctk.CTkLabel(FormFrame, text="",
        font=ctk.CTkFont(size=14), text_color="white")
    CStatus.pack(anchor="w")

    def salvar_cadastro():
        usernameCad = CUser.get()
        passwordCad = CPass.get()
        if usernameCad and passwordCad:
            dados.DicLog[usernameCad] = passwordCad
            CStatus.configure(text="Cadastro realizado com sucesso!", text_color="#30D158")
            cadastro.after(800, cadastro.destroy)
        else:
            CStatus.configure(text="Usuário e senha não podem ser vazios.", text_color="#FF453A")

    CBotao = ctk.CTkButton(FormFrame, text="Cadastrar",
        width=360, height=46, corner_radius=10,
        font=ctk.CTkFont(size=16, weight="bold"),
        fg_color="#FF5733", hover_color="#FE6543", text_color="white",
        command=salvar_cadastro)
    CBotao.pack(anchor="w", pady=(0, 20))


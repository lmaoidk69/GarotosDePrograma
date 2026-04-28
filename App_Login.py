import customtkinter as ctk
from PIL import Image, ImageDraw
import App_Cadastro as cadastro
import Dados_Login as dados
import App_TelaP as App_TelaP
import App_NViagem as App_NViagem

ctk.deactivate_automatic_dpi_awareness()
ctk.set_appearance_mode("dark")

incial = ctk.CTk()
incial.geometry("1280x720")
incial.resizable(False, False)
incial.title("Aplicativo de viagem")

# ── Hero image gerada com PIL ─────────────────────────────────────────────────
def _make_hero(w, h):
    img = Image.new("RGBA", (w, h))
    draw = ImageDraw.Draw(img)
    for y in range(h):
        t = y / h
        r = int(255 + (110 - 255) * t)
        g = int(87  + (18  -  87) * t)
        b = int(51  + (0   -  51) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))
    ov = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    od.ellipse([w // 2 - 80, -220,  w + 240,  h // 2 + 20], fill=(255, 140, 85,  55))
    od.ellipse([-220,         h // 2 - 20, w // 3, h + 220], fill=(140, 22,  0,  50))
    od.ellipse([60,   10,    340,   290],                     fill=(255, 210, 150, 28))
    od.ellipse([w - 200, h - 240, w + 100, h + 100],         fill=(180, 45,  5,  40))
    return Image.alpha_composite(img, ov).convert("RGB")

HERO_W = 730
_hero_pil = _make_hero(HERO_W, 720)
hero_img = ctk.CTkImage(light_image=_hero_pil, dark_image=_hero_pil, size=(HERO_W, 720))

# ── Layout principal ──────────────────────────────────────────────────────────
incial.grid_columnconfigure(0, weight=0)
incial.grid_columnconfigure(1, weight=1)
incial.grid_rowconfigure(0, weight=1)

# ── Painel esquerdo (hero) ────────────────────────────────────────────────────
LeftPanel = ctk.CTkFrame(incial, fg_color="transparent", corner_radius=0, width=HERO_W)
LeftPanel.grid(row=0, column=0, sticky="nsew")
LeftPanel.grid_propagate(False)

HeroLabel = ctk.CTkLabel(LeftPanel, image=hero_img, text="")
HeroLabel.place(x=0, y=0, relwidth=1, relheight=1)

ctk.CTkLabel(LeftPanel, text="✈",
    font=ctk.CTkFont(size=52), text_color="white",
    fg_color="transparent").place(relx=0.1, rely=0.26)

ctk.CTkLabel(LeftPanel, text="Aplicativo\nde Viagem",
    font=ctk.CTkFont(size=46, weight="bold"), text_color="white",
    fg_color="transparent", justify="left").place(relx=0.1, rely=0.36)

ctk.CTkLabel(LeftPanel,
    text="Planeje sua próxima aventura\ncom facilidade e estilo.",
    font=ctk.CTkFont(size=16), text_color="#FFD4C8",
    fg_color="transparent", justify="left").place(relx=0.1, rely=0.62)

# ── Painel direito (formulário) ───────────────────────────────────────────────
RightPanel = ctk.CTkFrame(incial, fg_color="#1C1C1E", corner_radius=0)
RightPanel.grid(row=0, column=1, sticky="nsew")
RightPanel.grid_rowconfigure(0, weight=1)
RightPanel.grid_rowconfigure(2, weight=1)
RightPanel.grid_columnconfigure(0, weight=1)

FormFrame = ctk.CTkFrame(RightPanel, fg_color="transparent")
FormFrame.grid(row=1, column=0, padx=55, sticky="ew")

ctk.CTkLabel(FormFrame, text="Bem-vindo de volta",
    font=ctk.CTkFont(size=28, weight="bold"), text_color="white"
).pack(anchor="w", pady=(0, 6))

ctk.CTkLabel(FormFrame, text="Entre com suas credenciais para continuar",
    font=ctk.CTkFont(size=13), text_color="#8E8E93"
).pack(anchor="w", pady=(0, 32))

ctk.CTkLabel(FormFrame, text="USUÁRIO",
    font=ctk.CTkFont(size=11, weight="bold"), text_color="#AEAEB2"
).pack(anchor="w", pady=(0, 6))
TUser = ctk.CTkEntry(FormFrame, placeholder_text="Digite seu usuário",
    width=360, height=44, corner_radius=10,
    border_color="#3A3A3C", fg_color="#2C2C2E", border_width=1)
TUser.pack(anchor="w", pady=(0, 18))

ctk.CTkLabel(FormFrame, text="SENHA",
    font=ctk.CTkFont(size=11, weight="bold"), text_color="#AEAEB2"
).pack(anchor="w", pady=(0, 6))
TPass = ctk.CTkEntry(FormFrame, placeholder_text="Digite sua senha", show="*",
    width=360, height=44, corner_radius=10,
    border_color="#3A3A3C", fg_color="#2C2C2E", border_width=1)
TPass.pack(anchor="w", pady=(0, 28))

TBotao = ctk.CTkButton(FormFrame, text="Entrar",
    width=360, height=46, corner_radius=10,
    font=ctk.CTkFont(size=16, weight="bold"),
    fg_color="#FF5733", hover_color="#FE6543", text_color="white",
    command=lambda: validar_login())
TBotao.pack(anchor="w", pady=(0, 16))

# Divisor "ou"
DivRow = ctk.CTkFrame(FormFrame, fg_color="transparent")
DivRow.pack(anchor="w", fill="x", pady=(0, 16))
ctk.CTkFrame(DivRow, height=1, fg_color="#3A3A3C").pack(
    side="left", fill="x", expand=True, padx=(0, 10), pady=7)
ctk.CTkLabel(DivRow, text="ou",
    font=ctk.CTkFont(size=13), text_color="#8E8E93").pack(side="left")
ctk.CTkFrame(DivRow, height=1, fg_color="#3A3A3C").pack(
    side="left", fill="x", expand=True, padx=(10, 0), pady=7)

TBotaocadastro = ctk.CTkButton(FormFrame, text="Criar nova conta",
    width=360, height=46, corner_radius=10,
    font=ctk.CTkFont(size=16),
    fg_color="transparent", hover_color="#2C2C2E",
    text_color="#FF5733", border_width=1, border_color="#FF5733",
    command=cadastro.fazer_cadastro)
TBotaocadastro.pack(anchor="w", pady=(0, 20))

Tlogin_status = ctk.CTkLabel(FormFrame, text="",
    font=ctk.CTkFont(size=14), text_color="white")
Tlogin_status.pack(anchor="w")


def validar_login():
    usernameLog = TUser.get()
    passwordLog = TPass.get()
    if usernameLog in dados.DicLog and dados.DicLog[usernameLog] == passwordLog:
        Tlogin_status.configure(text=f"Bem-vindo, {usernameLog}!", text_color="#30D158")
        incial.after(800, lambda: [incial.destroy(), App_TelaP.abrir_telaP()])
    else:
        Tlogin_status.configure(text="Credenciais inválidas. Tente novamente.", text_color="#FF453A")


incial.mainloop()

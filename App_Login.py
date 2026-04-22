import customtkinter as ctk
import time as t
import App_Cadastro as cadastro
import Dados_Login as dados

ctk.deactivate_automatic_dpi_awareness()
# Configurações iniciais login

ctk.set_appearance_mode("dark")
incial = ctk.CTk()
incial.geometry("1280x720")
incial.title("Aplicativo de viagem")

def validar_login():
    usernameLog = TUser.get()
    passwordLog = TPass.get()
    
    if usernameLog in dados.DicLog and dados.DicLog[usernameLog] == passwordLog:
        print("Login bem-sucedido!")
        Tlogin_status.configure(text=f"Login bem-sucedido! Bem-vindo, {usernameLog}!", text_color="green")
        t.sleep(2)
        incial.destroy()  

    else:
        Tlogin_status.configure(text="Credenciais inválidas. Tente novamente.", text_color="red")

#UI
TTitulo = ctk.CTkLabel(incial, text="Bem-vindo ao aplicativo de viagem!")
TTitulo.pack(pady=20)

TUser = ctk.CTkEntry(incial ,placeholder_text="Username")
TUser.pack(pady=10)

TPass = ctk.CTkEntry(incial,placeholder_text="Password", show="*")
TPass.pack(pady=10)

TBotao = ctk.CTkButton(incial, text="Login", command=validar_login, width=100, height=40, corner_radius=10)
TBotao.pack(pady=10)

TBotaocadastro = ctk.CTkButton(incial, text="Cadastrar", command=cadastro.fazer_cadastro, width=100, height=40, corner_radius=10)
TBotaocadastro.pack(pady=10)

Tlogin_status = ctk.CTkLabel(incial, text="")
Tlogin_status.pack(pady=10)


incial.mainloop()
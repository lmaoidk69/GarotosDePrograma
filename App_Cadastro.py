import time as t
import customtkinter as ctk
import Dados_Login as dados

ctk.deactivate_automatic_dpi_awareness()

def fazer_cadastro():


    ctk.set_appearance_mode("dark")
    cadastro = ctk.CTk()
    cadastro.geometry("1280x720")
    cadastro.title("Cadastro de usuário")

    CUser = ctk.CTkEntry(cadastro, placeholder_text="Username")
    CUser.pack(pady=10)

    CPass = ctk.CTkEntry(cadastro, placeholder_text="Password", show="*")
    CPass.pack(pady=10)
    #Funções:
    
    def salvar_cadastro():
        usernameCad = CUser.get()
        passwordCad = CPass.get()
        
        if usernameCad and passwordCad:
            dados.DicLog[usernameCad] = passwordCad
            print("Cadastro realizado com sucesso!")
            t.sleep(2)
            cadastro.destroy()
        else:
            print("Username e Password não podem ser vazios.")
    
    CBotao = ctk.CTkButton(cadastro, text="Salvar", command=salvar_cadastro, width=100, height=40, corner_radius=10)
    CBotao.pack(pady=10)


    
    cadastro.mainloop()

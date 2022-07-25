import tkinter.messagebox
from tkinter import *
import customtkinter
import mysql.connector
import re

def cadastrar():
    global user
    conexao =mysql.connector.connect (
    host='localhost',
    user='root',
    password='Rodrigo1995@',
    database='teste_bancodados'
)

    regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    def chek_email(email):
        if (re.search(regex,email)):
              pass
        else:
            return False


    cadastr= (ent_log.get(),ent_senha.get())
    chek_email(cadastr[0])
    if cadastr[0]=='' or cadastr[1] == '':
        return tkinter.messagebox.showwarning(title='Aviso de erro ',message='Os campos de login e senha devem estar preenchidos!!!')
    elif cadastr[0] == cadastr[1]:
        ent_log.delete(0,END)
        ent_senha.delete(0,END)
        return tkinter.messagebox.showwarning(message='Usuário e senha devem ser diferentes!!!')
    elif chek_email(cadastr[0]) == False:
        ent_log.delete(0, END)
        ent_senha.delete(0, END)
        return tkinter.messagebox.showwarning(message='Por Favor utilize um e-mail valido !!!')
    else:
        cursor = conexao.cursor()
        comando = f'INSERT INTO usuarios(nome,senha)VALUES ("{cadastr[0]}","{cadastr[1]}")'
        cursor.execute(comando)
        conexao.commit()
        ent_log.delete(0, END)
        ent_senha.delete(0, END)
        return tkinter.messagebox.showinfo(message=f'Cadastro realizado com sucesso!')




def buscar_login():
    global user
    conexao =mysql.connector.connect(
    host='localhost',
    user='root',
    password='Rodrigo1995@',
    database='teste_bancodados'

)
    cadastr= (ent_log.get(),ent_senha.get())
    if cadastr[0]=='' or cadastr[1] == '':
        ent_log.delete(0, END)
        ent_senha.delete(0, END)
        return tkinter.messagebox.showwarning(title='Aviso de erro ',message='Os campos de login e senha devem estar preenchidos!!!')
    else:
        cursor = conexao.cursor()
        comando = f'SELECT  nome,senha FROM usuarios'
        cursor.execute(comando)
        resultado =cursor.fetchall()
        for c in resultado:
            if cadastr[0] and cadastr[1] in c:
                user= c
        if user in resultado:
            ent_log.delete(0, END)
            ent_senha.delete(0, END)
            return tkinter.messagebox.showinfo(message=f'Login efetuado com sucesso seja bem vindo {user[0]}!')
        else:
            ent_log.delete(0, END)
            ent_senha.delete(0, END)
            return tkinter.messagebox.showwarning(message=f'Senha ou e-mail incorretos!')






cor = '#60a3c4'
corbt= '#134c69'
user = ""
customtkinter.set_appearance_mode("light")
root = customtkinter.CTk()
root.geometry(f"{300}x{140}")
root.config(bg=cor)
login = Label(root, text="E-mail",bg=cor,pady= 5,padx= 4)
login.place(x=20, y=30)

esconder_senha= StringVar()


ent_log =customtkinter.CTkEntry(root, placeholder_text="E-mail",width=150,height=20,border_width=2,corner_radius=10)
ent_log.place(x=80, y= 20)


senha = Label(root, text="Senha",bg=cor)
senha.place(x=20, y=100)

ent_senha = customtkinter.CTkEntry(root, placeholder_text="Senha",textvariable=esconder_senha,show='*',width=150,height=20,border_width=2,corner_radius=10)
ent_senha.place(x=80, y=67 )
#botâo novo usuario
novo_us=customtkinter.CTkButton(root, text="Novo usuário",bg=corbt, width=10, height=10,command=cadastrar)
novo_us.place(x=14, y=100)
#botâo login
log=customtkinter.CTkButton(root, text="Login", bg=corbt,width=10, height=10 ,command=buscar_login)
log.place(x=130, y=100)
#botâo logout
sair=customtkinter.CTkButton(root, text="Sair",bg=corbt,width=10, height=10 ,command=root.destroy,)
sair.place(x=210, y=100)

root.mainloop()
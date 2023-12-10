from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser
import os

# variavel jan de janela
jan = Tk()
jan.title("OS Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False) # para ele não ser responsivel
jan.attributes("-alpha", 0.9)

# ====== carregar imagens ====
Logo = PhotoImage(file="icon/os.png")

# ====== widgets ========
leftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
leftFrame.pack(side=LEFT) # frame da esquerda

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

# ==== gerar imagem ====
LogoLabel = Label(leftFrame, image=Logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

# === Login ====
UserLabel = Label(RightFrame, text="Username: ",font=("Century Gothic", 20) ,bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=100)
UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)
#
PassLabel = Label(RightFrame, text="Password: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=5, y=150) # y é a altura
PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=150, y=160)

# === button ====
def Login():
    UserLogin = UserEntry.get()
    PassLogin = PassEntry.get()
    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """, (UserLogin, PassLogin))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if(UserLogin in VerifyLogin and PassLogin in VerifyLogin):
            messagebox.showinfo(title="Aviso de Login", message="Acesso Confirmado!")
        else:
            pass
    except:
        messagebox.showinfo(title="Aviso de Login", message="Acesso Negado, Usuario ou Senha incorreta")

LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=225)

def Register():
    # Removendo botoes de login é Register
    LoginButton.place(x=60000)
    RegisterButton.place(x=60000)
    # Inserindo windgts de cadastro
    NomeLabel = Label(RightFrame, text="Name: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=5, y=5)
    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=100, y=19)
    # ====================
    EmailLabel = Label(RightFrame, text="Email: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5, y=55)
    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=100, y=69)
    # ======== button =========
    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()
        if (Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Register error", message="Não deixe nenhum campo vazio")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES (?, ?, ?, ?)                   
            """, (Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta criada com sucesso")

    Register = ttk.Button(RightFrame, text="Registrar", width=30, command=RegisterToDataBase)
    Register.place(x=100, y=225)
    def BackToLogin():
        # removendo widgets de cadastro
        NomeLabel.place(x=60000)
        NomeEntry.place(x=60000)
        EmailLabel.place(x=60000)
        EmailEntry.place(x=60000)
        Register.place(x=60000)
        Back.place(x=60000)
        # trazendo os widgets do login
        LoginButton.place(x=100)
        RegisterButton.place(x=115)
    Back = ttk.Button(RightFrame, text="Sair", width=20, command=BackToLogin)
    Back.place(x=115, y=255)

RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=115, y=255)
# loop para iniciar o programa
jan.mainloop()
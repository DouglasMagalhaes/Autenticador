from tkinter import *

class Logins:
    banco_de_dados = {
        'user@gmail.com': 'senha123',
        'douglas@gmail.com': 'vai_se-lascar',
    }

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def autenticar(self):
        if self.email in Logins.banco_de_dados:
            if Logins.banco_de_dados[self.email] == self.password:
                return True
        return False

# Função de botao de entrada
def verificar_login():
    email = email_entry.get()
    senha = password_entry.get()

    logins = Logins(email, senha)
    if logins.autenticar():
        resultado_label.config(text="Login autorizado", fg="lime")
    else:
        resultado_label.config(text="Email ou senha incorretos", fg="red")


# Criando janela
janela = Tk()
janela.configure(bg="black")
janela.geometry("300x200")
janela.title("Autenticação")

# Titulo
titulo = Label(janela, text="Autenticação de Login", bg="black", fg="green")
titulo.place(x=90, y=10)

# Email
email_label = Label(janela, text="Digite seu email", bg="black", fg="green")
email_label.place(x=20, y=40)

# Entrada do email
email_entry = Entry(janela, bg="white", fg="black")
email_entry.place(x=125, y=40)

# Senha
password_label = Label(janela, text="Digite sua senha", bg="black", fg="green")
password_label.place(x=20, y=80)

# Entrada da senha
password_entry = Entry(janela, bg="white", fg="black")
password_entry.place(x=125, y=80)

# Botoao de Resultado
resultado_button = Button(janela, text="Resultado", bg="white", fg="green", width=10, command=verificar_login)
resultado_button.place(x=110, y=125)

# Label de Resultado
resultado_label = Label(janela, text="", bg="black", fg="green", font=("Arial", 10, "bold"))
resultado_label.place(x=70, y=170)

janela.mainloop()
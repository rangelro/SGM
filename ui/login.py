import tkinter as tk
from tkinter import messagebox
from ui.adminpanel import AdminPanel
from data.admin import Admin
import sqlite3

class LoginPanel:
    """
    Classe que representa a tela de login.

    Atributos:
        root (Tk): A janela principal da aplicação.
        label_sgm (Label): Rótulo para exibir "SGM v1".
        label_user (Label): Rótulo para exibir "Usuário".
        entry_user (Entry): Caixa de texto para inserir o nome de usuário.
        label_password (Label): Rótulo para exibir "Senha".
        entry_password (Entry): Caixa de texto para inserir a senha.
        button_confirm (Button): Botão para confirmar o login.
    """

    def __init__(self, root):
        """
        Inicializa a tela de login.

        Parâmetros:
            root (Tk): A janela principal da aplicação.
        """
        # Definir janela
        self.root = root
        self.root.title("SGM v1")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Adicionar label de titulo
        self.label_sgm = tk.Label(root, text="SGM v1", font=("Helvetica", 24))
        self.label_sgm.pack(pady=20)

        # Adicionar label do texto de usuário
        self.label_user = tk.Label(root, text="Usuário:")
        self.label_user.pack()

        # Adicionar caixa de texto do usuário
        self.entry_user = tk.Entry(root)
        self.entry_user.pack()

        # Adicionar label da senha
        self.label_password = tk.Label(root, text="Senha:")
        self.label_password.pack()

        # Adicionar caixa de texto da senha
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack()

        # Adicionar botão de confirmação
        self.button_confirm = tk.Button(root, text="Confirmar", command=self.validate_login)
        self.button_confirm.pack(pady=20)

    def validate_login(self):
        """
        Valida as credenciais inseridas pelo usuário e exibe uma mensagem de login.

        A mensagem exibida depende se as credenciais são válidas ou não.
        """
        user = self.entry_user.get()
        password = self.entry_password.get()
        
        # Connectar ao banco de dados para fazer o login
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        query = '''SELECT * FROM Users WHERE username = ? AND password = ? AND is_active = 1;'''
        cursor.execute(query, (user, password))
        result = cursor.fetchone()
        conn.close() # Fechar conexão
        
        # Lógica de validação do login
        if result:
            messagebox.showinfo("Login", "Login bem-sucedido!")
            
            # Fechar janela de login e abrir janela do usuário
            self.root.destroy()
            new_root = tk.Tk()
            admin_panel = AdminPanel(new_root, Admin(result[1]))
            new_root.mainloop()
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos.")
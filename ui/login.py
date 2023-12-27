import tkinter as tk
from tkinter import messagebox
from ui.adminpanel import AdminPanel
from ui.cashierpanel import CashierPanel
from ui.stockpanel import StockPanel
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
        self.__root = root
        self.__root.title("SGM v1")
        self.__root.geometry("500x400")
        self.__root.resizable(False, False)

        # Adicionar label de titulo
        self.__label_sgm = tk.Label(root, text="SGM v1", font=("Helvetica", 24))
        self.__label_sgm.pack(pady=20)

        # Adicionar label do texto de usuário
        self.__label_user = tk.Label(root, text="Usuário:")
        self.__label_user.pack()

        # Adicionar caixa de texto do usuário
        self.__entry_user = tk.Entry(root)
        self.__entry_user.pack()

        # Adicionar label da senha
        self.__label_password = tk.Label(root, text="Senha:")
        self.__label_password.pack()

        # Adicionar caixa de texto da senha
        self.__entry_password = tk.Entry(root, show="*")
        self.__entry_password.pack()

        # Adicionar botão de confirmação
        self.__button_confirm = tk.Button(root, text="Confirmar", command=self.validate_login)
        self.__button_confirm.pack(pady=20)

    def validate_login(self):
        """
        Valida as credenciais inseridas pelo usuário e exibe uma mensagem de login.

        A mensagem exibida depende se as credenciais são válidas ou não.
        """
        user = self.__entry_user.get()
        password = self.__entry_password.get()
        
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
            self.__root.destroy()
            new_root = tk.Tk()
            # Verificar tipo de usuário para criar o novo usuário com base em seu tipo e abrir sua respectiva janela
            if result[3] == "Admin":
                window = AdminPanel(new_root, Admin(result[1]))
            elif result[3] == "Stockist":
                window = StockPanel(new_root, Admin(result[1]))
            elif result[3] == "Cashier":
                window = CashierPanel(new_root, Admin(result[1]))
            else:
                messagebox.showerror("Login", "Usuário sem cargo definido, verifique com seu administrador!")
            new_root.mainloop()
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos.")
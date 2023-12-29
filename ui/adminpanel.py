import tkinter as tk
from tkinter import messagebox, simpledialog
from data.admin import Admin
from data.stockist import Stockist
from data.user import User

class AdminPanel:
    """
    Classe que representa o painel de administração (CRUD).

    Atributos:
        root (Tk): A janela principal da aplicação.
        lista_users (list): Lista de usuários.
        listbox_users (Listbox): Widget Listbox para exibir usuários.
        button_add (Button): Botão para adicionar um novo usuário.
        button_edit (Button): Botão para editar um usuário.
        button_disable (Button): Botão para desativar um usuário.
    """

    def __init__(self, root, user):
        """
        Inicializa o painel de administração.

        Parâmetros:
            root (Tk): A janela principal da aplicação.
        """
        # Definindo variavel de usuário
        self.__user = user

        self.__root = root
        self.__root.title("Admin Panel")
        self.__root.geometry("800x600")

        self.__label_title = tk.Label(root, text="Lista de Usuários", font=("Helvetica", 24))
        self.__label_title.pack(pady=20)

        # Definindo lista de usuario
        self.__list_users = []
        
        # Exibindo a lista de usuários
        self.__listbox_users = tk.Listbox(root)
        self.__listbox_users.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)  # Ocupa toda a largura com margens de 20px
        
        # Atualizar lista de usuarios
        self.update_users()

        # Botões de ação
        self.button_add = tk.Button(root, text="Adicionar Usuário", command=self.add_user)
        self.button_add.pack(side=tk.LEFT, padx=20, pady=10)

        self.button_edit = tk.Button(root, text="Editar Usuário", command=self.edit_user)
        self.button_edit.pack(side=tk.LEFT, padx=20, pady=10)

        self.button_disable = tk.Button(root, text="Desativar Usuário", command=self.disable_user)
        self.button_disable.pack(side=tk.LEFT, padx=20, pady=10)
        
        self.button_enable = tk.Button(root, text="Ativar Usuário", command=self.enable_user)
        self.button_enable.pack(side=tk.LEFT, padx=20, pady=10)
    
    # Preencher lista de usuarios
    def update_users(self):
        # Buscar todos os usuários do banco de dados
        result = self.__user.all_users()
        self.__list_users.clear() # Limpar lista de usuário do painel para evitar duplicatas
        self.__listbox_users.delete(0, 'end') # Limpar listbox
        
        for user in result:
            self.__list_users.append(user) # Adicionar usuário a lista
            self.__listbox_users.insert(tk.END, f"{user[1]} - {user[3]} | {'Ativo' if user[4] != 0 else 'Desativado'}") # Adicionar no listbox

    def add_user(self):
        """
        Adiciona um novo usuário à lista.
        """
        username=simpledialog.askstring("Adicionar usuario","Digite o nome do usuário: ",parent=self.__root)
        password=simpledialog.askstring("Adicionar usuario","Digite a senha do usuário: ",parent=self.__root)
        user_type=simpledialog.askstring("Adicionar usuario","Qual o cargo do usuário (Admin, Cashier, Stockist): ",parent=self.__root)
        
        if self.__user.add_user(username, password, user_type):
            self.update_users() # Atualiza lista após adicionar
        else:
            messagebox.showerror("Adicionar usuario","Usuário já existe no sistema.")
        

    def edit_user(self):
        """
        Edita o usuário selecionado na lista.
        """
        selected_index = self.__listbox_users.curselection()
        if selected_index:
            # Identifica qual usuário está selecionado na lista
            selected_user = self.__list_users[selected_index[0]]
            
            if selected_user:
                name = simpledialog.askstring("Editar Usuario", "Digite o novo nome do usuario:", initialvalue=selected_user[1], parent=self.__root)
                password = simpledialog.askstring("Editar Usuario", "Digite a nova senha do usuario:", initialvalue=selected_user[2], parent=self.__root)
                user_type = simpledialog.askstring("Editar usuario","Qual o novo cargo do usuário (Admin, Cashier, Stockist): ",initialvalue=selected_user[3], parent=self.__root)

                self.__user.edit_user(selected_user[0], name, password, user_type)
                self.update_users() # Atualiza lista
                messagebox.showinfo("Editar Usuario", f"Usuário '{selected_user[1]}' editado com sucesso.")
        else:
            messagebox.showwarning("Editar Usuario", "Não há nenhum usuário selecionado no momento, por gentileza selecionar um usuário.")
    

    def disable_user(self):
        """
        Desativa o usuário selecionado na lista.
        """
        selected_index = self.__listbox_users.curselection()
        if selected_index:
            selected_user = self.__list_users[selected_index[0]]
            self.__user.disable_user(selected_user[0])
            self.update_users()
            messagebox.showinfo("Admin Panel", f"Usuário '{selected_user[1]}' desativado com sucesso!")
        else:
            messagebox.showwarning("Admin Panel", "Selecione um usuário para desativar.")

    def enable_user(self):
        """
        Ativa o usuário selecionado na lista.
        """
        selected_index = self.__listbox_users.curselection()
        if selected_index:
            selected_user = self.__list_users[selected_index[0]]
            self.__user.active_user(selected_user[0])
            self.update_users()
            messagebox.showinfo("Admin Panel", f"Usuário '{selected_user}' ativado com sucesso!")
        else:
            messagebox.showwarning("Admin Panel", "Selecione um usuário para ativar.")

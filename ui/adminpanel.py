import tkinter as tk
from tkinter import messagebox, simpledialog
from data.admin import Admin




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
        #Definindo variaveis de usuário
        self.__user = user

        self.__root = root
        self.__root.title("Admin Panel")
        self.__root.geometry("800x600")

        self.__label_title = tk.Label(root, text="Lista de Usuários", font=("Helvetica", 24))
        self.__label_title.pack(pady=20)

        #Definindo lista de usuario
        self.__lista_users = []
        

       

        # Exibindo a lista de usuários
        self.__listbox_users = tk.Listbox(root)
        for user in self.__lista_users:
            self.__listbox_users.insert(tk.END, user)
        self.__listbox_users.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)  # Ocupa toda a largura com margens de 20px
        #Atualizar lista de usuarios
        self.update_users()

        # Botões de ação
        self.button_add = tk.Button(root, text="Adicionar Usuário", command=self.add_user)
        self.button_add.pack(side=tk.LEFT, padx=20, pady=10)

        self.button_edit = tk.Button(root, text="Editar Usuário", command=self.edit_user)
        self.button_edit.pack(side=tk.LEFT, padx=20, pady=10)

        self.button_disable = tk.Button(root, text="Desativar Usuário", command=self.disable_user)
        self.button_disable.pack(side=tk.LEFT, padx=20, pady=10)
     #Preencher lista de usuarios
    def update_users(self):
        result =self.__user.all_users()
        self.__lista_users.clear()
        for user in result:
            if user[3] == "Admin":
                new_user = Admin(user[1])
            self.__lista_users.append(new_user)
            self.__listbox_users.insert(tk.END, user[1])

    def add_user(self):
        """
        Adiciona um novo usuário à lista.
        """
        username=simpledialog.askstring("Adicionar usuario","Digite o nome do usuário: ",parent=self.__root)
        password=simpledialog.askstring("Adicionar usuario","Digite a senha do usuário: ",parent=self.__root)
        user_type=simpledialog.askstring("Adicionar usuario","Qual o cargo do usuário (Admin, Cashier, Stockist): ",parent=self.__root)
        if self.__user.add_user(username,password,user_type):
            self.__listbox_users.insert(tk.END, username)
        else:
            messagebox.showerror("Adicionar usuario","Usuário já existe no sistema.")
        

    def edit_user(self):
        """
        Edita o usuário selecionado na lista.
        """
        
        selected_index = self.__listbox_users.curselection()
        if selected_index:
            #Seleciona o usuário que está sendo buscado
            selected_user = self.__lista_users[selected_index[0]]
            #Info
            name = simpledialog.askstring("Editar Usuario", "Digite o novo nome do usuario:", initialvalue=self.__lista_users["Nome"], parent=self.__root)
            password = simpledialog.askstring("Editar Usuario", "Digite a nova senha do usuario:", initialvalue=["Nome"], parent=self.__root)
            user_type=simpledialog.askstring("Editar usuario","Qual o novo cargo do usuário (Admin, Cashier, Stockist): ",parent=self.__root)

            if self.__user.edit_user(id,name,password,user_type):
                self.__listbox_users.insert(tk.CURRENT,name)
            else:
                messagebox.showerror("Editar Usuario","Usuario inexistente.")
            
            messagebox.showinfo("Editar Usuario", f"Usuário '{selected_user}' editado com sucesso.")
        else:
            messagebox.showwarning("Editar Usuario", "Usuario inválido.")

        
        

    def disable_user(self):
        """
        Desativa o usuário selecionado na lista.
        """
        selected_index = self.__listbox_users.curselection()
        if selected_index:
            selected_user = self.__lista_users[selected_index[0]]
            del self.__lista_users[selected_index[0]]
            self.__listbox_users.delete(selected_index)
            messagebox.showinfo("Admin Panel", f"Usuário '{selected_user}' desativado com sucesso!")
        else:
            messagebox.showwarning("Admin Panel", "Selecione um usuário para desativar.")

    def active_user(self):
        """
        Ativa o usuário selecionado na lista.
        """
        selected_index = self.__listbox_users.curselection()
        if selected_index:
            selected_user = self.__lista_users[selected_index[0]]

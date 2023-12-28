import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from data.product import Product
import sqlite3

class StockPanel:
    """
    Classe que representa o painel de estoque.

    Atributos:
        root (Tk): A janela principal da aplicação.
        tree (ttk.Treeview): Widget Treeview para exibir produtos.
        products (list): Lista de produtos.
        button_add (Button): Botão para adicionar um novo produto.
        button_edit (Button): Botão para editar um produto.
        button_remove (Button): Botão para remover um produto.
    """

    def __init__(self, root, user):
        """
        Inicializa o painel de estoque.

        Parâmetros:
            root (Tk): A janela principal da aplicação.
            user (Stockist): Usuário que irá operar o estoque.
        """
        # Definindo usuário operador do estoque
        self.__user = user
        
        self.__root = root
        self.__root.title("Painel de Estoque")
        self.__root.geometry("800x600")

        self.__label_title = tk.Label(root, text="Lista de Produtos", font=("Helvetica", 24))
        self.__label_title.pack(pady=20)

        # Integração com banco de dados
        self.__conn = sqlite3.connect("database.db")
        self.__cursor = self.__conn.cursor()
        
        # Criar lista de produtos
        self.__products = []
        
        # Verificar se a tabela dos produtos existe, caso não criar uma nova
        query = '''CREATE TABLE IF NOT EXISTS Stock (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    code TEXT NOT NULL,
                    value REAL NOT NULL,
                    validity TEXT NOT NULL,
                    quantity INTEGER NOT NULL
                );'''
        self.__cursor.execute(query)
        self.__conn.commit()
        
        # Carregar produtos na lista
        self.update_list()

        # Configurando a tabela (Treeview)
        self.__tree = ttk.Treeview(root, columns=("id", "name", "code", "qt", "unit_value"), show="headings")
        self.__tree.heading("id", text="ID")
        self.__tree.heading("name", text="Nome")
        self.__tree.heading("code", text="Código")
        self.__tree.heading("qt", text="Quantidade")
        self.__tree.heading("unit_value", text="Valor Unitário")
        self.__tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Preenchendo a tabela com dados
        self.update_table()

        # Botões de ação
        self.__button_add = tk.Button(root, text="Adicionar Produto", command=self.add_product)
        self.__button_add.pack(side=tk.LEFT, padx=20, pady=10)

        self.__button_edit = tk.Button(root, text="Editar Produto", command=self.edit_product)
        self.__button_edit.pack(side=tk.LEFT, padx=20, pady=10)

        self.__button_remove = tk.Button(root, text="Remover Produto", command=self.remove_product)
        self.__button_remove.pack(side=tk.LEFT, padx=20, pady=10)

    def update_list(self):
        # Carregar tabela a partir do banco de dados
        query = '''SELECT * FROM Stock'''
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        
        # Limpar lista antes de adicionar novos valores
        self.__products.clear()
        
        for p in result:
            self.__products.append(Product(p[0], p[1], p[2], p[3], p[4], p[5]))

    def update_table(self):
        """
        Atualiza a tabela com os dados dos produtos.
        """
        # Limpando itens existentes na tabela
        for item in self.__tree.get_children():
            self.__tree.delete(item)

        # Preenchendo a tabela com os dados da lista de produtos
        for product in self.__products:
            self.__tree.insert("", "end", values=(product.get_id(), 
                                                  product.get_name(), 
                                                  product.get_code(), 
                                                  product.get_amount(), 
                                                  product.get_value()))

    def add_product(self):
        """
        Adiciona um novo produto à lista.
        """
        name = simpledialog.askstring("Adicionar Produto", "Digite o nome do produto:", parent=self.__root)
        code = simpledialog.askstring("Adicionar Produto", "Digite o código do produto:", parent=self.__root)
        quantity = simpledialog.askinteger("Adicionar Produto", "Digite a quantidade do produto:", parent=self.__root)
        value = simpledialog.askfloat("Adicionar Produto", "Digite o valor unitário do produto:", parent=self.__root)
        validity = simpledialog.askstring("Adicionar Produto", "Digite a validade, caso não tenha, deixe em branco: ", parent=self.__root)

        new_product = Product(0, name, code, value, validity, quantity)
        self.__user.add_product(self.__conn, new_product)
        self.update_list()
        self.update_table()  # Atualiza a tabela após adicionar um novo produto
        messagebox.showinfo("Painel de Estoque", "Produto adicionado com sucesso!")

    def edit_product(self):
        """
        Edita o produto selecionado na tabela.
        """
        selected_item = self.__tree.focus()
        if selected_item:
            # Obter ID do item selecionado
            selected_id = self.__tree.item(selected_item, "values")
            if selected_id:
                p = self.find_product_byid(selected_id[0])
                if p:
                    # Caso o produto seja identificado, fazer as edições
                    name = simpledialog.askstring("Editar produto", "Digite o nome do produto:", parent=self.__root, initialvalue=p.get_name())
                    p.set_name(name)
                    code = simpledialog.askstring("Editar produto", "Digite o codigo do produto:", parent=self.__root, initialvalue=p.get_code())
                    p.set_code(code)
                    value = simpledialog.askfloat("Editar produto", "Digite o valor do produto:", parent=self.__root, initialvalue=p.get_value())
                    p.set_value(value)
                    amount = simpledialog.askinteger("Editar produto", "Digite a quantidade do produto:", parent=self.__root, initialvalue=p.get_amount())
                    p.set_amount(amount)
                    validity = simpledialog.askstring("Editar produto", "Digite a validade do produto:", parent=self.__root, initialvalue=p.get_validity())
                    p.set_validity(validity)
                    
                    # atualizar no banco de dados
                    self.__user.edit_product(self.__conn, p)
                    self.update_table() # Atualiza tabela
        else:
            messagebox.showerror("Painel de Estoque", "Nenhum item selecionado, por gentileza selecionar um item!")

    def remove_product(self):
        """
        Remove o produto selecionado na tabela.
        """
        # TODO Adicionar funcionalidade para remoção de produto do estoque
        
    def find_product_byid(self, id) -> Product:
        for p in self.__products:
            if id == str(p.get_id()):
                return p

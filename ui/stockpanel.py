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

        # Configurando a tabela (Treeview)
        self.__tree = ttk.Treeview(root, columns=("name", "code", "qt", "unit_value"), show="headings")
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

    def update_table(self):
        """
        Atualiza a tabela com os dados dos produtos.
        """
        # Carregar tabela a partir do banco de dados
        query = '''SELECT * FROM Stock'''
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        
        # Limpando itens existentes na tabela
        for item in self.__tree.get_children():
            self.__tree.delete(item)

        # Preenchendo a tabela com os dados da lista de produtos
        for product in result:
            self.__tree.insert("", "end", values=(product[1], product[2], product[5], product[3]))

    def add_product(self):
        """
        Adiciona um novo produto à lista.
        """
        name = simpledialog.askstring("Adicionar Produto", "Digite o nome do produto:", parent=self.__root)
        code = simpledialog.askstring("Adicionar Produto", "Digite o código do produto:", parent=self.__root)
        quantity = simpledialog.askinteger("Adicionar Produto", "Digite a quantidade do produto:", parent=self.__root)
        value = simpledialog.askfloat("Adicionar Produto", "Digite o valor unitário do produto:", parent=self.__root)
        validity = simpledialog.askstring("Adicionar Produto", "Digite a validade, caso não tenha, deixe em branco: ", parent=self.__root)

        new_product = Product(name, code, value, validity, quantity)
        self.__user.add_product(self.__conn, new_product)
        self.update_table()  # Atualiza a tabela após adicionar um novo produto
        messagebox.showinfo("Painel de Estoque", "Produto adicionado com sucesso!")

    def edit_product(self):
        """
        Edita o produto selecionado na tabela.
        """
        # TODO Adicionar funcionalidade para edição de produto

    def remove_product(self):
        """
        Remove o produto selecionado na tabela.
        """
        # TODO Adicionar funcionalidade para remoção de produto do estoque

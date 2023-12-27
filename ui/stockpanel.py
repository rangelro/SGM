import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

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
        self.root = root
        self.root.title("Painel de Estoque")
        self.root.geometry("800x600")

        self.label_title = tk.Label(root, text="Lista de Produtos", font=("Helvetica", 24))
        self.label_title.pack(pady=20)

        # Exemplo de uma lista de produtos (pode ser substituída por uma estrutura de dados real)
        self.products = [
            {"Nome": "Produto A", "Código": "001", "Quantidade": 10, "Valor Unitário": 5.0},
            {"Nome": "Produto B", "Código": "002", "Quantidade": 20, "Valor Unitário": 8.0},
            {"Nome": "Produto C", "Código": "003", "Quantidade": 15, "Valor Unitário": 12.0}
        ]

        # Configurando a tabela (Treeview)
        self.tree = ttk.Treeview(root, columns=("Nome", "Código", "Quantidade", "Valor Unitário"), show="headings")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Código", text="Código")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Valor Unitário", text="Valor Unitário")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Preenchendo a tabela com dados
        self.update_table()

        # Botões de ação
        self.button_add = tk.Button(root, text="Adicionar Produto", command=self.add_product)
        self.button_add.pack(side=tk.LEFT, padx=20, pady=10)

        self.button_edit = tk.Button(root, text="Editar Produto", command=self.edit_product)
        self.button_edit.pack(side=tk.LEFT, padx=20, pady=10)

        self.button_remove = tk.Button(root, text="Remover Produto", command=self.remove_product)
        self.button_remove.pack(side=tk.LEFT, padx=20, pady=10)

    def update_table(self):
        """
        Atualiza a tabela com os dados dos produtos.
        """
        # Limpando itens existentes na tabela
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Preenchendo a tabela com os dados da lista de produtos
        for product in self.products:
            self.tree.insert("", "end", values=(product["Nome"], product["Código"], product["Quantidade"], product["Valor Unitário"]))

    def add_product(self):
        """
        Adiciona um novo produto à lista.
        """
        name = simpledialog.askstring("Adicionar Produto", "Digite o nome do produto:", parent=self.root)
        code = simpledialog.askstring("Adicionar Produto", "Digite o código do produto:", parent=self.root)
        quantity = simpledialog.askinteger("Adicionar Produto", "Digite a quantidade do produto:", parent=self.root)
        unit_price = simpledialog.askfloat("Adicionar Produto", "Digite o valor unitário do produto:", parent=self.root)

        new_product = {"Nome": name, "Código": code, "Quantidade": quantity, "Valor Unitário": unit_price}
        self.products.append(new_product)
        self.update_table()  # Atualiza a tabela após adicionar um novo produto
        messagebox.showinfo("Painel de Estoque", "Produto adicionado com sucesso!")

    def edit_product(self):
        """
        Edita o produto selecionado na tabela.
        """
        selected_item = self.tree.selection()
        if selected_item:
            selected_product_index = int(self.tree.index(selected_item))
            selected_product = self.products[selected_product_index]

            name = simpledialog.askstring("Editar Produto", "Digite o novo nome do produto:", initialvalue=selected_product["Nome"], parent=self.root)
            code = simpledialog.askstring("Editar Produto", "Digite o novo código do produto:", initialvalue=selected_product["Código"], parent=self.root)
            quantity = simpledialog.askinteger("Editar Produto", "Digite a nova quantidade do produto:", initialvalue=selected_product["Quantidade"], parent=self.root)
            unit_price = simpledialog.askfloat("Editar Produto", "Digite o novo valor unitário do produto:", initialvalue=selected_product["Valor Unitário"], parent=self.root)

            edited_product = {"Nome": name, "Código": code, "Quantidade": quantity, "Valor Unitário": unit_price}
            self.products[selected_product_index] = edited_product
            self.update_table()  # Atualiza a tabela após editar um produto
            messagebox.showinfo("Painel de Estoque", "Produto editado com sucesso!")
        else:
            messagebox.showwarning("Painel de Estoque", "Selecione um produto para editar.")

    def remove_product(self):
        """
        Remove o produto selecionado na tabela.
        """
        selected_item = self.tree.selection()
        if selected_item:
            selected_product_index = int(self.tree.index(selected_item))
            del self.products[selected_product_index]
            self.update_table()  # Atualiza a tabela após remover um produto
            messagebox.showinfo("Painel de Estoque", "Produto removido com sucesso!")
        else:
            messagebox.showwarning("Painel de Estoque", "Selecione um produto para remover.")

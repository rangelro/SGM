import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class CashierPanel:
    """
    Classe que representa o sistema de caixa.

    Atributos:
        root (Tk): A janela principal da aplicação.
        tree (ttk.Treeview): Widget Treeview para exibir itens da compra.
        items (list): Lista de itens da compra.
        button_add_item (Button): Botão para adicionar um item à compra.
        button_remove_item (Button): Botão para remover um item da compra.
        button_finish_purchase (Button): Botão para finalizar a compra.
        button_cancel_purchase (Button): Botão para cancelar a compra.
    """

    def __init__(self, root):
        """
        Inicializa o sistema de caixa.

        Parâmetros:
            root (Tk): A janela principal da aplicação.
        """
        self.root = root
        self.root.title("Sistema de Caixa")
        self.root.geometry("800x600")

        self.label_title = tk.Label(root, text="Itens da Compra", font=("Helvetica", 24))
        self.label_title.pack(pady=20)

        # Exemplo de uma lista de itens da compra (pode ser substituída por uma estrutura de dados real)
        self.items = []

        # Configurando a tabela (Treeview)
        self.tree = ttk.Treeview(root, columns=("Nome", "Quantidade", "Valor Unitário", "Valor Total"), show="headings")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Valor Unitário", text="Valor Unitário")
        self.tree.heading("Valor Total", text="Valor Total")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Botões de ação
        self.button_add_item = tk.Button(root, text="Adicionar Item", command=self.add_item)
        self.button_add_item.pack(side=tk.LEFT, padx=20, pady=10)

        self.button_remove_item = tk.Button(root, text="Remover Item", command=self.remove_item)
        self.button_remove_item.pack(side=tk.LEFT, padx=20, pady=10)

        self.button_finish_purchase = tk.Button(root, text="Finalizar Compra", command=self.finish_purchase)
        self.button_finish_purchase.pack(side=tk.LEFT, padx=20, pady=10)

        self.button_cancel_purchase = tk.Button(root, text="Cancelar Compra", command=self.cancel_purchase)
        self.button_cancel_purchase.pack(side=tk.LEFT, padx=20, pady=10)

    def update_table(self):
        """
        Atualiza a tabela com os dados dos itens da compra.
        """
        # Limpando itens existentes na tabela
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Preenchendo a tabela com os dados da lista de itens da compra
        for item in self.items:
            self.tree.insert("", "end", values=(item["Nome"], item["Quantidade"], item["Valor Unitário"], item["Valor Total"]))

    def add_item(self):
        """
        Adiciona um novo item à compra.
        """
        code = simpledialog.askstring("Adicionar Item", "Digite o código do produto:", parent=self.root)
        # Simulando uma busca pelo código na lista de produtos (substitua isso pela lógica real)
        product = self.find_product_by_code(code)

        if product:
            quantity = simpledialog.askinteger("Adicionar Item", f"Digite a quantidade para {product['Nome']}:", parent=self.root)

            if quantity is not None and quantity > 0:
                item_total = quantity * product["Valor Unitário"]
                new_item = {
                    "Nome": product["Nome"],
                    "Quantidade": quantity,
                    "Valor Unitário": product["Valor Unitário"],
                    "Valor Total": item_total
                }

                self.items.append(new_item)
                self.update_table()  # Atualiza a tabela após adicionar um novo item
                messagebox.showinfo("Sistema de Caixa", f"Item {product['Nome']} adicionado com sucesso!")
            else:
                messagebox.showwarning("Sistema de Caixa", "Quantidade inválida.")
        else:
            messagebox.showwarning("Sistema de Caixa", "Produto não encontrado.")

    def remove_item(self):
        """
        Remove o item selecionado da tabela.
        """
        selected_item = self.tree.selection()
        if selected_item:
            selected_item_index = int(self.tree.index(selected_item))
            del self.items[selected_item_index]
            self.update_table()  # Atualiza a tabela após remover um item
            messagebox.showinfo("Sistema de Caixa", "Item removido com sucesso!")
        else:
            messagebox.showwarning("Sistema de Caixa", "Selecione um item para remover.")

    def finish_purchase(self):
        """
        Finaliza a compra e exibe um resumo.
        """
        if self.items:
            total_purchase_value = sum(item["Valor Total"] for item in self.items)
            purchase_summary = f"Resumo da Compra:\nTotal: R$ {total_purchase_value:.2f}"

            messagebox.showinfo("Sistema de Caixa - Compra Finalizada", purchase_summary)
            self.items = []  # Limpa a lista de itens após finalizar a compra
            self.update_table()  # Atualiza a tabela após finalizar a compra
        else:
            messagebox.showwarning("Sistema de Caixa", "A compra está vazia.")

    def cancel_purchase(self):
        """
        Cancela a compra e limpa a lista de itens.
        """
        confirmation = messagebox.askyesno("Sistema de Caixa", "Tem certeza que deseja cancelar a compra?")
        if confirmation:
            self.items = []  # Limpa a lista de itens ao cancelar a compra
            self.update_table()  # Atualiza a tabela ao cancelar a compra
            messagebox.showinfo("Sistema de Caixa", "Compra cancelada com sucesso.")

    def find_product_by_code(self, code):
        """
        Simulação de busca por um produto utilizando o código.

        Parâmetros:
            code (str): O código do produto.

        Retorna:
            dict: Os detalhes do produto encontrado ou None se não encontrado.
        """
        # Exemplo: substitua isso pela lógica real de busca por código
        products = {
            "001": {"Nome": "Produto A", "Valor Unitário": 5.0},
            "002": {"Nome": "Produto B", "Valor Unitário": 8.0},
            "003": {"Nome": "Produto C", "Valor Unitário": 12.0}
        }

        return products.get(code)

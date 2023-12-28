from ui.login import LoginPanel
from ui.stockpanel import StockPanel
from data.stockist import Stockist
import tkinter as tk

if __name__ == "__main__":
    root_login = tk.Tk()
    tela_login = StockPanel(root_login, Stockist("Teste"))
    root_login.mainloop()

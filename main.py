from ui.login import LoginPanel
from ui.adminpanel import AdminPanel
from ui.stockpanel import StockPanel
from data.admin import Admin
import tkinter as tk

if __name__ == "__main__":
    root_login = tk.Tk()
    tela_login = AdminPanel(root_login, Admin("rangel"))
    root_login.mainloop()

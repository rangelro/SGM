from ui.login import LoginPanel
from ui.adminpanel import AdminPanel
from data.admin import Admin
import tkinter as tk

if __name__ == "__main__":
    root_login = tk.Tk()
    tela_login = LoginPanel(root_login)
    root_login.mainloop()

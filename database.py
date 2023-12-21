import sqlite3

class ManagementSystem:
    def __init__(self,db_file="SGM.db"):
        self.conn =sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTERGER,
                name TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products(
                code INTERGER,
                name TEXT NOT NULL,
                value FLOAT NOT NULL
            )
        ''')

    #Registrar usuário
    def register_user(self,id,name,password):
        self.cursor.execute('''INSERT INTO users (id,name,password) VALUES (?,?,?)''',(id,name,password))
        self.conn.commit()
    
    #Desativar usuário
    def disable_user(self,id):
        self.cursor.execute('''DELETE FROM users WHERE id=?''',(id))
        self.conn.commit()


    #Listar Produtos
    def listProducts(self):
        self.cursor.execute("SELECT * FROM products")

        for linha in self.cursor.fetchall():
            print(linha)

        self.conn.close()
from data.user import User
from utilities.log import LogMixin
import sqlite3

class Admin(User, LogMixin):
    def __init__(self, username):
        super().__init__(username)
        
        # Implementação do usuário admin com o banco de dados, em específico a tabela 'Users'
        self.__connection = sqlite3.connect("database.db")
        self.__cursor = self.__connection.cursor()
        
        # Caso não exista a tabela "Users", criar uma nova
        query = '''CREATE TABLE IF NOT EXISTS Users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    user_type TEXT NOT NULL
                );'''
                
        self.__cursor.execute(query)
        self.__connection.commit()
        
    def add_user(self, username, password, user_type):
        # Efetuar operação de INSERT no banco de dados
        if not self.check_user_exists(username):
            query = '''INSERT INTO Users (username, password, user_type) VALUES (?, ?, ?);'''
            self.__cursor.execute(query, (username, password, user_type))
            self.__connection.commit()
            
            # Adiciona ação ao log
            self.print_log(f"Adicionado novo usuário({username}) ao banco de dados.")
            
            return True # Retorne verdadeiro para caso já exista o usuário
        else:
            return False # Caso já existe um usuário com esse nome, retornar falso para a adição
    
    def check_user_exists(self, username):
        query = '''SELECT COUNT(*) FROM Users WHERE username = ?;'''
        self.__cursor.execute(query, (username,))
        result = self.__cursor.fetchone()
        return result[0] > 0
    
    def edit_user(self, id, username, password, type):
        # TODO implementar sistema de edição de usuário
        
        # Adiciona ação ao log
        self.print_log(f"Usuário({id}) foi modificado.")
        
    def disable_user(self, id):
        # TODO implementar sistema para desabilitar usuário
        
        # Adiciona ação ao log
        self.print_log(f"Usuário({id}) foi desativado.")
        
    def active_user(self, id):
        # TODO implementar sistema para ativar usuário
        
        # Adiciona ação ao log
        self.print_log(f"Usuário({id}) foi ativado.")
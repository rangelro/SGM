from data.user import User
from utilities.log import LogMixin
import sqlite3

class Admin(User, LogMixin):
    """
    Classe que representa o administrador do sistema, com funções para adicionar, editar, desativar e ativar usuários.

    Attributes:
    - username (str): Nome de usuário do administrador.

    Methods:
    - __init__(self, username): Inicializa um objeto Admin com o nome de usuário fornecido.
    - add_user(self, username, password, user_type): Adiciona um novo usuário ao banco de dados.
    - check_user_exists(self, username): Verifica se um usuário com o nome fornecido já existe no sistema.
    - edit_user(self, id, username, password, user_type): Edita as informações de um usuário no banco de dados.
    - disable_user(self, id): Desativa um usuário no sistema.
    - active_user(self, id): Ativa um usuário previamente desativado no sistema.
    """
    def __init__(self, username):
        """
        Inicializa um objeto Admin com o nome de usuário fornecido.

        Parameters:
        - username (str): Nome de usuário do administrador.
        """
        super().__init__(username)
        
        # Implementação do usuário admin com o banco de dados, em específico a tabela 'Users'
        self.__connection = sqlite3.connect("database.db")
        self.__cursor = self.__connection.cursor()
        
        # Caso não exista a tabela "Users", criar uma nova
        query = '''CREATE TABLE IF NOT EXISTS Users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL,
                        user_type TEXT NOT NULL,
                        is_active INTEGER DEFAULT 1 CHECK (is_active IN (0, 1))
                    );'''
                
        self.__cursor.execute(query)
        self.__connection.commit()
        
    def add_user(self, username, password, user_type):
        """
        Adiciona um novo usuário ao banco de dados.

        Parameters:
        - username (str): Nome de usuário do novo usuário.
        - password (str): Senha do novo usuário.
        - user_type (str): Tipo de usuário (papel) do novo usuário.

        Returns:
        - bool: True se o usuário foi adicionado com sucesso, False se o usuário já existe.
        """
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
        """
        Verifica se um usuário com o nome fornecido já existe no sistema.

        Parameters:
        - username (str): Nome de usuário a ser verificado.

        Returns:
        - bool: True se o usuário existe, False caso contrário.
        """
        query = '''SELECT COUNT(*) FROM Users WHERE username = ?;'''
        self.__cursor.execute(query, (username,))
        result = self.__cursor.fetchone()
        return result[0] > 0
    
    def edit_user(self,id,username, password, user_type):
        """
        Edita as informações de um usuário no banco de dados.

        Parameters:
        - id (int): ID do usuário a ser editado.
        - username (str): Novo nome de usuário.
        - password (str): Nova senha do usuário.
        - user_type (str): Novo tipo de usuário.

        Returns:
        - None
        """
        #Efetua a função UPDATE no banco de dados com as edições feitas no User
        query = '''UPDATE Users SET username=?,password=?,user_type=? WHERE id=?'''
        self.__cursor.execute(query,(username,password,user_type,id))
        self.__connection.commit()
        
        # Adiciona ação ao log
        self.print_log(f"Usuário({id}) foi modificado.")
        
    def disable_user(self, id):
        """
        Desativa um usuário no sistema.

        Parameters:
        - id (int): ID do usuário a ser desativado.

        Returns:
        - None
        """
        #Efetua um UPDATE no banco de dados desativando o usuário alterando a proriedade is_active
        query = '''UPDATE Users SET is_active=0 WHERE id=?'''
        self.__cursor.execute(query,(id))
        self.__connection.commit()
        
        # Adiciona ação ao log
        self.print_log(f"Usuário({id}) foi desativado.")
        
    def active_user(self, id):
        """
        Ativa um usuário previamente desativado no sistema.

        Parameters:
        - id (int): ID do usuário a ser ativado.

        Returns:
        - None
        """
        #Efetua um UPDATE no banco de dados ativando o usuário alterando a proriedade is_active
        query = '''UPDATE Users SET is_active=1 WHERE id=?'''
        self.__cursor.execute(query,(id))
        self.__connection.commit()
        
        # Adiciona ação ao log
        self.print_log(f"Usuário({id}) foi ativado.")

    def all_users(self):
        """
        Retorna todos os dados da tabela de usuários.

        Returns:
        - list: Lista de tuplas contendo os dados de todos os usuários.
        """
        query = '''SELECT * FROM Users'''
        self.__cursor.execute(query)
        return self.__cursor.fetchall()
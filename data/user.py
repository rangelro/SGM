class User:
    """
    Classe User

    Representa um usuário com um nome de usuário.

    Atributos:
    - __username (str): Nome de usuário do usuário.

    Métodos:
    - __init__(self, username): Inicializa um novo usuário com o nome de usuário fornecido.
    - get_username(self): Retorna o nome de usuário do usuário.
    - set_username(self, username): Define um novo nome de usuário para o usuário.
    """
    def __init__(self, username):
        """
        Inicializa um novo usuário.

        Parâmetros:
        - username (str): O nome de usuário para o novo usuário.
        """
        self.__username = username
    
    # Metodos get's e set's
    def get_username(self):
        return self.__username
    
    def set_username(self, username):
        self.__username = username
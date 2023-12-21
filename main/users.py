from database import ManagementSystem

class AuthenticableMixin():
    """Utilização de um Mixin para que seja feita a verificação de autenticação do usuário
    """
    def autentication(self, login, password):
        if self.login == login and self.password == password:
            return True
        else:
            return False
        

class User():
    """Criação da base para adicionar os usuários no sistema, utilizando uma classe com construtor para que sejam repassados os dados necessários para o sistema
    """
    def __init__(self,id,name, active):
        self.id = id
        self.name = name
        self.active = True

class Administrator(User,AuthenticableMixin,ManagementSystem):
    def register_user(self,id,name,password):
        self.ManagementSystem.register_user(id,name,password)
    def disable_user(self,id):
        self.ManagementSystem.disable_user(id)

class Stockist(User):
    pass

class Cashier(User):
    pass

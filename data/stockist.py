from data.user import User
from utilities.log import LogMixin

class Stockist(User, LogMixin):
    def __init__(self, username):
        super().__init__(username)
        
    def add_product(self, db, product):
        query = '''INSERT INTO Stock (name, code, value, validity, quantity) VALUES (?, ?, ?, ?, ?);'''
        db.cursor().execute(query, (product.get_name(), product.get_code(), product.get_value(), product.get_validity(), product.get_amount()))
        db.commit()
        
        # Adiciona ação ao log
        self.print_log(f"Adicionado novo produto({product.get_name()}) com código: {product.get_code()} ao estoque.")
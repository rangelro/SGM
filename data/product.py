class Product:
    """
    Representa um produto.

    Atributos:
        name (str): Nome do produto.
        code (str): Código identificador do produto.
        value (float): Valor do produto.
        validity (str): Data de validade do produto.
        amount (int): Quantidade do produto.
    """

    def __init__(self, name, code, value, validity, amount):
        """
        Inicializa uma instância da classe Product.

        Parâmetros:
            name (str): Nome do produto.
            code (str): Código identificador do produto.
            value (float): Valor do produto.
            validity (str): Data de validade do produto.
            amount (int): Quantidade do produto.
        """
        self.__name = name
        self.__code = code
        self.__value = value
        self.__validity = validity
        self.__amount = amount
        
    # Metodos gets e sets, não será necessário docstring
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
    def get_code(self):
        return self.__code
    
    def set_code(self, code):
        self.__code = code
    
    def get_value(self):
        return self.__value
    
    def set_value(self, value):
        self.__value = value
        
    def get_validity(self):
        return self.__validity
    
    def set_validity(self, validity):
        self.__validity = validity
    
    def get_amount(self):
        return self.__amount
    
    def set_amount(self, amount):
        self.__amount = amount
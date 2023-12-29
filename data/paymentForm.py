from abc import ABC, abstractmethod

#implementação da classe forma de pagamento
class PaymentForm(ABC):
    @abstractmethod
    def pay(self,valor,pagamento):
        if pagamento == valor:
            troco = 0
            return troco
        elif pagamento > valor:
            troco = pagamento - valor
            return troco

#Implementado a forma de pagamento com cartão de crédito
class CreditCard(PaymentForm):
    
    def __init__(self):
        pass

    def pay(self, valor):
        return super().pay(valor)
    
class Pix(PaymentForm):
    def __init__(self,pagamento):
        self.pagamento = pagamento

    def pay(self, valor):
        return super().pay(valor)
    
class Cash(PaymentForm):
    def __init__(self,pagamento):
        self.pagamento = pagamento
        
    def pay(self, valor, pagamento):
        return super().pay(valor, pagamento)
from produtos.carrinho import Carrinho
from pagamento.interface_formas_pagamento import Metodo_Pagamento

class Finalizar:
    def calculo_pagamento(self,compras:Carrinho)->float:
        # Descarregar carrinho
        total = 0
        for _,valor in compras.item:
            total += valor 
        return total
    
class Pix(Metodo_Pagamento):
    def pagar(self, valor:float):
        print(f"Pagando R${valor} no PIX")

class Boleto(Metodo_Pagamento):
    def pagar(self, valor:float):
        print(f"Pagando R${valor} no Boleto")

class Cartao(Metodo_Pagamento):
    def pagar(self, valor:float):
        print(f"Pagando R${valor} no Cartão de Credito")
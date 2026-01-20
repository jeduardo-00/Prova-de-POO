from produtos.produtos import Produto
class Carrinho:

    def __init__(self):
        self.item = []
        
    def adicionar_carrinho(self, item:Produto):
        self.item.append([item.item,item.valor])
        print("Produto adicionado")
    
    def total_compras(self):
        # Descarregar carrinho
        valor = 0
        for _,valor in self.item:
            total += valor 
        print(f"Valor total de compras é: R${total}")
    
    def mostrar_produtos(self):
        print("PRODUTOS: ")
        for elemento, valor in self.item:
            print(f"{elemento} - R${valor}")
        self.total_compras()
        
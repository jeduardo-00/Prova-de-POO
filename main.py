from produtos.produtos import Produto
from produtos.carrinho import Carrinho
import pagamento.pagamento as pag

# Solicitando produto
p1 = Produto("Notebook", 3500.00)
p2 = Produto("Mouse", 150.00)

meu_carrinho = Carrinho()
meu_carrinho.adicionar_carrinho(p1)
meu_carrinho.adicionar_carrinho(p2)

total_compras = pag.Finalizar().calculo_pagamento(meu_carrinho)
pagamento = pag.Pix()
pagamento.pagar(total_compras)
class Categoria:
    def __init__(self, nome):
        self.nome = nome

class Produto:
    def __init__(self, id_produto, nome, categoria, quantidade, preco, localizacao):
        self.id_produto = id_produto
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.localizacao = localizacao

class Movimentacao:
    def __init__(self, tipo, produto_id, quantidade, data):
        self.tipo = tipo
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.data = data

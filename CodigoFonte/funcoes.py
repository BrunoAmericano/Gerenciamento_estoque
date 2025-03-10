from datetime import datetime
produtos = []
categorias = {}
movimentacoes = []

def cadastrar_produto(id_produto, nome, categoria_nome, quantidade, preco, localizacao):
    if categoria_nome not in categorias:
        categorias[categoria_nome] = Categoria(categoria_nome)
    categoria = categorias[categoria_nome]
    produto = Produto(id_produto, nome, categoria, quantidade, preco, localizacao)
    produtos.append(produto)
    print(f"Produto {nome} cadastrado com sucesso.")

def consultar_produto(id_produto):
    for produto in produtos:
        if produto.id_produto == id_produto:
            return vars(produto)
    return "Produto não encontrado."

def movimentar_estoque(id_produto, quantidade, tipo):
    produto = next((p for p in produtos if p.id_produto == id_produto), None)
    if produto is None:
        print("Produto não encontrado.")
        return
    if tipo == 'entrada':
        produto.quantidade += quantidade
        print(f"{quantidade} unidades adicionadas ao estoque do produto {produto.nome}.")
    elif tipo == 'saida':
        if produto.quantidade >= quantidade:
            produto.quantidade -= quantidade
            print(f"{quantidade} unidades retiradas do estoque do produto {produto.nome}.")
        else:
            print("Estoque insuficiente.")
            return
    movimentacoes.append(Movimentacao(tipo, id_produto, quantidade, datetime.now()))

def relatorio_estoque_baixo(limite):
    print("Relatório de Estoque Baixo:")
    for produto in produtos:
        if produto.quantidade < limite:
            print(f"Produto: {produto.nome}, Quantidade: {produto.quantidade}")

def relatorio_historico_movimentacoes():
    print("Histórico de Movimentações:")
    for movimentacao in movimentacoes:
        print(f"{movimentacao.tipo.capitalize()} - Produto ID: {movimentacao.produto_id}, Quantidade: {movimentacao.quantidade}, Data: {movimentacao.data}")

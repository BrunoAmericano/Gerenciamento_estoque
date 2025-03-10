from datetime import datetime
from classes import Categoria, Produto, Movimentacao  # Importando as classes do arquivo classes.py

# Listas e dicionários para armazenar os dados
produtos = []
categorias = {}
movimentacoes = []

# Função para cadastrar produtos
def cadastrar_produto(id_produto, nome, categoria_nome, quantidade, preco, localizacao):
    if categoria_nome not in categorias:
        categorias[categoria_nome] = Categoria(categoria_nome)  # Cria uma nova categoria se ela não existir
    categoria = categorias[categoria_nome]  # Associa o produto à categoria existente
    produto = Produto(id_produto, nome, categoria, quantidade, preco, localizacao)
    produtos.append(produto)  # Adiciona o produto à lista de produtos
    print(f"Produto '{nome}' cadastrado com sucesso!")

# Função para consultar um produto pelo ID
def consultar_produto(id_produto):
    for produto in produtos:
        if produto.id_produto == id_produto:  # Verifica se o ID corresponde
            return vars(produto)  # Retorna os atributos do produto como um dicionário
    return "Produto não encontrado."

# Função para movimentar o estoque (entrada ou saída)
def movimentar_estoque(id_produto, quantidade, tipo):
    produto = next((p for p in produtos if p.id_produto == id_produto), None)  # Busca o produto pelo ID
    if produto is None:
        print("Produto não encontrado.")
        return
    if tipo == 'entrada':
        produto.quantidade += quantidade
        print(f"{quantidade} unidades adicionadas ao estoque do produto '{produto.nome}'.")
    elif tipo == 'saida':
        if produto.quantidade >= quantidade:
            produto.quantidade -= quantidade
            print(f"{quantidade} unidades retiradas do estoque do produto '{produto.nome}'.")
        else:
            print("Estoque insuficiente.")
            return
    else:
        print("Tipo de movimentação inválido. Use 'entrada' ou 'saida'.")
        return
    # Registra a movimentação
    movimentacoes.append(Movimentacao(tipo, id_produto, quantidade, datetime.now()))

# Função para gerar um relatório de produtos com estoque baixo
def relatorio_estoque_baixo(limite):
    print("\nRelatório de Estoque Baixo:")
    encontrou = False
    for produto in produtos:
        if produto.quantidade < limite:
            print(f"Produto: {produto.nome}, Quantidade: {produto.quantidade}")
            encontrou = True
    if not encontrou:
        print("Nenhum produto com estoque abaixo do limite.")

# Função para exibir o histórico de movimentações
def relatorio_historico_movimentacoes():
    print("\nHistórico de Movimentações:")
    if not movimentacoes:
        print("Nenhuma movimentação registrada.")
    for movimentacao in movimentacoes:
        print(f"{movimentacao.tipo.capitalize()} - Produto ID: {movimentacao.produto_id}, "
              f"Quantidade: {movimentacao.quantidade}, Data: {movimentacao.data}")

# Função para gerar um relatório completo do estoque atual
def relatorio_estoque():
    print("\nRelatório do Estoque Atual:")
    if not produtos:
        print("Nenhum produto cadastrado no sistema.")
    for produto in produtos:
        print(f"Produto: {produto.nome}, Quantidade: {produto.quantidade}, Localização: {produto.localizacao}")

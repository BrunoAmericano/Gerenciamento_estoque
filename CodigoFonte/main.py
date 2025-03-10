import sys
import os

# Adiciona o diretório raiz ao PYTHONPATH dinamicamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from funcoes import *  # Importa todas as funções do arquivo funcoes.py

# Função auxiliar para processar valores decimais e unidades como Kg
def entrada_quantidade(valor):
    try:
        if "kg" in valor.lower():  # Verifica se o valor contém "Kg"
            return float(valor.lower().replace("kg", "").strip())
        else:
            return int(valor)  # Caso contrário, assume que é um número inteiro
    except ValueError:
        print("Erro: Quantidade inválida. Tente novamente.")
        return None

# Função auxiliar para converter preços
def entrada_preco(valor):
    try:
        return float(valor.replace(",", ".").strip())  # Substitui vírgula por ponto para aceitação
    except ValueError:
        print("Erro: Preço inválido. Tente novamente.")
        return None

while True:
    print("\nSistema de Gerenciamento de Estoque")
    print("1. Cadastrar Produto")
    print("2. Consultar Produto")
    print("3. Movimentar Estoque")
    print("4. Relatório de Estoque Baixo")
    print("5. Histórico de Movimentações")
    print("6. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        # Solicita os dados do produto para o cadastro
        id_produto = input("ID do Produto: ")
        nome = input("Nome do Produto: ")
        categoria_nome = input("Categoria: ")
        quantidade_input = input("Quantidade (use 'Kg' se necessário): ")
        quantidade = entrada_quantidade(quantidade_input)
        if quantidade is None: 
            continue  # Reinicia o fluxo caso a entrada seja inválida
        preco_input = input("Preço (use ',' ou '.'): ")
        preco = entrada_preco(preco_input)
        if preco is None: 
            continue  # Reinicia o fluxo caso a entrada seja inválida
        localizacao = input("Localização: ")
        cadastrar_produto(id_produto, nome, categoria_nome, quantidade, preco, localizacao)
    elif escolha == "2":
        # Consulta os detalhes de um produto
        id_produto = input("Digite o ID do Produto para consultar: ")
        resultado = consultar_produto(id_produto)
        if isinstance(resultado, dict):
            for key, value in resultado.items():
                print(f"{key}: {value}")
        else:
            print(resultado)
    elif escolha == "3":
        # Movimenta o estoque (entrada ou saída)
        id_produto = input("Digite o ID do Produto: ")
        quantidade_input = input("Quantidade para movimentação (use 'Kg' se necessário): ")
        quantidade = entrada_quantidade(quantidade_input)
        if quantidade is None:
            continue  # Reinicia o fluxo caso a entrada seja inválida
        tipo = input("Tipo de movimentação (entrada/saida): ").strip().lower()
        if tipo in ["entrada", "saida"]:
            movimentar_estoque(id_produto, quantidade, tipo)
        else:
            print("Tipo de movimentação inválido. Use 'entrada' ou 'saida'.")
    elif escolha == "4":
        # Gera um relatório de produtos com estoque abaixo do limite
        limite_input = input("Defina o limite para estoque baixo (use 'Kg' se necessário): ")
        limite = entrada_quantidade(limite_input)
        if limite is None:
            continue  # Reinicia o fluxo caso a entrada seja inválida
        relatorio_estoque_baixo(limite)
    elif escolha == "5":
        # Exibe o histórico de movimentações do estoque
        relatorio_historico_movimentacoes()
    elif escolha == "6":
        # Sai do sistema
        print("Saindo do sistema...")
        break
    else:
        # Opção inválida
        print("Opção inválida! Tente novamente.")

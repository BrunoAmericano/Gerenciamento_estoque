from CodigoFonte.funcoes import *

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
        # Chamar função de cadastro
        cadastrar_produto(...)
    elif escolha == "2":
        # Consultar produto
        print(consultar_produto(...))
    elif escolha == "3":
        # Movimentar estoque
        movimentar_estoque(...)
    elif escolha == "4":
        relatorio_estoque_baixo(...)
    elif escolha == "5":
        relatorio_historico_movimentacoes()
    elif escolha == "6":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")

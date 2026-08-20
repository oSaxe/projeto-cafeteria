import auxiliares
from rich.traceback import install
install()

def menu():
    while True:
        print("----------MENU----------")
        print("1. Clientes") #Contém tudo relacionado aos clientes.
        print("2. Produtos & Cardápio") #Dentro dessa opção do menu temos opções relacionadas aos produtos, como cadastro, listagem, e edição dos mesmos, e os ingredientes e os valores dos itens.
        print("3. Pedidos") #Contém as informações relacionadas aos pedidos.
        print("0. Sair")

        opcao = str(input(f"Escolha uma opção ~> ")).strip()

        auxiliares.limpar_terminal()

        if opcao == "1":
            menu_clientes()

        elif opcao == "2":
            menu_produtos()

        elif opcao == "3":
            menu_pedidos()

        elif opcao == "0":
            break
        else:
            print("Valor invalido!")

def menu_clientes():
    while True:
        print(f"----------MENU CLIENTES----------")
        print("1. Cadastro ID")
        print("2. Listar IDs")
        print("3. Buscar por CPF")
        print("4. Atualizar Dados")
        print("5. Remover Cliente")
        print("0. Voltar")

        opcao = str(input(f"Escolha uma opção ~> ")).strip()

        auxiliares.limpar_terminal()

        if opcao == "1":
            print("Cadastro ID")
        elif opcao == "0":
            break

def menu_produtos():
    while True:
        print(f"----------MENU PRODUTOS & CARDÁPIO----------")
        print("1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Buscar Produto")
        print("4. Exibir Cardápio")
        print("5. Atualizar Produto")
        print("6. Excluir/Inativar Produto")
        print("0. Voltar")

        opcao = str(input(f"Escolha uma opção ~> ")).strip()

        auxiliares.limpar_terminal()

        if opcao == "1":
            print("Cadastro produto")
        elif opcao == "0":
            break

def menu_pedidos():
    while True:
        print(f"----------MENU PEDIDOS----------")
        print("1. Cadastrar Pedido")
        print("2. Listar Pedidos Ativos")
        print("3. Atualizar status")
        print("4. Atualizar Pedido")
        print("5. Cancelar pedido")
        print("0. Voltar")

        opcao = str(input(f"\nEscolha uma opção ~> ")).strip()

        auxiliares.limpar_terminal()

        if opcao == "1":
            print("Cadastro pedido")
        elif opcao == "0":
            break

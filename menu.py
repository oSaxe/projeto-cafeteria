import auxiliares
from time import sleep
from rich.traceback import install
install()

def menu(gerenciador_clientes):
    while True:
        auxiliares.limpar_terminal()
        print("----------MENU----------")
        print("1. Clientes") #Contém tudo relacionado aos clientes.
        print("2. Produtos & Cardápio") #Dentro dessa opção do menu temos opções relacionadas aos produtos, como cadastro, listagem, e edição dos mesmos, e os ingredientes e os valores dos itens.
        print("3. Pedidos") #Contém as informações relacionadas aos pedidos.
        print("0. Sair")

        opcao = str(input(f"Escolha uma opção ~> ")).strip()

        auxiliares.limpar_terminal()

        if opcao == "1":
            menu_clientes(gerenciador_clientes)

        elif opcao == "2":
            menu_produtos()

        elif opcao == "3":
            menu_pedidos()

        elif opcao == "0":
            break
        else:
            print("Valor invalido!")

def menu_clientes(gerenciador_clientes):
    while True:
        auxiliares.limpar_terminal()
        print(f"----------MENU CLIENTES----------")
        print("1. Cadastro Cliente")
        print("2. Listar Clientes")
        print("3. Buscar por CPF")
        print("4. Atualizar Dados")
        print("5. Remover Cliente")
        print("0. Voltar")

        opcao = str(input(f"Escolha uma opção ~> ")).strip()

        auxiliares.limpar_terminal()

        if opcao == "1":
            while True:
                auxiliares.limpar_terminal()

                print("----------CADASTRO----------")
                print("1. Cadastrar Cliente")
                print("0. Voltar")

                opcao = input("~> ").strip()

                if opcao == "1":
                    gerenciador_clientes.cadastrar_cliente()
                elif opcao == "0":
                    break
                else:
                    auxiliares.limpar_terminal()
                    print("OPÇÃO INVALIDA!")
                    print("\nAperte ENTER para retornar")
                    input("")

        elif opcao == "2":
            print(gerenciador_clientes.mostrar_arquivo())
            print("\nAperte ENTER para retornar")
            input("")
            auxiliares.limpar_terminal()

        elif opcao == "3":
            while True:
                auxiliares.limpar_terminal()
                print("----------BUSCAR CPF----------")
                print("1. Buscar CPF")
                print("0. Voltar")

                opcao = input("~> ").strip()

                if opcao == "1":   
                    auxiliares.limpar_terminal()             
                    print(gerenciador_clientes.buscar_cpf())
                    print("\nAperte ENTER para retornar")
                    input("")
                elif opcao == "0":
                    break
                else:
                    auxiliares.limpar_terminal()
                    print("OPÇÃO INVALIDA!")
                    print("\nAperte ENTER para retornar")
                    input("")

        elif opcao == "4":
            while True:
                auxiliares.limpar_terminal()
                print("----------ATUALIZAR DADOS----------")
                print("1. Atualizar NOME")
                print("2. Atualizar TELEFONE")
                print("3. Atualizar CPF")
                print("0. Voltar")

                opcao = input("~> ").strip()

                if opcao == "1":   
                    print(gerenciador_clientes.atualizar_nome_planilha())
                    print("\nAperte ENTER para retornar")
                    input("")
                    auxiliares.limpar_terminal()
                elif opcao == "2":
                    print(gerenciador_clientes.atualizar_telefone_planilha())
                    print("\nAperte ENTER para retornar")
                    input("")
                elif opcao == "3":
                    print(gerenciador_clientes.atualizar_cpf_planilha())
                    print("\nAperte ENTER para retornar")
                    input("")
                    auxiliares.limpar_terminal()
                elif opcao == "0":
                    break
                else:
                    auxiliares.limpar_terminal()
                    print("OPÇÃO INVALIDA!")
                    print("\nAperte ENTER para retornar")
                    input("")

            
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

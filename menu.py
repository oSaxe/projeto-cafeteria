import auxiliares

def menu_clientes(gerenciador_clientes):
    while True:
        auxiliares.limpar_terminal()
        print("----------MENU CLIENTES----------")
        print("1. Cadastro Cliente")
        print("2. Listar Clientes")
        print("3. Buscar por CPF")
        print("4. Atualizar Dados")
        print("5. Remover Cliente")
        print("0. Voltar")

        opcao = str(input("Escolha uma opção ~> ")).strip()
        auxiliares.limpar_terminal()

        if opcao == "1":
            while True:
                auxiliares.limpar_terminal()
                print("----------CADASTRO----------")
                print("1. Cadastrar Cliente")
                print("0. Voltar")

                sub_opcao = input("~> ").strip()

                if sub_opcao == "1":
                    gerenciador_clientes.cadastrar_cliente()
                elif sub_opcao == "0":
                    break
                else:
                    auxiliares.limpar_terminal()
                    print("OPÇÃO INVALIDA!")
                    input("\nAperte ENTER para retornar")

        elif opcao == "2":
            print(gerenciador_clientes.mostrar_arquivo())
            input("\nAperte ENTER para retornar")
            auxiliares.limpar_terminal()

        elif opcao == "3":
            while True:
                auxiliares.limpar_terminal()
                print("----------BUSCAR CPF----------")
                print("1. Buscar CPF")
                print("0. Voltar")

                sub_opcao = input("~> ").strip()

                if sub_opcao == "1":   
                    auxiliares.limpar_terminal()             
                    print(gerenciador_clientes.buscar_cpf())
                    input("\nAperte ENTER para retornar")
                elif sub_opcao == "0":
                    break
                else:
                    auxiliares.limpar_terminal()
                    print("OPÇÃO INVALIDA!")
                    input("\nAperte ENTER para retornar")

        elif opcao == "4":
            while True:
                auxiliares.limpar_terminal()
                print("----------ATUALIZAR DADOS----------")
                print("1. Atualizar NOME")
                print("2. Atualizar CPF")
                print("3. Atualizar TELEFONE")
                print("4. Atualizar EMAIL")
                print("0. Voltar")

                sub_opcao = input("~> ").strip()

                if sub_opcao == "1":   
                    print(gerenciador_clientes.atualizar_nome_planilha())
                    input("\nAperte ENTER para retornar")
                    auxiliares.limpar_terminal()
                elif sub_opcao == "2":
                    print(gerenciador_clientes.atualizar_cpf_planilha())
                    input("\nAperte ENTER para retornar")
                elif sub_opcao == "3":
                    print(gerenciador_clientes.atualizar_telefone_planilha())
                    input("\nAperte ENTER para retornar")
                    auxiliares.limpar_terminal()
                elif sub_opcao == "4":
                    print(gerenciador_clientes.atualizar_email_planilha())
                    input("\nAperte ENTER para retornar")
                elif sub_opcao == "0":
                    break
                else:
                    auxiliares.limpar_terminal()
                    print("OPÇÃO INVALIDA!")
                    input("\nAperte ENTER para retornar")

        elif opcao == "5":
            while True:
                auxiliares.limpar_terminal()
                print("----------REMOÇÃO CLIENTE----------")
                print("1. Remover Cliente")
                print("0. Voltar")  

                sub_opcao = str(input("~> ")).strip()

                if sub_opcao == "1":
                    auxiliares.limpar_terminal()
                    nome = input("Digite o NOME do cliente: ").strip().title()
                    telefone = str(input("Digite o TELEFONE do cliente: ")).strip()
                    cpf = str(input("Digite o CPF do cliente: ")).strip()

                    print(gerenciador_clientes.remover_cliente(nome, telefone, cpf))
                    input("\nAperte ENTER para retornar")
                    auxiliares.limpar_terminal()
                elif sub_opcao == "0":
                    break
                else:
                    auxiliares.limpar_terminal()
                    print("OPÇÃO INVALIDA!")
                    input("\nAperte ENTER para retornar")

        elif opcao == "0":
            break
        else:
            auxiliares.limpar_terminal()
            print("OPÇÃO INVALIDA!")
            input("\nAperte ENTER para retornar")


def menu_produtos(gerenciador_produtos):
    while True:
        auxiliares.limpar_terminal()
        print("----------MENU PRODUTOS & CARDÁPIO----------")
        print("1. Cadastrar Produto")
        print("2. Listar Todos os Produtos")
        print("3. Filtrar Produtos por Categoria")
        print("4. Buscar Produto por Nome ou ID")
        print("5. Exibir Cardápio ")
        print("6. Atualizar Estoque")
        print("7. Atualizar Dados do Produto")
        print("8. Ativar/Inativar Produto")
        print("0. Voltar")

        opcao = str(input("\nEscolha uma opção ~> ")).strip()
        auxiliares.limpar_terminal()

        if opcao == "1":
            print(gerenciador_produtos.cadastrar_produto())
        elif opcao == "2":
            print(gerenciador_produtos.listar_produtos())
        elif opcao == "3":
            print(gerenciador_produtos.filtrar_por_categoria())
        elif opcao == "4":
            print(gerenciador_produtos.buscar_produto())
        elif opcao == "5":
            print(gerenciador_produtos.exibir_cardapio())
        elif opcao == "6":
            print(gerenciador_produtos.atualizar_estoque())
        elif opcao == "7":
            print(gerenciador_produtos.atualizar_produto())
        elif opcao == "8":
            print(gerenciador_produtos.alternar_status_produto())
        elif opcao == "0":
            break
        else:
            print("OPÇÃO INVÁLIDA!")

        input("\nAperte ENTER para retornar")


def menu_pedidos(gerenciador_pedidos, gerenciador_clientes, gerenciador_produtos):
    while True:
        auxiliares.limpar_terminal()
        print("----------MENU PEDIDOS----------")
        print("1. Cadastrar Pedido")
        print("2. Listar Pedidos")
        print("3. Atualizar Status do Pedido")
        print("0. Voltar")

        opcao = str(input("\nEscolha uma opção ~> ")).strip()
        auxiliares.limpar_terminal()

        if opcao == "1":
            print(gerenciador_pedidos.cadastrar_pedido(gerenciador_clientes, gerenciador_produtos))
        elif opcao == "2":
            print(gerenciador_pedidos.listar_pedidos())
        elif opcao == "3":
            print(gerenciador_pedidos.atualizar_status_pedido())
        elif opcao == "0":
            break
        else:
            print("OPÇÃO INVÁLIDA!")

        input("\nAperte ENTER para retornar")


def menu(gerenciador_clientes, gerenciador_produtos, gerenciador_pedidos):
    while True:
        auxiliares.limpar_terminal()
        print("----------MENU----------")
        print("1. Clientes")
        print("2. Produtos & Cardápio")
        print("3. Pedidos")
        print("0. Sair")

        opcao = str(input("Escolha uma opção ~> ")).strip()
        auxiliares.limpar_terminal()

        if opcao == "1":
            menu_clientes(gerenciador_clientes)
        elif opcao == "2":
            menu_produtos(gerenciador_produtos)
        elif opcao == "3":
            menu_pedidos(gerenciador_pedidos, gerenciador_clientes, gerenciador_produtos)
        elif opcao == "0":
            break
        else:
            print("Valor inválido!")
            input("\nAperte ENTER para retornar")
import funcoes
import builtins
from time import sleep
from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

def menu():
    while True:
        conteudo_menu = (
            "1. Cadastrar produto\n"
            "2. Listar produtos\n"
            "3. Atualizar produto\n"
            "4. Excluir produto\n"
            "0. Sair"
        )
        painel_menu = Panel(conteudo_menu, title="COFFEE SHOPS TIA ROSA", expand=False)

        print(painel_menu)

        opcao = str(input(f"\nEscolha uma opção: ")).strip()

        if opcao == "1":
            funcoes.cadastrar_produto()
            sleep(2)
            funcoes.limpar_terminal()

        elif opcao == "2":
            funcoes.listar_produtos()
            sleep(2)
            funcoes.limpar_terminal()

        elif opcao == "3":
            funcoes.atualizar_produtos()
            sleep(2)
            funcoes.limpar_terminal()
            
        elif opcao == "4":
            funcoes.excluir_produtos()
            sleep(2)
            funcoes.limpar_terminal()

        elif opcao == "0":
            for i in range(3, 0, -1):
                builtins.print(f"\rSaindo do programa em {i}..", end="", flush=True)
                sleep(0.8)
            funcoes.limpar_terminal()
            break

        else:
            funcoes.limpar_terminal()
            print("Opção invalida!")
            sleep(2)
            funcoes.limpar_terminal()

if __name__ == "__main__":
    funcoes.limpar_terminal()
    menu()
import subprocess

def limpar_terminal():
    subprocess.run("cls", shell=True)

class CadastroProduto:
    """
    Classe para realizar o cadastro de um produto no sistema.
    """
    def __init__(self, id: int = 0, nome: str = "", preco: float = 0.0, quantidade: int = 0):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


    def cadastrar_produto(self):
        limpar_terminal()
        return

def listar_produtos():
    limpar_terminal()
    print("listar_produtos")
    return

def atualizar_produtos():
    limpar_terminal()
    print("atualizar_produtos")
    return

def excluir_produtos():
    limpar_terminal()
    print("excluir_produtos")
    return
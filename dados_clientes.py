import auxiliares
import numpy as np
import pandas as pd
from pathlib import Path
from rich.traceback import install
install()

class Cliente:
    """
    Classe para tratar dados, pontos e descontos dos clientes.

Métodos: 
transformar_dicionario: Transforma os dados dos clientes em um dicionario para salvar em um json.

    """
    def __init__(self, cliente_id: int = 0, Nome: str = "", Telefone: str = "", CPF: str = "", valor_total_gasto: float = 0.0, pontos: int = 0):
        self.id = cliente_id
        self.nome = Nome
        self.telefone = Telefone
        self.cpf = CPF
        self.valor_total_gasto = valor_total_gasto
        self.pontos = pontos

    def adicionar_gasto(self, valor):
        pontos_ganhos = int(valor // 5)

        self.valor_total_gasto += valor
        self.pontos += pontos_ganhos

    def pode_resgatar(self):
        return self.pontos >= 50

    def resgatar(self):
        if self.pode_resgatar():
            self.pontos -= 50
            return True
        return False

class GerenciadorClientes:
    def __init__(self, nome_arquivo = "dados_clientes.csv"):
        self.caminho_do_projeto = Path(__file__).parent / nome_arquivo
        

    def cadastrar_cliente(self):
        if self.caminho_do_projeto.is_file():
            df_dados_clientes = pd.read_csv(self.caminho_do_projeto)

            if not df_dados_clientes.empty:
                novo_id = int(df_dados_clientes["id"].max()) + 1
            else:
                novo_id = 1
        else:
            novo_id = 1

        print("Insira os dados do cliente: ")

        auxiliares.limpar_terminal()

        cliente = Cliente(
            cliente_id = novo_id,
            Nome = input("Cliente: ").title().strip(),
            Telefone = input("Telefone: ").strip(),
            CPF = input("CPF: ").strip(),
        )

        df_dados_clientes = pd.DataFrame([vars(cliente)])

        if not self.caminho_do_projeto.is_file():
            df_dados_clientes.to_csv(self.caminho_do_projeto, index=False)

        else:
            df_dados_clientes.to_csv(self.caminho_do_projeto, mode="a", header=False, index=False)

    def mostrar_arquivo(self):
        try:
            df_dados_clientes = pd.read_csv(self.caminho_do_projeto)
            return df_dados_clientes
        except FileNotFoundError:
            auxiliares.limpar_terminal()
            return "ARQUIVO NÃO ENCONTRADO."
             
    def buscar_cpf(self):
        if not self.caminho_do_projeto.is_file():
            auxiliares.limpar_terminal()
            return("ARQUIVO NÃO ENCONTRADO.")

        df_dados_clientes = pd.read_csv(self.caminho_do_projeto)

        cpf_alvo = input("Digite o CPF: ").strip()

        cliente = df_dados_clientes[df_dados_clientes["cpf"].astype(str) == cpf_alvo]

        if cliente.empty:
            auxiliares.limpar_terminal()
            return "CLIENTE NÃO ENCONTRADO."
        else:
            auxiliares.limpar_terminal()
            print("\n")
            return cliente.to_string(index=False)

    def atualizar_planilha(self):
        if not self.caminho_do_projeto.is_file():
            return("ARQUIVO NÃO ENCONTRADO.")
        
        df_dados_clientes = pd.read_csv(self.caminho_do_projeto)

        if df_dados_clientes.empty:
            return "ARQUIVO VAZIO."

        cpf_alvo = input("Digite o CPF do cliente que deseja alterar: ").strip()

        indice = df_dados_clientes.index[df_dados_clientes["cpf"].astype(str) == cpf_alvo].to_list()

        if not indice:
            return "CLIENTE NÃO ENCONTRADO."

        index_cliente = indice[0]

        auxiliares.limpar_terminal()

        print("\n---------------")
        print(" DADOS ATUAIS")
        print("---------------\n")
        print(df_dados_clientes.loc[[index_cliente]].to_string(index=False))

        print("\nPreencha com os novos dados, caso deseje manter o valor atual pressione ENTER.")

        novo_nome = input(f"Nome Antigo: [{df_dados_clientes.at[index_cliente, 'nome']}] | Novo Nome: ").strip()

        novo_telefone = input(f"Telefone Antigo: [{df_dados_clientes.at[index_cliente, 'telefone']}] | Novo Telefone: ").strip()

        if novo_nome:
            novo_nome = df_dados_clientes.at[index_cliente, "nome"].strip()
        if novo_telefone:
            novo_telefone = df_dados_clientes.at[index_cliente, "telefone"].strip()

        df_dados_clientes.to_csv(self.caminho_do_projeto, index=False)

        auxiliares.limpar_terminal()

        return "Dados atualizados com sucesso."
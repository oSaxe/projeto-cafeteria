import auxiliares
import pandas as pd
from pathlib import Path

class Cliente:
    def __init__(self, cliente_id: int = 0, nome: str = "", cpf: str = "", telefone: str = "", email: str = "", valor_total_gasto: float = 0.0, pontos: int = 0):
        self.id = cliente_id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.valor_total_gasto = valor_total_gasto
        self.pontos = pontos

    def pode_resgatar(self) -> bool:
        return self.pontos >= 50

    def resgatar(self) -> bool:
        if self.pode_resgatar():
            self.pontos -= 50
            return True
        return False

    def adicionar_compra(self, valor: float) -> int:
        pontos_ganhos = int(valor // 5)
        self.valor_total_gasto += valor
        self.pontos += pontos_ganhos
        return pontos_ganhos

class GerenciadorClientes:

    def __init__(self, nome_arquivo="dados_clientes.csv"):
        self.caminho_do_projeto = Path(__file__).parent / nome_arquivo

    def _tratar_nulos(self, df: pd.DataFrame) -> pd.DataFrame:
        """Método interno para padronizar e preencher valores nulos no DataFrame."""
        regras = {
            "nome": "NÃO INFORMADO",
            "cpf": "NÃO INFORMADO",
            "telefone": "NÃO INFORMADO",
            "email": "NÃO INFORMADO",
            "valor_total_gasto": 0.0,
            "pontos": 0
        }
        df_dados_clientes = df.fillna(value = regras)
        df_dados_clientes["valor_total_gasto"] = pd.to_numeric(df_dados_clientes["valor_total_gasto"], errors = "coerce").fillna(0.0)
        df_dados_clientes["pontos"] = pd.to_numeric(df_dados_clientes["pontos"], errors = "coerce").fillna(0).astype(int)
        return df_dados_clientes

    def processar_compra(self, cpf: str, valor_bruto: float):
        """
        Processa a compra de um cliente:
        - Aplica desconto de R$ 5,00 se o cliente tiver 50+ pontos.
        - Soma o valor gasto ao total do cliente.
        - Calcula e adiciona os novos pontos acumulados.
        - Atualiza a planilha CSV.
        """
        if not self.caminho_do_projeto.is_file():
            return valor_bruto, 0, False

        df_dados_clientes = pd.read_csv(self.caminho_do_projeto)
        df_dados_clientes = self._tratar_nulos(df_dados_clientes)

        indices = df_dados_clientes.index[df_dados_clientes["cpf"].astype(str) == str(cpf)].tolist()
        if not indices:
            return valor_bruto, 0, False

        idx = indices[0]

        
        linha = df_dados_clientes.loc[idx].to_dict()

        cliente = Cliente(
            cliente_id = int(linha["id"]),
            nome = str(linha["nome"]),
            cpf = str(linha["cpf"]),
            telefone = str(linha["telefone"]),
            email = str(linha["email"]),
            valor_total_gasto = float(linha["valor_total_gasto"]),
            pontos = int(linha["pontos"])
        )   
        
        resgatou = cliente.resgatar()
        valor_com_desconto = max(0.0, valor_bruto - 5.0) if resgatou else valor_bruto

        pontos_ganhos = int(valor_com_desconto // 5)

        cliente.adicionar_compra(valor_com_desconto)

        df_dados_clientes.at[idx, "valor_total_gasto"] = cliente.valor_total_gasto
        df_dados_clientes.at[idx, "pontos"] = cliente.pontos


        df_dados_clientes.to_csv(self.caminho_do_projeto, index = False)

        return valor_com_desconto, pontos_ganhos, resgatou

    def cadastrar_cliente(self):
        if self.caminho_do_projeto.is_file():
            df_dados_clientes = pd.read_csv(self.caminho_do_projeto)
            if not df_dados_clientes.empty:
                novo_id = int(df_dados_clientes["id"].max()) + 1
            else:
                novo_id = 1
        else:
            novo_id = 1

        auxiliares.limpar_terminal()
        print("Insira os dados do cliente: ")

        cliente = Cliente(
            cliente_id = novo_id,
            nome = input("Cliente: ").title().strip(),
            cpf = input("CPF: ").strip(),
            telefone = input("Telefone: ").strip(),
            email = input("Email:  ").strip()
        )

        df_novo_cliente = pd.DataFrame([vars(cliente)])

        if not self.caminho_do_projeto.is_file():
            df_novo_cliente.to_csv(self.caminho_do_projeto, index = False)
        else:
            df_novo_cliente.to_csv(self.caminho_do_projeto, mode="a", header = False, index = False)

    def mostrar_arquivo(self):
        try:
            df_dados_clientes = pd.read_csv(self.caminho_do_projeto)
            df_dados_clientes = self._tratar_nulos(df_dados_clientes)
            
            return df_dados_clientes.rename(columns = str.upper)
        
        except FileNotFoundError:
            auxiliares.limpar_terminal()
            return "ARQUIVO NÃO ENCONTRADO"

    def buscar_cpf(self):
        if not self.caminho_do_projeto.is_file():
            auxiliares.limpar_terminal()
            return "ARQUIVO NÃO ENCONTRADO"

        df_dados_clientes = pd.read_csv(self.caminho_do_projeto)
        df_dados_clientes = self._tratar_nulos(df_dados_clientes)

        cpf_alvo = input("Digite o CPF: ").strip()
        cliente = df_dados_clientes[df_dados_clientes["cpf"].astype(str) == cpf_alvo]

        if cliente.empty:
            auxiliares.limpar_terminal()
            return "CLIENTE NÃO ENCONTRADO"
        else:
            auxiliares.limpar_terminal()
            print("\n")
            return cliente.rename(columns=str.upper).to_string(index = False)

    def atualizar_nome_planilha(self):
        if not self.caminho_do_projeto.is_file():
            return "ARQUIVO NÃO ENCONTRADO"
        
        df_dados_clientes = pd.read_csv(self.caminho_do_projeto)
        df_dados_clientes = self._tratar_nulos(df_dados_clientes)

        if df_dados_clientes.empty:
            return "ARQUIVO VAZIO"

        auxiliares.limpar_terminal()
        cpf_alvo = input("Digite o CPF do cliente que deseja alterar: ").strip()
        indice = df_dados_clientes.index[df_dados_clientes["cpf"].astype(str) == cpf_alvo].to_list()

        if not indice:
            auxiliares.limpar_terminal()
            return "CLIENTE NÃO ENCONTRADO"

        index_cliente = indice[0]

        auxiliares.limpar_terminal()
        print("\n---------------")
        print(" DADOS ATUAIS")
        print("---------------\n")
        print(df_dados_clientes.loc[[index_cliente]].rename(columns = str.upper).to_string(index = False))

        print("\nPreencha com os novos dados, caso deseje manter o valor atual pressione ENTER.")
        novo_nome = input(f"Nome Antigo: [{df_dados_clientes.at[index_cliente, 'nome']}] | Novo Nome: ").strip()

        if novo_nome:
            df_dados_clientes.at[index_cliente, "nome"] = novo_nome.title()
            df_dados_clientes.to_csv(self.caminho_do_projeto, index = False)
            auxiliares.limpar_terminal()
            return "NOME atualizado com sucesso." 

        auxiliares.limpar_terminal()
        return "NOME permanece o mesmo."

    def atualizar_telefone_planilha(self):
        if not self.caminho_do_projeto.is_file():
            return "ARQUIVO NÃO ENCONTRADO"
        
        df_dados_clientes = pd.read_csv(self.caminho_do_projeto)
        df_dados_clientes = self._tratar_nulos(df_dados_clientes)

        if df_dados_clientes.empty:
            return "ARQUIVO VAZIO"

        auxiliares.limpar_terminal()
        cpf_alvo = input("Digite o CPF do cliente que deseja alterar: ").strip()
        indice = df_dados_clientes.index[df_dados_clientes["cpf"].astype(str) == cpf_alvo].to_list()

        if not indice:
            auxiliares.limpar_terminal()
            return "CLIENTE NÃO ENCONTRADO"

        index_cliente = indice[0]

        auxiliares.limpar_terminal()
        print("\n---------------")
        print(" DADOS ATUAIS")
        print("---------------\n")
        print(df_dados_clientes.loc[[index_cliente]].rename(columns = str.upper).to_string(index = False))

        print("\nPreencha com os novos dados, caso deseje manter o valor atual pressione ENTER.")
        novo_telefone = input(f"Telefone Antigo: [{df_dados_clientes.at[index_cliente, 'telefone']}] | Novo Telefone: ").strip()

        if novo_telefone:
            df_dados_clientes.at[index_cliente, "telefone"] = novo_telefone
            df_dados_clientes.to_csv(self.caminho_do_projeto, index = False)
            auxiliares.limpar_terminal()
            return "TELEFONE atualizado com sucesso."

        auxiliares.limpar_terminal()
        return "TELEFONE permanece o mesmo."

    def atualizar_cpf_planilha(self):
        if not self.caminho_do_projeto.is_file():
            return "ARQUIVO NÃO ENCONTRADO"
        
        df_dados_clientes = pd.read_csv(self.caminho_do_projeto)
        df_dados_clientes = self._tratar_nulos(df_dados_clientes)

        if df_dados_clientes.empty:
            return "ARQUIVO VAZIO"

        auxiliares.limpar_terminal()
        cpf_alvo = input("Digite o CPF do cliente que deseja alterar: ").strip()
        indice = df_dados_clientes.index[df_dados_clientes["cpf"].astype(str) == cpf_alvo].to_list()

        if not indice:
            auxiliares.limpar_terminal()
            return "CLIENTE NÃO ENCONTRADO"

        index_cliente = indice[0]

        auxiliares.limpar_terminal()
        print("\n---------------")
        print(" DADOS ATUAIS")
        print("---------------\n")
        print(df_dados_clientes.loc[[index_cliente]].rename(columns = str.upper).to_string(index = False))

        print("\nPreencha com os novos dados, caso deseje manter o valor atual pressione ENTER.")
        novo_cpf = input(f"CPF Antigo: [{df_dados_clientes.at[index_cliente, 'cpf']}] | Novo CPF: ").strip()

        if novo_cpf:
            df_dados_clientes.at[index_cliente, "cpf"] = novo_cpf
            df_dados_clientes.to_csv(self.caminho_do_projeto, index = False)
            auxiliares.limpar_terminal()
            return "CPF atualizado com sucesso."

        auxiliares.limpar_terminal()
        return "CPF permanece o mesmo."

    def atualizar_email_planilha(self):
        if not self.caminho_do_projeto.is_file():
            return "ARQUIVO NÃO ENCONTRADO"
        
        df_dados_clientes = pd.read_csv(self.caminho_do_projeto)
        df_dados_clientes = self._tratar_nulos(df_dados_clientes)

        if df_dados_clientes.empty:
            return "ARQUIVO VAZIO"

        auxiliares.limpar_terminal()
        cpf_alvo = input("Digite o CPF do cliente que deseja alterar: ").strip()
        indice = df_dados_clientes.index[df_dados_clientes["cpf"].astype(str) == cpf_alvo].to_list()

        if not indice:
            auxiliares.limpar_terminal()
            return "CLIENTE NÃO ENCONTRADO"

        index_cliente = indice[0]

        auxiliares.limpar_terminal()
        print("\n---------------")
        print(" DADOS ATUAIS")
        print("---------------\n")
        print(df_dados_clientes.loc[[index_cliente]].rename(columns = str.upper).to_string(index = False))

        print("\nPreencha com os novos dados, caso deseje manter o valor atual pressione ENTER.")
        novo_email = input(f"EMAIL Antigo: [{df_dados_clientes.at[index_cliente, 'email']}] | Novo EMAIL: ").strip()

        if novo_email:
            df_dados_clientes.at[index_cliente, "email"] = novo_email
            df_dados_clientes.to_csv(self.caminho_do_projeto, index = False)
            auxiliares.limpar_terminal()
            return "EMAIL atualizado com sucesso."

        auxiliares.limpar_terminal()
        return "EMAIL permanece o mesmo."

    def remover_cliente(self, nome: str, telefone: str, cpf: str):
        if not self.caminho_do_projeto.is_file():
            return "ARQUIVO NÃO ENCONTRADO"

        df_dados_clientes = pd.read_csv(self.caminho_do_projeto)
        df_dados_clientes = self._tratar_nulos(df_dados_clientes)

        cliente = df_dados_clientes[
            (df_dados_clientes["nome"] == nome) &
            (df_dados_clientes["telefone"] == telefone) &
            (df_dados_clientes["cpf"] == cpf)
        ]

        if cliente.empty:
            auxiliares.limpar_terminal()
            return "CLIENTE NÃO ENCONTRADO"

        auxiliares.limpar_terminal()
        print("\n----------DADOS CLIENTE----------")
        print(cliente.rename(columns = str.upper).to_string(index = False))
        print("\n1. Confirmar exclusão.")
        print("0. Voltar")

        confirmacao = input("~> ").strip()

        if confirmacao == "1":
            df_dados_clientes = df_dados_clientes[
                ~(
                    (df_dados_clientes["nome"] == nome) &
                    (df_dados_clientes["telefone"] == telefone) &
                    (df_dados_clientes["cpf"] == cpf)
                )
            ]
            df_dados_clientes.to_csv(self.caminho_do_projeto, index = False)
            auxiliares.limpar_terminal()
            return "Cliente removido com sucesso."
        
        auxiliares.limpar_terminal()
        return "Operação cancelada."
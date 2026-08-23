import pandas as pd
from pathlib import Path
from datetime import datetime

class Pedido:
    def __init__(self, pedido_id: int, cliente_cpf: str, produto_id: int, quantidade: int, valor_unitario: float, valor_total: float, status: str = "Pendente", data_hora: str = ""):
        self.id = pedido_id
        self.cliente_cpf = cliente_cpf
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.valor_total = valor_total
        self.status = status
        self.data_hora = data_hora


class GerenciadorPedidos:
    def __init__(self, nome_arquivo="dados_pedidos.csv"):
        self.caminho_do_projeto = Path(__file__).parent / nome_arquivo

    def _tratar_nulos(self, df: pd.DataFrame) -> pd.DataFrame:
        regras = {
            "cliente_cpf": "NÃO INFORMADO",
            "produto_id": 0,
            "quantidade": 0,
            "valor_unitario": 0.0,
            "valor_total": 0.0,
            "status": "Pendente",
            "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        df_pedidos = df.fillna(value=regras)
        df_pedidos["quantidade"] = pd.to_numeric(df_pedidos["quantidade"], errors = "coerce").fillna(0).astype(int)
        df_pedidos["valor_unitario"] = pd.to_numeric(df_pedidos["valor_unitario"], errors = "coerce").fillna(0.0)
        df_pedidos["valor_total"] = pd.to_numeric(df_pedidos["valor_total"], errors = "coerce").fillna(0.0)
        return df_pedidos

    def cadastrar_pedido(self, gerenciador_clientes, gerenciador_produtos):
        if not gerenciador_clientes.caminho_do_projeto.is_file():
            return "Nenhum cliente cadastrado no sistema."

        df_clientes = pd.read_csv(gerenciador_clientes.caminho_do_projeto)
        df_clientes = gerenciador_clientes._tratar_nulos(df_clientes)

        cpf_alvo = input("Digite o CPF do cliente: ").strip()
        cliente = df_clientes[df_clientes["cpf"].astype(str) == cpf_alvo]

        if cliente.empty:
            return "CLIENTE NÃO ENCONTRADO"

        nome_cliente = cliente.iloc[0]["nome"]
        pontos_cliente = cliente.iloc[0]["pontos"]
        print(f"\nCliente selecionado: {nome_cliente} | Pontos atuais: {pontos_cliente}")

        if not gerenciador_produtos.caminho_do_projeto.is_file():
            return "Nenhum produto cadastrado no sistema."

        df_produtos = pd.read_csv(gerenciador_produtos.caminho_do_projeto)
        df_produtos = gerenciador_produtos._tratar_nulos(df_produtos)

        try:
            prod_id = int(input("Digite o ID do produto: ").strip())
        except ValueError:
            return "ID de produto inválido."

        indices_prod = df_produtos.index[(df_produtos["id"] == prod_id) & (df_produtos["ativo"] == True)].tolist()
        if not indices_prod:
            return "PRODUTO NÃO ENCONTRADO OU INATIVO"

        idx_prod = indices_prod[0]
        nome_produto = df_produtos.at[idx_prod, "nome"]
        preco_unitario = float(df_produtos.at[idx_prod, "preco"])
        estoque_atual = int(df_produtos.at[idx_prod, "quantidade_estoque"])

        print(f"Produto: {nome_produto} | R$ {preco_unitario:.2f} | Estoque: {estoque_atual}")

        try:
            qtd = int(input("Quantidade desejada: ").strip())
        except ValueError:
            return "QUANTIDADE INVÁLIDA"

        if qtd <= 0:
            return "A quantidade deve ser maior que zero."

        if qtd > estoque_atual:
            return f"ESTOQUE INSUFICIENTE. Disponível: {estoque_atual}"

        valor_bruto = preco_unitario * qtd

        valor_final, pontos_ganhos, resgatou = gerenciador_clientes.processar_compra(cpf_alvo, valor_bruto)

        df_produtos.at[idx_prod, "quantidade_estoque"] = estoque_atual - qtd
        df_produtos.to_csv(gerenciador_produtos.caminho_do_projeto, index=False)

        if self.caminho_do_projeto.is_file():

            df_pedidos = pd.read_csv(self.caminho_do_projeto)
            if not df_pedidos.empty:
                novo_id = int(df_pedidos["id"].max()) + 1
            else:
                novo_id = 1
        else:
            novo_id = 1

        novo_pedido = Pedido(
            pedido_id = novo_id,
            cliente_cpf = cpf_alvo,
            produto_id = prod_id,
            quantidade = qtd,
            valor_unitario = preco_unitario,
            valor_total = valor_final,
            status="Concluído"
        )

        df_novo_pedido = pd.DataFrame([vars(novo_pedido)])

        if not self.caminho_do_projeto.is_file():
            df_novo_pedido.to_csv(self.caminho_do_projeto, index = False)
        else:
            df_novo_pedido.to_csv(self.caminho_do_projeto, mode="a", header = False, index = False)
        if resgatou:
            msg_resgate = "(50 pontos resgatados)"
        else:
            msg_resgate = ""

        return f"Pedido #{novo_id} cadastrado com sucesso!\nValor Final: R$ {valor_final:.2f}\nPontos ganhos nesta compra: {pontos_ganhos}{msg_resgate}"

    def listar_pedidos(self):
        if not self.caminho_do_projeto.is_file():
            return "NENHUM PEDIDO REGISTRADO"

        df_pedidos = pd.read_csv(self.caminho_do_projeto)
        df_pedidos = self._tratar_nulos(df_pedidos)

        if df_pedidos.empty:
            return "NENHUM PEDIDO REGISTRADO"

        return df_pedidos.rename(columns = str.upper).to_string(index = False)

    def atualizar_status_pedido(self):
        if not self.caminho_do_projeto.is_file():
            return "ARQUIVO NÃO ENCONTRADO"

        df_pedidos = pd.read_csv(self.caminho_do_projeto)
        df_pedidos = self._tratar_nulos(df_pedidos)

        try:
            pedido_id = int(input("Digite o ID do pedido para alterar o status: ").strip())
        except ValueError:
            return "ID INVÁLIDO."

        indices = df_pedidos.index[df_pedidos["id"] == pedido_id].tolist()
        if not indices:
            return "PEDIDO NÃO ENCONTRADO."

        idx = indices[0]
        print(f"Status atual: {df_pedidos.at[idx, 'status']}")
        novo_status = input("Digite o novo status (Pendente, Em Preparo, Concluído, Cancelado): ").strip().title()

        if novo_status:
            df_pedidos.at[idx, "status"] = novo_status
            df_pedidos.to_csv(self.caminho_do_projeto, index = False)
            return f"Status do Pedido #{pedido_id} alterado para '{novo_status}'."

        return "Status não foi alterado."
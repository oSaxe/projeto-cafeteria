import auxiliares
import pandas as pd
from pathlib import Path

class Produto:
    def __init__(self, produto_id: int = 0, nome: str = "", categoria: str = "", preco: float = 0.0, ingrediente: str = "", quantidade_estoque: int = 0, ativo: bool = True):
        self.id = produto_id
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.ingrediente = ingrediente
        self.quantidade_estoque = quantidade_estoque
        self.ativo = ativo


class GerenciadorProdutos:
    def __init__(self, nome_arquivo = "dados_produtos.csv"):
        self.caminho_do_projeto = Path(__file__).parent / nome_arquivo

    def _tratar_nulos(self, df_produtos: pd.DataFrame) -> pd.DataFrame:
        regras = {
            "nome": "NÃO INFORMADO",
            "categoria": "GERAL",
            "preco": 0.0,
            "ingrediente": "NÃO INFORMADO",
            "quantidade_estoque": 0,
            "ativo": True
        }
        df_produtos = df_produtos.fillna(value = regras)
        df_produtos["preco"] = pd.to_numeric(df_produtos["preco"], errors = "coerce").fillna(0.0)
        df_produtos["quantidade_estoque"] = pd.to_numeric(df_produtos["quantidade_estoque"], errors = "coerce").fillna(0).astype(int)
        df_produtos["ativo"] = df_produtos["ativo"].astype(bool)
        return df_produtos

    def cadastrar_produto(self):
        if self.caminho_do_projeto.is_file():
            df_produtos = pd.read_csv(self.caminho_do_projeto)
            novo_id = int(df_produtos["id"].max()) + 1 if not df_produtos.empty else 1
        else:
            novo_id = 1

        auxiliares.limpar_terminal()
        print("---------- CADASTRO DE PRODUTO ----------")
        nome = input("Nome do Produto: ").title().strip()
        categoria = input("Categoria (ex: Café, Salgado, Doce): ").title().strip()
        
        try:
            preco = float(input("Preço (R$): ").replace(",", ".").strip())
        except ValueError:
            preco = 0.0

        ingrediente = input("Ingredientes / Descrição: ").strip()

        try:
            estoque = int(input("Quantidade inicial em Estoque: ").strip())
        except ValueError:
            estoque = 0

        produto = Produto(
            produto_id = novo_id,
            nome = nome,
            categoria = categoria,
            preco = preco,
            ingrediente = ingrediente,
            quantidade_estoque = estoque,
            ativo = True
        )

        df_novo_produto = pd.DataFrame([vars(produto)])

        if not self.caminho_do_projeto.is_file():
            df_novo_produto.to_csv(self.caminho_do_projeto, index = False)
        else:
            df_novo_produto.to_csv(self.caminho_do_projeto, mode="a", header = False, index = False)

        auxiliares.limpar_terminal()
        return "Produto cadastrado com sucesso!"

    def listar_produtos(self):
        if not self.caminho_do_projeto.is_file():
            auxiliares.limpar_terminal()
            return "NENHUM PRODUTO CADASTRADO"

        df_produtos = pd.read_csv(self.caminho_do_projeto)
        df_produtos = self._tratar_nulos(df_produtos)

        if df_produtos.empty:
            auxiliares.limpar_terminal()
            return "NENHUM PRODUTO CADASTRADO"

        return df_produtos.rename(columns = str.upper)

    def filtrar_por_categoria(self):
        if not self.caminho_do_projeto.is_file():
            return "ARQUIVO NÃO ENCONTRADO"

        df_produtos = pd.read_csv(self.caminho_do_projeto)
        df_produtos = self._tratar_nulos(df_produtos)

        if df_produtos.empty:
            return "NENHUM PRODUTO CADASTRADO"

        categoria_alvo = input("Digite a categoria desejada: ").strip().lower()

        resultado = df_produtos[df_produtos["categoria"].astype(str).str.lower() == categoria_alvo]

        auxiliares.limpar_terminal()

        if resultado.empty:
            return f"Nenhum produto encontrado para a categoria '{categoria_alvo.title()}'."

        return resultado.rename(columns = str.upper).to_string(index = False)

    def exibir_cardapio(self):
        if not self.caminho_do_projeto.is_file():
            return "CARDÁPIO VAZIO"

        df_produtos = pd.read_csv(self.caminho_do_projeto)
        df_produtos = self._tratar_nulos(df_produtos)

        cardapio = df_produtos[df_produtos["ativo"] == True]

        if cardapio.empty:
            return "NENHUM PRODUTO DISPONÍVEL NO MOMENTO"

        return cardapio[["id", "nome", "categoria", "preco", "ingrediente", "quantidade_estoque"]].rename(columns = str.upper).to_string(index = False)

    def buscar_produto(self):
        if not self.caminho_do_projeto.is_file():
            return "ARQUIVO NÃO ENCONTRADO"

        df_produtos = pd.read_csv(self.caminho_do_projeto)
        df_produtos = self._tratar_nulos(df_produtos)

        busca = input("Digite o nome ou ID do produto: ").strip().lower()

        resultado = df_produtos[
            (df_produtos["nome"].astype(str).str.lower().str.contains(busca)) |
            (df_produtos["id"].astype(str) == busca)
        ]

        auxiliares.limpar_terminal()

        if resultado.empty:
            return "PRODUTO NÃO ENCONTRADO"

        return resultado.rename(columns = str.upper).to_string(index = False)

    def atualizar_estoque(self):
        if not self.caminho_do_projeto.is_file():
            return "ARQUIVO NÃO ENCONTRADO"

        df_produtos = pd.read_csv(self.caminho_do_projeto)
        df_produtos = self._tratar_nulos(df_produtos)

        try:
            prod_id = int(input("Digite o ID do produto para atualizar o estoque: ").strip())
        except ValueError:
            return "ID INVÁLIDO"

        indices = df_produtos.index[df_produtos["id"] == prod_id].tolist()
        if not indices:
            return "PRODUTO NÃO ENCONTRADO"

        idx = indices[0]

        print(f"\nProduto: {df_produtos.at[idx, 'nome']}")
        print(f"Estoque atual: {df_produtos.at[idx, 'quantidade_estoque']}")

        try:
            novo_estoque = int(input("\nDigite a nova quantidade total do estoque: ").strip())
            df_produtos.at[idx, "quantidade_estoque"] = novo_estoque
            df_produtos.to_csv(self.caminho_do_projeto, index = False)
            return "Estoque atualizado com sucesso!"
        except ValueError:
            return "VALOR DE ESTOQUE INVÁLIDO"

    def atualizar_produto(self):
        if not self.caminho_do_projeto.is_file():
            return "ARQUIVO NÃO ENCONTRADO"

        df_produtos = pd.read_csv(self.caminho_do_projeto)
        df_produtos = self._tratar_nulos(df_produtos)

        try:
            prod_id = int(input("Digite o ID do produto a alterar: ").strip())

        except ValueError:
            auxiliares.limpar_terminal()
            return "ID INVÁLIDO"

        indices = df_produtos.index[df_produtos["id"] == prod_id].tolist()
        if not indices:
            return "PRODUTO NÃO ENCONTRADO"

        idx = indices[0]

        print("\n--- DADOS ATUAIS ---")
        print(df_produtos.loc[[idx]].rename(columns = str.upper).to_string(index = False))
        print("\nPressione ENTER para manter o valor atual.")

        novo_nome = input(f"Nome [{df_produtos.at[idx, 'nome']}]: ").strip()
        nova_cat = input(f"Categoria [{df_produtos.at[idx, 'categoria']}]: ").strip()
        novo_preco = input(f"Preço [{df_produtos.at[idx, 'preco']}]: ").strip()
        novo_ing = input(f"Ingredientes [{df_produtos.at[idx, 'ingrediente']}]: ").strip()

        if novo_nome:
            df_produtos.at[idx, "nome"] = novo_nome.title()
        if nova_cat:
            df_produtos.at[idx, "categoria"] = nova_cat.title()
        if novo_preco:
            try:
                df_produtos.at[idx, "preco"] = float(novo_preco.replace(",", "."))
            except ValueError:
                pass
        if novo_ing:
            df_produtos.at[idx, "ingrediente"] = novo_ing

        df_produtos.to_csv(self.caminho_do_projeto, index = False)
        return "Produto atualizado com sucesso!"

    def alternar_status_produto(self):
        if not self.caminho_do_projeto.is_file():
            return "ARQUIVO NÃO ENCONTRADO."

        df_produtos = pd.read_csv(self.caminho_do_projeto)
        df_produtos = self._tratar_nulos(df_produtos)

        try:
            prod_id = int(input("Digite o ID do produto para alterar o status: ").strip())
        except ValueError:
            return "ID INVÁLIDO."

        indices = df_produtos.index[df_produtos["id"] == prod_id].tolist()
        if not indices:
            return "PRODUTO NÃO ENCONTRADO."

        idx = indices[0]
        status_atual = df_produtos.at[idx, "ativo"]
        novo_status = not status_atual

        df_produtos.at[idx, "ativo"] = novo_status
        df_produtos.to_csv(self.caminho_do_projeto, index = False)

        estado_str = "ATIVADO" if novo_status else "INATIVADO"
        return f"Produto {estado_str} com sucesso!"
import os
import numpy
import pandas as pd

#Constantes
VALOR_POR_PONTOS = 5            #Constante que define o valor que deve ser gasto para ganhar 1 ponto
MIN_PONTOS_PARA_RESGATE  = 50   #Valor minimo para resgate dos pontos


class Cliente:
    """
    Classe para tratar dados, pontos e descontos dos clientes.

Métodos: 
transformar_dicionario: Transforma os dados dos clientes em um dicionario para salvar em um json.

    """
    def __init__(self, cliente_id: int = 0, nome: str = "", telefone: str = "", pontos: int = 0, cpf: str = ""):
            self.id = cliente_id
            self.nome = nome
            self.telefone = telefone
            self.pontos = pontos
            self.cpf = cpf

    # Metodos:

        
    def para_csv(self) -> dict:
        """
        Metodo para transformar os dados que são passados em um dicionario para ser salvo em um json.
        """
        return {
                "id": self.id,
                "nome": self.nome,
                "telefone": self.telefone,
                "pontos": self.pontos
        }

    def pontuacao(self, valor_gasto: float) -> int:
        novos_pontos = int(valor_gasto // VALOR_POR_PONTOS)
        self.pontos += novos_pontos
        return novos_pontos

    def resgate_pontos(self, VALOR_DO_DESCONTO: float = 10.0):
        if self.pontos < MIN_PONTOS_PARA_RESGATE:
            return 0.0
        lotes_pontos = self.pontos // MIN_PONTOS_PARA_RESGATE
        desconto_pontos = lotes_pontos * MIN_PONTOS_PARA_RESGATE
        

clientes = Cliente(101, "Thiago", "61 985751420", 70)


               
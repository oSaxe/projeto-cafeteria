# Sistema de Gerenciamento de Cafeteria

Projeto desenvolvido em Python com o objetivo de simular o gerenciamento de uma cafeteria por meio de uma aplicação executada no terminal.

O sistema permite gerenciar clientes, produtos e pedidos, além de controlar estoque, sistema de pontos e informações das vendas.

Este projeto foi desenvolvido como parte dos meus estudos em programação e Análise e Desenvolvimento de Sistemas, aplicando conceitos de Programação Orientada a Objetos, manipulação de dados e organização de código.

## Funcionalidades

### Clientes

* Cadastro de clientes
* Listagem de clientes cadastrados
* Busca de cliente por CPF
* Atualização de dados
* Remoção de clientes
* Controle do valor total gasto
* Sistema de pontos
* Resgate de pontos para desconto

### Produtos

* Cadastro de produtos
* Listagem de produtos
* Busca por nome ou ID
* Filtro por categoria
* Exibição do cardápio
* Controle de estoque
* Atualização de informações
* Ativação e inativação de produtos

### Pedidos

* Cadastro de pedidos
* Associação do pedido ao cliente
* Seleção de produto por ID
* Validação da disponibilidade em estoque
* Cálculo do valor da compra
* Atualização automática do estoque
* Acúmulo e resgate de pontos
* Listagem de pedidos
* Atualização do status do pedido

## Sistema de Pontos

O sistema possui um programa de fidelidade integrado ao cadastro de clientes.

* A cada R$ 5,00 gastos, o cliente recebe 1 ponto
* Ao atingir 50 pontos, o cliente pode realizar o resgate
* O resgate utiliza 50 pontos e aplica R$ 5,00 de desconto
* Novos pontos são calculados sobre o valor final da compra

## Tecnologias utilizadas

* Python
* Pandas
* CSV
* Pathlib
* Git
* GitHub

## Conceitos aplicados

* Programação Orientada a Objetos
* Separação de responsabilidades
* Manipulação de DataFrames com Pandas
* Persistência de dados utilizando arquivos CSV
* Tratamento de valores nulos
* Validação de entradas
* Manipulação de arquivos
* Modularização do código
* Controle de versão com Git

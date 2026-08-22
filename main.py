import menu
import clientes, produtos, pedidos


gerenciador_clientes = clientes.GerenciadorClientes()
gerenciador_produtos = produtos.GerenciadorProdutos()
gerenciador_pedidos = pedidos.GerenciadorPedidos()

menu.menu(gerenciador_clientes, gerenciador_produtos ,gerenciador_pedidos)



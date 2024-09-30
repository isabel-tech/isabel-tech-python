# ### Terceira versão da segmentação de clientes

# Mantenha a funcionalidade do programa, mas agora use funções para organizar o código. Crie funções para cada uma das operações: `solicitar_nome_cliente`, `solicitar_total_compras` e `atribuir_segmento` e `print_segmento_por_cliente`. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções. Além disso, normalize que todos os nomes sejam armazenados em letras minúsculas.

def solicitar_nome_cliente():
	nome_cliente = input("Digite o nome do cliente (ou 'sair' para sair): ").lower()
	if nome_cliente == 'sair':
		return None
	return nome_cliente
	
def solicitar_compras_totais():
	while True:
		try:
			compras_totais = float(input('Digite o total de compras: '))
			if compras_totais < 0:
				raise ValueError
			break
		except ValueError:
			print('Entrada inválida. Por favor, digite um número para compras.')
	return compras_totais

def atribuir_segmento(segmentos, compras_totais, nome_cliente):
	for limite, segmento in segmentos:
		if compras_totais <= limite:    
			clientes[nome_cliente] = segmento
			break

def print_segmento_por_cliente(clientes):
	for nome_cliente, segmento in clientes.items():
		print(f"{nome_cliente.capitalize()}: Segmento do Cliente = {segmento}")

clientes = {}
segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]

while True:
	nome_cliente = solicitar_nome_cliente()
	if nome_cliente == None:
		break
	compras_totais = solicitar_compras_totais()
	segmento = atribuir_segmento(segmentos, compras_totais, nome_cliente)
print_nome_segmento = print_segmento_por_cliente(clientes)


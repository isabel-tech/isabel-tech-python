# ### Terceira versão do relatório de vendas

#  Mantenha a funcionalidade do programa, mas agora use funções para organizar o código. Crie funções para cada uma das operações: `solicitar_nome_vendedor`, `solicitar_vendas` e `atualizar_dados` e `print_dados`. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções.


def nome_vendedor():
	vendedor = input("Digite o nome do vendedor (ou 'sair' para sair): ").lower()
	if vendedor == 'sair':
		return None
	return vendedor

def solicitar_vendas():
	while True:
		try: 
			vendas = float(input("Digite as vendas: "))
			if vendas < 0:
				raise ValueError
		except ValueError:
			print("Entrada inválida. Por favor, digite um número para vendas.")
			continue
		return vendas
	
def atualizar_dados(vendedor, vendas, cont, dicionario_vendas, dicionario_total_e_qtde):
	if vendedor in dicionario_vendas:
		if vendas != 0:
			dicionario_vendas[vendedor]['quantidade_vendas'] += cont
			dicionario_vendas[vendedor]['total_vendas'] += vendas
			return dicionario_vendas[vendedor]['quantidade_vendas'], dicionario_vendas[vendedor]['total_vendas']
	else:
		dicionario_total_e_qtde = {'total_vendas': vendas, 'quantidade_vendas': cont}
		dicionario_vendas[vendedor] = dicionario_total_e_qtde
	return dicionario_total_e_qtde, dicionario_vendas[vendedor]	
	
def print_dados(dicionario_vendas):
	for vendedor, total_e_qtde in dicionario_vendas.items():
		print(f"{vendedor.capitalize()}: Total de vendas = R${dicionario_vendas[vendedor]['total_vendas']:.2f}, Média de vendas = R${dicionario_vendas[vendedor]['total_vendas']/dicionario_vendas[vendedor]['quantidade_vendas']:.2f}")

dicionario_vendas = {}
dicionario_total_e_qtde = {}
cont = 1

while True:
	vendedor = nome_vendedor()
	if vendedor == None:
		break
	vendas = solicitar_vendas()
	dados = atualizar_dados(vendedor, vendas, cont, dicionario_vendas, dicionario_total_e_qtde)

print_dados(dicionario_vendas)
	

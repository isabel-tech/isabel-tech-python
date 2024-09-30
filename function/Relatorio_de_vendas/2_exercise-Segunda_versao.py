# ### Segunda versão do relatório de vendas
# 
# Mantenha a mesma funcionalidade do programa anterior, mas agora valide a entrada do usuário.
# Se o usuário digitar um valor inválido para vendas, mostre a mensagem
# "Entrada inválida. Por favor, digite um número para vendas." e peça para o usuário digitar
# novamente. Tal validação deve ser feita usando try/except. FEITO <3
# 
# Além disso, ao invés de armazenar cada venda em uma lista para cada vendedor, armazene
# o total de vendas e a quantidade de vendas em um dicionário. Por exemplo, se o usuário
# digitar "João" e "1000" para vendas, o dicionário deve ficar assim:
# 
# {'João': {'total_vendas': 1000, 'quantidade_vendas': 1}}
# ```
# Se, após, o usuário digitar "João" e "2000" para vendas, o dicionário deve ficar assim:
# 
# {'João': {'total_vendas': 3000, 'quantidade_vendas': 2}}
# ```
# Perceba como o total de vendas de João aumentou em 2000, assim como a quantidade aumentou em uma unidade.
#
# Ao final, mostre o total de vendas e a média de vendas de cada vendedor.
# 
# Exemplo de saída:
# ```
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 1000
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 2000
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 2000
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 3000
# Digite o nome do vendedor (ou 'sair' para sair): sair
# João: Total de vendas = R$ 3000.00, Média de vendas = R$ 1500.00
# Maria: Total de vendas = R$ 5000.00, Média de vendas = R$ 2500.00
# ```

dicionario_vendas = {}
dicionario_total_e_qtde = {}
cont = 1
while True:
	vendedor = input("Digite o nome do vendedor (ou 'sair' para sair): ").lower()
	if vendedor == 'sair':
		break
	try: 
		vendas = float(input("Digite as vendas: "))
	except ValueError:
		print("Entrada inválida. Por favor, digite um número para vendas.")
		continue
	if vendedor in dicionario_vendas:
		dicionario_vendas[vendedor]['quantidade_vendas'] += cont
		dicionario_vendas[vendedor]['total_vendas'] += vendas
	else:
		dicionario_total_e_qtde = {'total_vendas': vendas, 'quantidade_vendas': cont}
		dicionario_vendas[vendedor] = dicionario_total_e_qtde 

for vendedor, total_e_qtde in dicionario_vendas.items():
	print(f"{vendedor.capitalize()}: Total de vendas = R${dicionario_vendas[vendedor]['total_vendas']:.2f}, Média de vendas = R${dicionario_vendas[vendedor]['total_vendas']/dicionario_vendas[vendedor]['quantidade_vendas']:.2f}")

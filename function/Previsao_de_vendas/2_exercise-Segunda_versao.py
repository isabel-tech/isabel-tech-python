# ### Segunda versão da previsão de vendas
# 

# Mantenha a mesma funcionalidade do programa anterior, mas agora valide a entrada do usuário.
# Se o usuário digitar um valor inválido para vendas ou taxa de crescimento, mostre a mensagem
# "Entrada inválida. Por favor, digite um número para vendas e taxa de crescimento." e peça
# para o usuário digitar novamente. Tal validação deve ser feita usando try/except.
# 

previsoes_de_venda = {}

while True:
	nome_produto = input('Digite o nome do produto (ou "sair" para sair): ').lower()
	if nome_produto == 'sair':
		break
	try:
		vendas_mes_atual = float(input('Digite as vendas do mês atual: '))
		taxa_crescimento = float(input('Digite a taxa de crescimento (%): ').replace('%',''))
	except ValueError:
		print('Entrada Inválida. Digite um valor válido para as vendas e taxa de crescimento')
		continue
	previsao = vendas_mes_atual + ((taxa_crescimento/100) * vendas_mes_atual)
	previsoes_de_venda[nome_produto] = previsao

for chave in previsoes_de_venda:
	print(f'{chave}: Previsão de vendas do próximo mês = R${previsoes_de_venda[chave]:.2f}')
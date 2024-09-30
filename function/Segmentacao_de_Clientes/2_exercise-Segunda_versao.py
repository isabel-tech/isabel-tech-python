# ### Segunda versão da segmentação de clientes
# 
# Mantenha a mesma funcionalidade do programa anterior, mas agora valide a entrada do usuário.
# Se o usuário digitar um valor inválido para compras, mostre a mensagem
# "Entrada inválida. Por favor, digite um número para compras." e peça para o usuário digitar
# novamente. Tal validação deve ser feita usando try/except.
# 
# Além disso, ao invés de deixar os limites de compras fixos no programa, armazene-os em uma
# lista de tuplas. Por exemplo:
# 
# ```python
# segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]
# ``` 
# 
# Assim, outros segmentos podem ser adicionados facilmente. O primeiro elemento da tupla é o
# limite de compras e o segundo é o nome do segmento. O último elemento da lista é uma tupla
# com limite `float('inf')`, que representa o segmento Ouro. Isso significa que, se o valor de
# compras for maior que todos os limites, o segmento será Ouro.
# 
# Depois, percorra essa lista e, para cada tupla, verifique se o valor de compras é menor ou igual
# ao limite. Se for, armazene o segmento em um dicionário. Por exemplo, se o usuário digitar
# "João" e "500" para compras, o dicionário deve ficar assim:
# `{'João': 'Bronze'}`

clientes = {}
segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]

while True:
	nome_cliente = input("Digite o nome do cliente (ou 'sair' para sair): ").lower()
	if nome_cliente == 'sair':
		break
	while True:
		try:
			compras_totais = float(input('Digite o total de compras: '))
			break
		except ValueError:
			print('Entrada inválida. Por favor, digite um número para compras.')		
	for limite, segmento in segmentos:
		if compras_totais <= limite:    
			clientes[nome_cliente] = segmento
			break
for nome_cliente, segmento in clientes.items():
	print(f"{nome_cliente.capitalize()}: Segmento do Cliente = {segmento}")

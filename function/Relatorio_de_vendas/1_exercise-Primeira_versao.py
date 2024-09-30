# ### Primeira versão do relatório de vendas

# Escreva um programa que calcula o total e a média de vendas para cada vendedor em uma empresa.
# O usuário deve digitar o nome do vendedor e suas vendas, e o programa deve manter o controle
# do total e da média de vendas para cada vendedor.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie um dicionário vazio para armazenar os dados de vendas.
# 2. Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
# 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
# 4. Se o usuário digitar 'sair', encerre o loop usando break.
# 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.
# 
# Exemplo de saída:
#     
# ```
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 100
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 200
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 300
# Digite o nome do vendedor (ou 'sair' para sair): sair
# João: Total de vendas = R$ 400.0, Média de vendas = R$ 200.0
# Maria: Total de vendas = R$ 200.0, Média de vendas = R$ 200.0
# ```
# 
# Dica: use o método sum() para calcular o total de vendas e o método len() para calcular o número de vendas.

# Criando um dicionário vazio para armazenar os dados de vendas:
dicionario_vendas = {}
#Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
while True:
	vendedor = input("Digite o nome do vendedor (ou 'sair' para sair): ").lower()
	if vendedor == 'sair':
		break
	vendas = float(input("Digite as vendas: "))
	if vendedor in dicionario_vendas:
		#Acessando a lista de vendas do vendedor no dicionário. O valor que uma chave recebe é uma lista, então, você pode fazer um append
		dicionario_vendas[vendedor].append(vendas)
	else:
		dicionario_vendas[vendedor] = [vendas]

for vendedor, vendas in dicionario_vendas.items():
	total_vendas = sum(vendas)
	media_vendas = total_vendas/ len(vendas)
	print(f'{vendedor.capitalize()}: Total de vendas = R${total_vendas:.2f}, Média de vendas = R${media_vendas:.2f}')

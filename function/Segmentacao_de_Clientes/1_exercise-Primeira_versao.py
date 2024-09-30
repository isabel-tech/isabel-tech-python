# ### Primeira versão da segmentação de clientes

# Escreva um programa que segmenta clientes com base em suas compras totais.
# O usuário deve digitar o nome do cliente e suas compras totais, e o programa
# deve atribuir cada cliente a um segmento: 'Bronze' para compras de até R\\$ 1000,
# 'Prata' para compras de até R\\$ 5000 e 'Ouro' para compras acima de R\\$ 5000.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie um dicionário vazio para armazenar os clientes e seus segmentos.
# 2. Crie um loop infinito que solicite ao usuário o nome do cliente e suas compras totais.
# 3. Dentro do loop, use uma declaração if para atribuir o segmento apropriado ao cliente.
# 4. Se o usuário digitar 'sair' para o nome do cliente, encerre o loop usando break.
# 5. Fora do loop, use um loop for para imprimir o nome e o segmento de cada cliente.
# 
# Exemplo de saída:
#     
# ```
# Digite o nome do cliente (ou 'sair' para sair): João
# Digite o total de compras: 100
# Digite o nome do cliente (ou 'sair' para sair): Maria
# Digite o total de compras: 2000
# Digite o nome do cliente (ou 'sair' para sair): José
# Digite o total de compras: 6000
# Digite o nome do cliente (ou 'sair' para sair): sair
# João: Segmento do Cliente = Bronze
# Maria: Segmento do Cliente = Prata
# José: Segmento do Cliente = Ouro

#'Bronze' para compras de até R$ 1000
#'Prata' para compras de até R$ 5000 
#'Ouro' para compras acima de R$ 5000
 

clientes_e_segmentos = {}

while True:
	nome_cliente = input("Digite o nome do cliente (ou 'sair' para sair): ").lower()
	if nome_cliente == 'sair':
		break
	compras_totais = float(input('Digite o total de compras: '))
	if compras_totais <= 1000:
		clientes_e_segmentos[nome_cliente] = 'Bronze'
	elif 1000 < compras_totais <= 5000:
		clientes_e_segmentos[nome_cliente] = 'Prata'
	elif compras_totais > 5000:
		clientes_e_segmentos[nome_cliente] = 'Ouro'

for nome_cliente in clientes_e_segmentos:
	print(f'{nome_cliente.capitalize()}: Segmento do Cliente= {clientes_e_segmentos[nome_cliente]}')